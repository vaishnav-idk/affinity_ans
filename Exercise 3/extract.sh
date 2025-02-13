#!/bin/bash
#taking value from the website link via curl redirticting into txt file

curl https://www.amfiindia.com/spages/NAVAll.txt > nava.txt

#using awk to extract data from txt file as columns

awk -F ';' '{print $4 \t\t $5}' nava.txt > nav.tsv

#in awk command -F command to make ; as separator and printing $4 and $5th colum the scheme name and assest column

#attempting to maintian subheading  and some formatting

awk -F ';' '{
#using regex to take print subheading (they dont have ; )
/^[^;]*$/{
print
}

#now to print normal lines we take the idea that they start with numbers
/^[0-9]/{
printf "%s %s\n", $4, $5
}

#trying to print header using begin command
BEGIN{
printf "%s %60s\n", "Scheme Name", "Net Asset Value"
}
