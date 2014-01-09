git_an_adventure
================

This is a collaborative HTML text adventure for learning how to use git and github

<br>
<br>

__RULES FOR THE ADVENTURE__
______________________________________________

* Don't delete files once they are created 
* Don't delete someone's actions (only add actions)
* You can't put photos into the directory (by url link only)
* Keep it clean 
* Have fun!

<br>
<br>

__Process__
______________________________________________
1) Clone the repository 

	git clone https://github.com/AstroJuniorResearcherMeetings/git_an_adventure

1.1) to protect the template.html file

	chmod 444 template.html

1.2) Try running the adventure by

	In Web Browser (e.g. firefox) ==> File ==> Open File ==> git_an_adventure/START.html

2) Change/create a file by copying the template.html then modifying

	cp template.html new_file_name.html

3) Add the new file/change to cache

	git add new_file_name.html

4) Commit the new adds to the staging area
	
	git commit -m "message describing the change"

5) Pull the changes from repository

	git pull

5.1) Possibly resolve conflicts/merge changes by opening up the file and editing the differences so they make sense
	

6) Push your changes
	
	git push

7) Read other's changes by repeating 1.2 or pressing refresh on your web browser

8) Rinse and repeat steps 2 through 7

<br>
<br>
<br>

__Tips__
______________________________________________

Set git config global variables of the user name and email

	git --global user.name "My Name"
	git --global user.email "my_email@utah.edu"

To check the status of your directory

	git status

To check the past commits of the directory

	git log

For help on any git command type --help

	git --help 

	git add --help

	git merge --help

Keep the git figure in mind. Each arrow is a git command (e.g. git add ==> puts files from the working directory to the cache)

<img src="http://www.308tube.com/youtube/github/img/Git_flow.png">

