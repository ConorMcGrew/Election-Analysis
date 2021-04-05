# Election-Analysis

## Overview of Election Audit

The purpose of this project is to assist Tom at the Board of Electors in determining the winner of a US congressional precinct in Colarado. We were tasked with determining the total votes, votes for each candidate, percentage of votes for each candidate, the winner (based on simple majority), voter turnout for each county, percentage of vote from each county, and the county with the highest turnout. 

## Election-Audit Results

The overall results of this election audit were:

<img width="322" alt="Screen Shot 2021-04-04 at 8 00 32 PM" src="https://user-images.githubusercontent.com/80495710/113525005-6eab3a80-9580-11eb-9396-ac34d9256cf4.png">

* In total, there were 369,711 votes cast. 

* In terms of county votes cast:

  * Arapahoe county cast 6.7% (24,855) of the total votes. 

  * Jefferson county cast 10.5% (38,855) of the total votes.
  
  * Denver county cast 82.5% (306,055) of the total votes, making it the county with the largest voter turnout.

* In terms of candidate votes received:
  
  * Charles Casper Stockham received 23.0% (85,213) of the total votes.

  * Raymon Anthony Doane received 3.1% (11,606) of the total votes. 

  * Diana DeGette received 73.8% (272,892) of the total votes, making her the winner of the Congressional seat. 

## Election-Audit Summary

Because this script simply continues to add names to a list and then updates the number of votes to a dictionary, it can be used for any csv dataset that contains only the candidate voted for and the place of origin. For example, it could be modified to be used for a state governer election, each candidate could have a breakdown of their total vote and percentage, and we could see the voter turnout for a larger sample of counties. Or it could be used for a presidential election. The county portions would have to be modified to represent states, and the winner would have to be determined by the electoral college vote (so the winner of each state would have to be tracked individually, and then the overall winner would be determined by the particular states won). In any case, this scipt is highly versatile for use in virtually any election review. 
