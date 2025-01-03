# untracked until committed because it is 
#made in VS only
#use "git restore --staged <file>..." to unstage
'''
cd <filename> (to change directory)
mkdir <filename> (make new diectory)
git config --global user.name "My name"
git config --global user.email "my email"
git --config list (to see everything configuredcd z)
git --version
git clone <link of file>
git add <filename(with extension)>    git add .  (add all files in folder)
git status(to check the status of files(U,A,M))
U -->untracked(not uploaded),M -->Modified(to be added),A --> Added and ready to commit
git commit -m "Message"
git push origin <branch name>
git init (to make the working file a git directory)
<Branch Commands > :
git branch     (to check branch)
git branch -M "new name"  (to rename branch)
git switch <branch name> (to navigate or move from one branch to another)
git branch <branch name> (to make new branch)
git branch -d <branch name> (to delete branch)  can't delete the working branch 
git pull origin main (to pull merged branch on VS code from github)
git merge <branch name>  (merge branch with opened branch)
git log (to check all commits till done)
git reset HEAD~1 (the latest commit is called HEAD & ~1 means to shift HEAD one step back) ,(print q to quit)

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   restore    Restore working tree files
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   diff       Show changes between commits, commit and working tree, etc
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   backfill   Download missing objects in a partial clone
   branch     List, create, or delete branches
   commit     Record changes to the repository
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   reset      Reset current HEAD to the specified state
   switch     Switch branches
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects
'''