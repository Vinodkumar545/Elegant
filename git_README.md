## git commands

1. git config - This command sets the author name and email address respectively to be used with your commits.

```
 $ git config –global user.name “[name]” 
 $ git config –global user.email “[email address]” 
```

2. git init - This command is used to start a new repository.

` $ git init [repository name]
`

3. git clone - This command is used to obtain a repository from an existing URL.

` $ git clone [url]
`

4. git add - This command adds a file to the staging area

` $ git add [filename]
  $ git add * - This command adds one or more to the staging area.
`

5. git commit - This command records or snapshots the file permanently in the version history.

```
  $ git commit -m “[ Type in the commit message]”
  $ git commit -a This command commits any files you’ve added with the git add command and also commits any files you’ve changed since then.
  $ git commit -am "comments" - add all the changed and commit
```

6. git diff - This command shows the file differences which are not yet staged.

`$ git diff
`

7. git status - This command lists all the files that have to be committed

` $ git status
`

8. git rm - This command deletes the file from your working directory and stages the deletion.

` $ git rm [filename]
`

9. git log - This command is used to list the version history for the current branch

` $ git log
`

10. git show - This command shows the metadata and content changes of the specified commit.

` $ git show [commit]
`

11. git branch -  This command lists all the local branches in the current repository.

```
  $ git branch
  $ git branch [branch_name] - This command creates a new branch.
  $ git branch -d [branch_name] - This command deletes the feature branch.
```

12. git checkout - This command is used to switch from one branch to another.

` $ git checkout [branch_name]
  $ git checkout -b [branch_name] - This command creates a new branch and also switches to it.
`

13. git merge - This command merges the specified branch’s history into the current branch.

` $ git merge [branch_name]
`

14. git push - This command is used to push the branch to the github.

` $ git push origin [branch_name]
`

15. git pull - This command is used to pull the branch from the github

` $ git pull origin [branch_name]
`

16. git stash - This command is used to remove all the changes made to the file

` $ git stash 
`

17. git fetch - This command fetches and display all the branches

` $ git fetch
`

