# Sir Perceval's quest

This task was super interesting though little bit difficult for someone who are new to these tools and Github.

## Modules Used
I used request module and imported git from perceval.backends.core.git

## Problems Faced
Initially I was iterating only the url of the git repository and not the repository directory by mistake and instead of fetching the data I had filtered the commits and extracted the commit info which given output in the form of bandit password but then [vchrombie](https://github.com/vchrombie) had guided me to observe that logical error and to just get the commits data and not to filter it.

## Result
For result we have to be in the respective directory and type the following command in the terminal for executing the script and to get the data into the `commits.json` file:

`python3 perceval.py --json-line >>  commits.json`

