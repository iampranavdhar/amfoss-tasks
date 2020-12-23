# Rust Scrapper

## Tabular Form of the data

|S.No|Country|Toatal Cases|Total Deaths|Total Recovered|
|---|---|---|---|---|
|1|USA|18,687,330|330,841|10,948,136|
|2|India|10,106,499|146,509|9,668,099|
|3|Brazil|7,320,020|188,285|6,354,972|
|4|Russia|2,933,753|52,461|2,343,967|
|5|France|2,490,946|61,702|186,058|
|6|UK|2,110,314|68,307|N/A|
|7|Turkey|2,062,960|18,602|1,866,815|
|8|Italy|1,977,370|69,842|1,301,573|
|9|Spain|1,838,654|49,520|N/A|
|10|Germany|1,556,611|28,241|1,136,700|

## Overview
This task took more time for me and found it little bit difficult than other tasks.

## Getting Output in the CSV file
For getting output in the csv file we can try this with two methods.

### Approach 1
You can directly use the following comand in the terminal:
`cargo run >> filename.csv`
This creates the csv file with the respective filename in the respective project file.

### Approach 2
We can also get this CSV file in the script itself by adding the `csv` dependency.

## Screenshot of output

![Screenshot from 2020-12-23 19-53-57](https://user-images.githubusercontent.com/73348574/103013573-685df900-4563-11eb-9491-6a4521bbc690.png)


## Resources Used
[Programming Rust](https://www.amazon.com/Programming-Rust-Fast-Systems-Development/dp/1491927283/ref=sr_1_1?ie=UTF8&qid=1515194775&sr=8-1&keywords=programming+rust)<br/>
[Scrapping With Rust-Github Repo](https://github.com/kadekillary/scraping-with-rust)<br/>
[Rust-Docs](https://docs.rs/scraper/0.12.0/scraper/)<br/>
