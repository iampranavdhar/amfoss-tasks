extern crate reqwest;
extern crate scraper;
extern crate csv;

use scraper::{Html, Selector};
use csv::Writer;
use std::fs::File;

#[tokio::main]  //We must include this for using async for main function and we should also include this dependency.Without this we get error
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    
    //Requesting for the data from the url

    let mut req = reqwest::get("https://www.worldometers.info/coronavirus/#countries").unwrap();
    assert!(req.status().is_success());

    let doc_body = Html::parse_document(&req.text().unwrap());
    
    // Selecting the data
    let countries = Selector::parse("#main_table_countries_today tbody:nth-child(2) tr:not([style*=\"display: none\"]):not(.total_row_world)").unwrap();
    

    File::create("casesdata.csv")?;

    let mut csvfile = Writer::from_path("casesdata.csv")?;

    csvfile.write_record(&["S.No","Country","Total Cases","Total Deaths","Total Recovered"])?;



    // For taking just 10 Countries as the records we are using take
    for country in doc_body.select(&countries).take(10){
        let mut countrydata = country.text().collect::<Vec<_>>();
        
        // For removing blank line("\n" and "\n ") and starting from the + without this we get blank lines as output.
        countrydata.retain(|ele| *ele != "\n");
        countrydata.retain(|ele| *ele != "\n ");
        countrydata.retain(|ele| !ele.starts_with("+"));

        //For printing output in the termminal.

        println!("{} {} {} {} {}",countrydata[0],countrydata[1],countrydata[2],countrydata[3],countrydata[4]);

        //For priting  the output in the CSV file.

        csvfile.write_record(&[countrydata[0],countrydata[1],countrydata[2],countrydata[3],countrydata[4]])?;
    }
    csvfile.flush()?;
    Ok(())
}

