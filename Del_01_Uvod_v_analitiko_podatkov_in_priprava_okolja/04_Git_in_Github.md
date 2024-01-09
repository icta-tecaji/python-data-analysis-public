# Git in Github

## Osnove Git-a

- [Introduction to Git and GitHub for Python Developers](https://realpython.com/python-git-github-intro/)
- [Git Book](https://git-scm.com/book/en/v2)
- [Become a git guru](https://www.atlassian.com/git/tutorials)

**Git is a distributed version control system (DVCS).**

A **version control system (VCS)** is a set of tools that track the history of a set of files. This means that you can tell your VCS (Git, in our case) to save the state of your files at any point. Then, you may continue to edit the files and store that state as well. Saving the state is similar to **creating a backup copy of your working directory**. When using Git, we refer to this saving of state as making a commit.

When you make a commit in Git, you add a commit **message that explains at a high level what changes you made in this commit**. Git can show you the history of all of the commits and their commit messages. This provides a useful history of what work you have done and can really help pinpoint when a bug crept into the system.

In addition to showing you the log of changes you’ve made, Git also allows you to **compare files between different commits**.

> Check if git is installed: `git --version`. If not use the page [Download for Windows](https://git-scm.com/download/win) to install it.

### Creating a New Repo

- To work with Git, you first need to tell it who you are. You can set your username and email with the git config command:
  - `git config --global user.name "your name goes here"`
  - `git config --global user.email "your email goes here"`
- Once that is set up, you will need a repo to work in. Creating a repo is simple. Use the git init command in a directory:

  - `mkdir example`
  - `cd example`
  - `git init`

- Once you have a repo, you can ask Git about it. The Git command you’ll use most frequently is `git status`.
- With your favorite editor, create the file hello.py, which has just a print statement in it.
- If you run `git status` again, you’ll see a different result.
- Now Git sees the new file and tells you that it’s untracked. That’s just Git’s way of saying that the file is not part of the repo and is not under version control. We can fix that by adding the file to Git. Use the git add command to make that happen: `git add .`
- When you commit changes, you are telling Git to make a snapshot of this state in the repo: `git commit -m "creating hello.py"`

They don’t do any communication to a server or over the network. It turns out that there are only four major Git commands which actually talk to remote repos:

- `clone`
- `fetch`
- `pull`
- `push`

## Osnove Github-a

- [GitHub Docs](https://docs.github.com/en)
- [Hello World](https://docs.github.com/en/get-started/quickstart/hello-world)

GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

1. [Signing up for GitHub](https://docs.github.com/en/get-started/signing-up-for-github)
2. [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
3. [Creating a repository](https://docs.github.com/en/get-started/quickstart/create-a-repo)
   - A repository is usually used to organize a single project. Repositories can contain folders and files, images, videos, spreadsheets, and data sets -- anything your project needs. Often, repositories include a README file, a file with information about your project. README files are written in the plain text Markdown language.
   - `.gitignore`: But sometimes you’ll find that there are a bunch of files that show up in the untracked section and that you want Git to just not see. That’s where the .gitignore file comes in.
4. [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
5. Make changes to a file and commit them.
   - `git status` – Make sure your current area is clean.
   - `git pull` – Get the latest version from the remote. This saves merging issues later.
   - Edit your files and make your changes.
   - `git status` – Find all files that are changed. Make sure to watch untracked files too!
   - `git add [files] `– Add the changed files to the staging area.
   - `git commit -m "message"` – Make your new commit.
6. [Pushing commits to a remote repository](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)

> Never put confidential information into a public repository on GitHub. Passwords, API keys, and similar items should not be committed to a repo. Someone will find them eventually.

[Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github): If your code is stored locally on your computer and is tracked by Git or not tracked by any version control system (VCS), you can import the code to GitHub using GitHub CLI or Git commands.

Clone the [Uvod v Python in razvojna okolja](https://github.com/icta-tecaji/uvod-v-python-in-razvojna-okolja) locally.

> You can use [organizations](https://docs.github.com/en/organizations) to collaborate with an unlimited number of people across many projects at once, while managing access to your data and customizing settings.