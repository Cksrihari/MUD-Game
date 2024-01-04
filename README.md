git clone https://github.com/amansethuea/webdev9.git

git status → to check the current modified / newly added or deleted files on the branch you working on

If there are important untracked files and you like to add them to tracked files, do the following:-
git add <path_and_name_of_file>

Check git status and you should be able to view the files in tracked files

Un-important files can be ignored and removed using the following commands:-

git clean -n → lists out the untracked files that would be removed

git clean -f → removes untracked / unwanted files

On main branch : -

git pull → pulls the latest code

git branch → view branches

git branch -D <branch_name> → deletes unused branches

git checkout -b <local_branch> → creates a local branch

Now you have the same code as master branch i.e main on your newly created local branch

Do your code

git add * → adds all the files to the git [NOTE: add doesn’t mean its merged]

or git add <file_name> → if you want to add specific file

git commit -m “appropriate meaningful message “

git push → it gives the upstream command on the prompt, copy that and run that.

Go to github and branches → go to your local branch → create pull request

wait for request to merge

once merged, go back to terminal → git checkout main

git pull → see the merged changes

git branch -D <local_branch_name> → deletes the local branch which is not used by you anymore

git checkout -b <new_local_branch> → creates a new local branch

repeat the same process again
 
