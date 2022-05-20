'''
Created By: Kayla Mahan
Created On: November 19th, 2020
Last Modified By:
Last Modified On:
Course: Forensics F20
Assignment: Lab 9
Purpose: Email Analysis
'''

# Import for retrieving and parsing whoisdata from
# IP addresses and using regular expressions
from ipwhois import IPWhois
from pprint import pprint
import warnings
import re
import socket

# Class that implements functionality to detect a spoofed email
class DetectSpoof():

    # Initializes an object of the DetectSpoof class.
    # self -        this specific DetectSpoof object.
    # inputFile -   the text file containing the raw email in question.
    def __init__(self, inputFile):

        # The Class Banner
        self.banner()

        # The email header's file name and raw string
        self.spoofed_email = inputFile

        self.outFile = "Email Header Report.txt"

    def openFile(self, headFile):
        x = []
        with open(headFile, "r") as header:
            for i in header:
                x.append(i.split("\n"))
        x = [[j.strip() for j in i if j!=''] for i in x if i!=None]
        return x

    def permitted(self, headList):
        permit = [[j for j in i if "designates" in j] for i in headList]
        permit = list(filter(None, permit))
        return permit

    def ipAddresses(self, headList):
        ipAddresses = [re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
                                  str(j)) for i in headList for j in i]
        ipAddresses = list(filter(None, ipAddresses))
        return ipAddresses
    
    def fullyQualifiedDomain(self, headList):
        fullDomain = [re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))",
                                 str(j)) for i in headList for j in i]
        fullDomain = list(filter(None, fullDomain))
        return fullDomain

    def topLevelDomain(self, headList):
        topLevel = [re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}',
                               str(j)) for i in headList for j in i]
        topLevel = list(filter(None, topLevel))
        return topLevel

    def emailAddresses(self, headList):
        email = [re.findall(r'[\w\.-]+@[\w\.-]+', str(j)) for i in headList for j in i]
        email = list(filter(None, email))
        return email

    def replyTo(self, headList):
        reply = [[j for j in i if "Reply" in j] for i in headList]
        reply = list(filter(None, reply))
        return reply

    def writeParsedHeader(self, ip, ipParse, domain, topLevel, emailAddr, replyTo, permitted):
        x = len(ip)
        sus = 0
        valid = 0
        destip = 0
        srcip = 0
        try:
            with open(self.outFile, "w") as parsed:
                for item in ip:
                    if x == len(ip):
                        print(str("[Destination IP] ")+
                                     "".join(i for i in str(item) if i not in "[]'\n"))
                        destip = ("".join(i for i in str(item) if i not in "[]'"))
                        try:
                            obj = IPWhois(destip)
                            results = obj.lookup_whois()
                            print("Country: " + results['nets'][0]['country'])
                            print("Name: " + results['nets'][0]['name'])
                            print("Description: " + results['nets'][0]['description'])
                            print("Emails:")
                            print(results['nets'][0]['emails'])
                            print()
                        except Exception as e:
                            print(e)
                    elif x == 1:
                        print(str("[Source IP] ")+
                                     "".join(i for i in str(item) if i not in "[]'\n"))
                        srcip = ("".join(i for i in str(item) if i not in "[]'"))
                        try:
                            obj = IPWhois(srcip)
                            results = obj.lookup_whois()
                            print("Country: " + results['nets'][0]['country'])
                            print("Name: " + results['nets'][0]['name'])
                            print("Description: " + results['nets'][0]['description'])
                            print("Emails:")
                            print(results['nets'][0]['emails'])
                            print()
                        except Exception as e:
                            print(e)
                    x = x-1



                ans = input("Is destination IP suspicious? Y or N\n")
                if ans == 'Y' or ans == 'y':
                    print("RESULTS: Destination IP address is suspicious\n")
                    sus = sus + 1
                else:
                    print("RESULTS: Destination IP address is not suspicious\n")
                    valid = valid + 1

                ans = input("Is source IP suspicious? Y or N\n")
                if ans == 'Y' or ans == 'y':
                    print("RESULTS: Source IP address is suspicious\n")
                    sus = sus + 1
                else:
                    print("RESULTS: Source IP address is not suspicious\n")
                    valid = valid + 1
                
                print("\n---TOP LEVEL DOMAINS---")
                print(self.generateOutput(topLevel))

                ans = input("Do any of the domains look suspicious? Y or N\n")
                if ans == 'Y' or ans == 'y':
                    print("RESULTS: One or more domains seem suspicious\n")
                    sus = sus + 1
                else:
                    print("RESULTS: None of the domains seem suspicious\n")
                    valid = valid + 1

                print("\n---LINKS---")
                print(self.generateOutput(domain))    

                ans = input("Do any of the links look suspicious? Y or N\n")
                if ans == 'Y' or ans == 'y':
                    print("RESULTS: One or more links seem suspicious\n")
                    sus = sus + 1
                else:
                    print("RESULTS: None of the links seem suspicious\n")
                    valid = valid + 1                       

                print("\n---E-MAIL ADDRESSES---")
                print(self.generateOutput(emailAddr))

                ans = input("Do any of the email addresses look suspicious? Y or N\n")
                if ans == 'Y' or ans == 'y':
                    print("RESULTS: One or more addresses seem suspicious\n")
                    sus = sus + 1
                else:
                    print("RESULTS: None of the addresses seem suspicious\n")
                    valid = valid + 1  

                print("\n---Authentication---")
                print(self.generateOutput(permitted))

                if re.search('fail', self.generateOutput(permitted)):
                    print("RESULTS: Authentication did not pass\n")
                    sus = sus + 1
                else:
                    print("RESULTS: Authentication passed\n")
                    valid = valid + 1 

            parsed.close()

            count = 0
            with open(self.spoofed_email, 'r+') as email:
                for line in email:        
                    if line.startswith('Date:'):
                        if count < 1:
                            print(line)
                            ans = input("Is the date reasonable? Y or N\n")
                            if ans == 'N' or ans == 'n':
                                print("RESULTS: Date is not reasonable\n")
                                sus = sus + 1
                            else:
                                print("RESULTS: Date is reasonable\n")
                                valid = valid + 1
                        count = 1
            
            print("Sus results",sus)
            print("Valid results", valid)
            if sus > valid:
                print("FINAL RESULTS: Email is suspicious")
            else:
                print("FINAL RESULTS: Email is not suspicious")
        except Exception as ex:
            flag = ("Encountered error when writing output file.\n%s" % (ex))

    def generateOutput(self, prop):
        propString = ""
        for item in prop:
            propString = propString + (''.join(i for i in str(item) if i not in "[]',\n")+ "\n")
        return propString

    def ipParse(self, ip):
        PrivIp = ["10.", "192.", "172.", "127."]

        public = [[j for j in i if j[0:3]!= PrivIp[0] and j[0:4] != PrivIp[1]
                   and j[0:4] != PrivIp[2] and j[0:4] != PrivIp[3]] for i in ip]
        
        private = [[j for j in i if j[0:3] == PrivIp[0] and j[0:4] == PrivIp[1]
                    and j[0:4] == PrivIp[2] and j[0:4] == PrivIp[3]] for i in ip]

        public = list(filter(None, public))
        private = list(filter(None, private))
        
        return public, private

    # Runs Spoof by calling its core functions.
    # self - this specific Spoof object.
    def run(self):
        head = self.openFile(self.spoofed_email)
        head = [[x.split() for x in y] for y in head]

        ip = self.ipAddresses(head)
        fulldomain = self.fullyQualifiedDomain(head)
        topLevel = self.topLevelDomain(head)
        emailAddr = self.emailAddresses(head)
        repto = self.replyTo(head)
        ipParse = self.ipParse(ip)
        permit = self.permitted(head)

        print(self.writeParsedHeader(ip, ipParse, fulldomain, topLevel, emailAddr, repto, permit))

    # Prints out our program's banner.
    def banner(self):
        """
        Generated by http://patorjk.com/software/taag/
        """
        print("\n")
        print("________          __                 __      _________                     _____   ")
        print("\______ \   _____/  |_  ____   _____/  |_   /   _____/_____   ____   _____/ ____/  ")
        print(" |    |  \_/ __ \   __\/ __ \_/ ___\   __\  \_____  /\____ \ /  _ \ /  _ \   __\   ")
        print(" |    `   \  ___/|  | \  ___/\  \___|  |    /        \  |_> >  <_> |  <_> )  |     ")
        print("/_______  /\___  >__|  \___  >\___  >__|   /_______  /   __/ \____/ \____/|__|     ")
        print("        \/     \/          \/     \/               \/|__|                        \n")
