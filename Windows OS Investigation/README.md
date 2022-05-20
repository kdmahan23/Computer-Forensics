# Forensics Lab 03 - Windows OS Investigation
This lab is meant introduce you to forensic investigations on Microsoft Windows operating
systems and using larger GUI based forensic analysis tools. You will be required to perform dead analysis using *Autopsy* on a system running Windows 10 in order to recreate a timeline of events on the system.

---

## Procedure<a name="procedure"></a>
The year is 2025. A strange computer is found, and you must determine the events that took place and find all five of the hidden flags as well as create a timeline of **all** events that occurred on the computer. 

### Part 1 - Acquire the Image
**Steps for Physically Acquiring**
1. Put on gloves so at not to contaminate evidence
2. Check with other investigators to see if you can remove evidence yet.
3. Either out entire desktop into evidence bag or remove just the hard drive and put it in an evidence bag.
4. Take it back to the lab and check it into evidence.
6. Create an image of the hard drive so you aren't using the actually hard drive to analysis. This allows the court to know you did not tamper with the evidence while analyzing it 
7. Create a hash value of the image and the physical hard drive, this will be used to verify the authenticity of the acquired image.

**Hashes** 
- First three Autopsy runs
  - MD5: `ea6244e539af6b363b4c5e760d9137b9`

---

### Part 2 - Analyze the Image
I analyzed the given image four different times in Autopsy to gain as much information as I could. I used the same hash each time. I then went through each analysis created to put together 
a timeline of events and find the flags.
The hash verification did not pass. I am unsure why this is. I double checked the hash with different hash generators and got the same hash.

**Analysis**
- Name: DESKTOP-E2H5CVP

- Operating System: Windows 10 Home

- Processor Architecture: AMD64

- Owner: forensics@lab5.com

- Installed Programs: 26

- USB Device Attached: 12

- Web Bookmarks: 9

- Web Cookies: 1058

- Web Downloads: 54

- Web History: 120

- Web Search: 40

- EXIF Metadata: 5
  - 4 JPEGS
  - 1 PNG
- Metadata: 83
  - m4a files
  - rtf files
  - MsoIrmProtector files
    - .doc
    - .xls
    - .ppt
- Recent Documents: 12
  - 4 JPEGS
  - 1 PNG
  - 1 GIF
  - 6 Unknown
- Recycle Bin: 5
  - 3 JPEGS
  - 1 PNG
  - 1 GIF
- User Accounts: 16
  - Toph
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
  - Iroh
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
  - Katara
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
  - Sokka
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
  - Zuko
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
  - Ozai
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
  - Administrator
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
    - Description: Built-in account for administering the computer/domain
    - Account Settings: Account Disabled
  - foren
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
    - Email: forensics@lab5.com
  - Aang
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
  - defaultuser0
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
    - Account Settings: Account Disabled
  - WDAGUtilityAccount
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
    - Description: A user account managed and used by the system for Windows Defender Application Guard scenarios.	
    - Account Settings: Account Disabled
  - DefaultAccount
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
    - Description: A user account managed by the system.	
    - Account Settings: Account Disabled
  - Guest
    - Created: Sept. 1st, 2020
    - Flag: Normal user account
    - Description: Built-in account for guest access to the computer/domain	
    - Account Settings: Account Disabled

**Timeline**
- July 2004
  - Microsoft Office applications installed
- June 2015
  - Skype installed
- March 2015
  - Skype updated
- December 2019
  - Installed multiple programs
- September 2020 (This is where everything happens)
  - paisho.jpeg
    - Created: Sept. 7th, 2020
    - Modified: Sept. 7th, 2020
    - Accessed: Sept. 7th, 2020
    - Changed: Sept. 7th, 2020
  - spartan.edb
    - Created: Sept. 1th, 2020
    - Modified: Sept. 7th, 2020
    - Accessed: Sept. 7th, 2020
    - Changed: Sept. 7th, 2020
  - cabbageman.jpeg
    - Created: Sept. 7th, 2020
    - Modified: Sept. 7th, 2020
    - Accessed: Sept. 7th, 2020
    - Changed: Sept. 7th, 2020
  - $RHTZARL.png
    - Created: Sept. 7th, 2020
    - Modified: Sept. 7th, 2020
    - Accessed: Sept. 7th, 2020
    - Changed: Sept. 7th, 2020

**Flags**
- flag{you_do_always_come_back}
  - Found in Web Bookmarks
  - Title of source file 'spartan.edb'

![](./imgs/flag1.png)

- flag{white_lotus}
  - Found while looking through the files on the hard drive
  - Found within the text paisho.jpeg. JPEG was located on desktop of user Iroh

![](./imgs/flag2.png)

- flag{my_cabbages}
  - Found while looking through the timeline created by Autopsy
  - Found on the desktop of user Toph

![](./imgs/flag3.png)

- flag{then_everything_changed_when_the_fire_nation_attacked}
  - Found while looking through the timeline created by Autopsy
  - Found in the Recycle bin

