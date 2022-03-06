# GIT introduction

https://gitlab.uw.edu.pl/python-tools/git-laboratory
https://gitlab.mimuw.edu.pl/python-tools/git-laboratory

## Local work

 *  `git init` – create an empty repository
 *  `git status` – check status of repository
 *  `git add <paths>` – add files to repository
 *  `git add -u` – add updated files
 *  `git add -A` – add all files 
 *  `git rm <path>` – remove files from repository
 *  `git rm --cached <paths>` – remove files from the repository but keep a local copy.
 *  `git commit -m "<message>"` – create a commit with the currently added files, with `<message>` as the commit description
 *  `git branch <name>` – create a new branch with name `<name>`
 *  `git checkout <name>` – change the current branch to the branch named `<name>` 
 *  `git checkout -b <name>` – create a new branch with name `<name>` and checkout to it (equivalent to the sequence of commands: `git branch` and `git checkout`)
 *  `git reset` - revert changes locally
 *  `git revert` – create a commit reverting the changes introduced by a given list of commits 
 *  `git merge` – create a commit which merges the contents of two branches
 *  `git rebase` – take diverging commits from one branch and put them on top of the other one
 *  `git log` – show history of commits in the current branch
 
### Exercise 1
Create a new repository in directory `sample_project`. Add two
commits with the following descriptions: "initial commit" and "first changes". 
History of commits should look like:
```
commit 6a2cf1d03f2429573c0a8baa99fb54296998c5b6 (HEAD -> master)
Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
Date:   Fri Nov 6 16:09:41 2020 +0100

    first changes

commit ebc2cdb495c93951e6c33657ac6d38561ff1e3b2
Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
Date:   Fri Nov 6 16:09:20 2020 +0100

    inital commit
```
 
### Exercise 2
Create two branches in the repository. Each should contain at least one commit not present in the other. 
 
```bash
$ git log --graph --all
* commit 6b0a08d280a573835339e66271a36f815299a26c (HEAD -> develop)
| Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
| Date:   Fri Nov 6 16:23:12 2020 +0100
| 
|     begin develop branch
|   
| * commit 6a2cf1d03f2429573c0a8baa99fb54296998c5b6 (master)
|/  Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
|   Date:   Fri Nov 6 16:09:41 2020 +0100
|   
|       first changes
| 
* commit ebc2cdb495c93951e6c33657ac6d38561ff1e3b2
  Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
  Date:   Fri Nov 6 16:09:20 2020 +0100
  
      inital commit
```

_Command `git log --graph --oneline --all` is nice to use_

### Exercise 2.2

Create a repository with at least 3 commits. Create branch `develop` and reset `master` branch to previous commit. 
Results should be similar to:   

```
* 42b2f9e (develop) third commit
* baad3d7 (HEAD -> master) second commit
* 0183122 initial commit
```

### Exercise 3
Edit the same line of the same file in two different branches. Try the merge and rebase operations on these two branches.
 
  
## Remote work
 
 *  `git clone` – clone a remote repository locally
 *  `git pull` – pull changes from remote and update the local branch
 *  `git fetch` – update information from remote repository
 *  `git push` – push changes to the remote repository
 
### Exercise 4
Clone the [https://gitlab.uw.edu.pl/python-tools/git-example-repo](https://gitlab.uw.edu.pl/python-tools/git-example-repo)
repository and compare the local version with the server one. 
 
### Exercise 5
Create an empty repository on [https://gitlab.uw.edu.pl](https://gitlab.uw.edu.pl). 
Clone it locally, modify it and push the changes to the gitlab repository.

(information about ssh access configuration https://gitlab.uw.edu.pl/help/ssh/README.md) 
 
### Exercise 6
Create one commit using the web interface and use `git fetch` command and second commit locally.
Then use `git log --graph --oneline --all` to see the results. 

 
## .gitignore
_Files which name starts from `.` are hidden on unix systems_

To avoid unintentionally adding files to the repository (like temporary files and local data),
a mechanism of file exclusion, based on the simple path matching to a set of expressions, was introduced. 
There are two locations where the user can put these expressions:

_Exclusions are applied only to new files. So if a file is tracked by git, then any changes in `.gitignore` will not affect it._

* `.gitignore` – will be synchronised with other computers,
* `.git/info/exclude` – apply only on local machines.

A few examples of rules:

* `*.tmp` – ignore all files with extension `.tmp`
* `__pycache__/` - ignore content of all directories named `__pycache__`
* `/__pycache__/` - ignore content of top level directory named `__pycache__` 

To keep a folder in the structure of repository, but not trace its content (e.g. data storage) you need to use two expression in `.gitignore`:

```
data/*
!data/.keep
```

as well as keep an empty file in the directory, which in this example is named `.keep`.



Here is a good generator of gitignore files, which is a good starting point in project 
[https://gitignore.io](https://gitignore.io)


### Exercise 7 
Initialize a new repository then add to it a .gitignore file which excludes `.txt` files. 
Then create the following files: `test.py` and `test.txt`. Try to add both of them to the repository. 
Confirm that only `test.py` was added. (Do not use the `--force` option when commiting)


## Additional materials

Visualization of basic commands: [https://onlywei.github.io/explain-git-with-d3](https://onlywei.github.io/explain-git-with-d3)

Big file (e.g. binary blobs) storage: Git lfs [https://git-lfs.github.com/](https://git-lfs.github.com/)

### GIT GUI 

Let's check out the following ones:

 * IDE built-in GUI (PyCharm, VSCode, etc)
 * GitEye 
 * GitKraken

A longer list of clients can be found here: [https://git-scm.com/downloads/guis](https://git-scm.com/downloads/guis)

### Git Services 

 * GitHub – [https://github.com/](https://github.com/)
 * Gitlab – [https://about.gitlab.com/](https://about.gitlab.com/)
 * Bitbucket - [https://bitbucket.org/](https://bitbucket.org/)
 * Overleaf - [https://www.overleaf.com/](https://www.overleaf.com/); an online LaTeX editor with git support [https://www.overleaf.com/user/bonus](https://www.overleaf.com/user/bonus) 

### Links
 * Official manual [https://git-scm.com/book/](https://git-scm.com/book/)
 * Tutorials from gitkraken authors [https://www.gitkraken.com/resources/learn-git](https://www.gitkraken.com/resources/learn-git)
 * Github help [https://guides.github.com/](https://guides.github.com/)
