#importing
import subprocess
from subprocess import call


print "Enter 1 for 1st query, 2 for 2nd, 3 to update and 4 to quit"
c=raw_input()
while c!="4":
    if c=="2":
        print "Enter the Application ID:\t"
        r = raw_input();
        print subprocess.check_output(['swipl','-q', '-s', 'facts_and_rules.pl', '-g' ,"list("+r+"),halt."])
    if c=="1":
        print "Enter the application ID:\t"
        r = raw_input();
        print "Enter the machine ID:\t"
        x = raw_input();
        r = r+", "+x
        counter = 0
        x = subprocess.check_output(['swipl','-q', '-s', 'facts_and_rules.pl', '-g' ,"newlist("+r+"),halt."])
        print x
        for i in x:
            if i==",":
                counter = counter+1
        if len(x)>3:
            counter = counter+1
        
        if counter==0:
            print "No"
        else:
            print "Yes"    
    if c=="3":
        call(["python", "facts_gen.py"])
    print "Enter 1 for 1st query, 2 for 2nd, 3 to update and 4 to quit"
    c = raw_input();
