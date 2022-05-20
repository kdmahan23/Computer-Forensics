# Forensics Lab 04 - Linux OS Investigation
This lab is meant introduce you to forensic investigations on Linux based operating systems
and make you comfortable with Linux internals in a purely terminal environment. You will be
required to analyze a live system running Ubuntu Server 16.04 and recover sensitive data which
has been maliciously hidden. 

---

## Procedure<a name="procedure"></a>
The Black Mesa Research Corporation has had an incident! The research and development group's
central database has be hacked by what it believes to be a competing research laboratory - Aperture Science! Black Mesa says all of their backups have been destroyed in a forensically sound, unrecoverable manner. All they have left is the virtual machine containing a copy of the central database server immediately after the attack occurred. Luckily, their Intrusion Detection System uses heuristics based machine learning algorithms which detected *weird* activity on the Black Mesa server and isolated it from the internet before any **corporate secrets** could be exfiltrated. That being said, their top scientist have been unable to recover the vital information stored on the VM. They report that everything's been moved around and hidden, the system exhibits strange behavior, and also something about trains... In a last ditch effort, Black Mesa Research Corporation has uploaded a copy of the server for you to access. It is up to you to recover Black Mesa's vital corporate information.

Black Mesa has given us the following information and restrictions:
- Black Mesa said the attacker changed all the system's passwords, but they did discover the password to account "subject1498" is "stillalive".
- We've been told by Black Mesa that Dead analysis, along with any sort of data carving, is strictly prohibited. Who knows why.
- Black Mesa also says the use of GRUB is prohibited and that you must proceed through their "Test Chambers" sequentially
- Black Mesa does not have the ability to install new applications on their server. You must recover the Corporate Secrets using only what is already present on the machine.
- We've been told very little about the Corporate Secrets themselves, other than that they are stored in 5 of what Black Mesa calls Global Interest Files.

I started off by taking a snapshot of the machine and then using the login credentials given to us by Black Mesa. Upon logging in, text pops up that says "Systematically uninstalling test subject in" and then begins to count down. Once it reaches 1, it begins deleting most of the files of 'subject1498'.

![](./imgs/login.png)

After this, I was still logged in as the user but when I checked the files and directories, there was very little. 

![](./imgs/hiddenbashfile.png)

There was a directory named "root_only!" that the user did not have access to and a hidden file named ".bash_login". Since, the hidden file was the only thing I was able to access, I used the command `nano` to view the contents of the file. 

![](./imgs/bashfile0.png)
![](./imgs/bashfile1.png)

The first comment gives a hint that something in this file may help me to stop everything from getting deleted. Looking through the file, I found an if-else statement that states if the word "cube" is not entered after logging in that the script will delete the specified files and directories. The if-else was the only interesting information inside the hidden file.

Knowing this, I reverted back to the snapshot of the machine I took before logging in and logged in again, making sure to enter "cube" before the countdown ended. This time I got a message that the abortion sequence had been received and that I had passed the welcome test. 

![](./imgs/abortpass.png)

Checking for files and directories again using the command `ls -al`, I found a lot more since they hadn't been deleted, including a directory called "test_chamber_1".

![](./imgs/filelist0.png)

Upon seeing the test chamber, I tried to change to that directory but instead of going into that directory I received a try again message and a train. Since I couldn't get into that directory, I started to look at the other files present to see what could possibly be blocking me. The file ".bash_aliases" looked interesting so I tried to open it with `nano`, however instead of opening the file I received a train again. Since `nano` did not work, I used the command `cat' to show the contents of the file. 

![](./imgs/bashaliases.png)

The contents of the file showed that a lot of the common commands had been aliased to run a program that makes a train run across the terminal window. I had found part of the reason I couldn't get into the test chamber directory. To remove the aliases, I used the `cat` command to erase the contents of the file. 

![](./imgs/removealias1.png)

Once this was done, I tried to use the `cd` command to get into the directory and was met again with the train. This meant that `cd` was still aliased, but was not in the ".bash_aliases" file. To unalias `cd`, I ran `unalias cd` in the command line. Since I received no input, I knew the command was successful. This allowed me to get into the test chamber directory.

Once in the directory, I started exploring. There were multiple directories with more directories in them. Which would have taken forever to look through each one individually. So I used the `file` command to locate all the files, but even this was too much information and most of the files were named "nope.txt" and were empty. Since I knew I was probably looking for a non empty file, I used `file` again with different flags to show me all the nonempty files within the test chamber. This produced 2 files. One of the files was an accident on my part and the other was a PNG.

![](./imgs/testchamber1.png)

The file path of the PNG was interesting, so I made sure to keep that in mind going forward. I navigated to the PNG and tried to open it using `nano`, but was told that it did not have read permissions. So I tried to use `chmod` and was met with the train. So I knew something was blocking me again. Remembering the file path of the PNG, I ran `which chmod` to find the path of the command. I noticed that it had a weird path file and navigated to it. Once there I ran `ls -al` and notice that chmod was linked to a file path that lead to the train. To remove this, I ran `unlink chmod` 

![](./imgs/chmodlink.png)

This allowed me to use `chmod` to give the PNG read permissions and open the PNG using `nano`. 

![](./imgs/readpermisson.png)

![](./imgs/cake.png)

The contents were very interesting and mentioned using my new found power. This made me automatically think 'root access' so that I could get into "root_only!". The first line looked like it might be a password so I ran the command `su root` and entered the first line just like it appeared in the file. The password worked and I now have root access. 

![](./imgs/root.png)

This allowed me to get into the "root_only!" directory which held a directory called portal that was was linked to the "lost+found" directory of the machine. Within it, I found test chamber 2 as a hidden directory.

![](./imgs/testchamber2.png)

Once in the test chamber I found 10 other directories that when read together say "Perseverance is key just keep looking over and over again". After multiple attempts at trying to find anything within the directories and having files disappear and move, I figured the directory the test chamber was in was causing these issues to make it difficult for me to find information. So I moved the entire test chamber outside of the "portal" directory into  "root_only!"

![](./imgs/testchamber2_1.png)

Once that was complete I ran `ls -alfsR` to list all the contents of the directories within the 2nd test chamber. Most of the directories were empty but I found some that I could explore. 

![](./imgs/list1.png)
![](./imgs/list2.png)
![](./imgs/list3.png)

I navigated to the different directories and viewed each file I came across. 

![](./imgs/readme.png)

![](./imgs/corpsecrets.png)

![](./imgs/actualsecrets.png)

![](./imgs/hint.png)

I finally get into a hidden directory that holds test chamber 3. 

![](./imgs/testchamber3.png)

This test chamber held a lot of files. None of them looked like GIFs or seemed interesting at all. I decided to run `file` with certain flags to see what the files actually were despite their name. Doing this revealed the 5 Black Mesa files we were searching for.

![](./imgs/file0.png)

![](./imgs/file1.png)

I moved these files into a different folder to be extracted to my host machine.


---

### Collaborators 
Colton Gwin  
Sebastien Dulor  
Carly Hughes