"""If they're from 0 to 2 the child should be with parents print : 'Still in Mama's arms' 
If they're 3 or 4 and should be in preschool print : 'Preschool Maniac' 
If they're from 5 to 11 and should be in elementary school print : 'Elementary school' 
From 12 to 14: 'Middle school' 
From 15 to 18: 'High school' 
From 19 to 22: 'College'
From 23 to 65: 'Working for the man' 
From 66 to 100: 'The Golden Years' 
If the age of the person less than 0 or more than 100 - it might be an alien - print: "This program is for humans"""

def stereotype(age):
    if age < 0 or age > 100:
        print "This program is for humans"
    elif age <= 2:
        print "Still in Mama's arms"
    elif age <= 4:
        print "Preschool Maniac"
    elif age <= 11:
        print "Elementary school"
    elif age <= 14:
        print "Middle school"
    elif age <= 18:
        print "High school"
    elif age <= 22:
        print "College"
    elif age <= 65:
        print "Working for the man"
    elif age <= 100:
        print "The Golden Years"    

import sys
with open(sys.argv[1]) as reader:
    for line in reader:
        age = int(line.strip())
        stereotype(age)
            
        