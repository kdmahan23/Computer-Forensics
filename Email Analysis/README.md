# Forensics Lab 09 - Email Analysis
This lab is meant to introduce students to the basics of email
tracking by teaching how to properly read email header information. Email
phishing scams are widely used by cyber criminals to lure unsuspecting
users into revealing sensitive personal information. By building mock
registration pages for commonly used web services such as social networking
sites, online auctioning and banking services; criminals are able to cash
in on a user’s inherent trust. Students will implement a class in Python to
parse an email's header file and attempt to detect if it was a spoofed email
or legitimate. 

---

To use my python script, all you have to do is type the following into the command line
`python3 Toolkit.py spoof -i <Path to input file>`

My code uses a lot of user input because I thought this was a better way of detecting spoof emails. Each test tallies up whether the user decided if the test passed or not and at the end shows the number for both counts, sus and valid, and displays if the email seemed suspicious or not. 

The first test that comes up is about the destination IP address. I wasn't able to figure out how to incorporate ipwhois into my code, so when this test comes up, I just looked up the IP address online instead. The second test is the same, it just asks about the source address instead of the destination address

Most of the other tests are self explanatory and is up to the user's discretion of whether or not something seems suspicious.

The last test has to do with the date. The date is displayed in the terminal and the user is asked if the date is reasonable. For some of the dates, I looked at a calendar to see if the date lined up correctly. 

**Q1:** In your email client, how do you view the header of an email?
- I personally use Gmail as my main email client. To view the full header of the email, you click on the three dots in the top right corner and then click show original

**Q2:** Of the provided emails, which were normal and which were suspicious?
- Header 0: Normal
- Header 1: Normal
- Header 2: Suspicious
- Header 3: Normal
- Header 4: Suspicious
- Header 5: Suspicious
- Header 6: Normal
- Header 7: Normal
- Header 8: Suspicious
- Header 9: Normal

**Q3:** For each suspicious email, indicate exactly which tests failed?
- Header 2: Suspicious
    - Date was not reasonable
    - Some of the email addresses were suspicious
- Header 4: Suspicious
    - Both IP addresses were suspicious 
    - Some of the email addresses looked suspicious
    - One of the authentications did not pass
- Header 5: Suspicious
    - Both IP addresses were suspicious 
    - Suspicious link
- Header 8: Suspicious
    - Both IP addresses were suspicious 
    - Some of the email addresses looked suspicious
    - Authentications did not pass
    - Date was not reasonable

**Q4:** Where were the suspicious emails coming from?
- Two of the suspicious emails came from North Korea

**Q5:** Who is going to study abroad and where are they going?
- James, Garrett, and Erin
- North Korea
---