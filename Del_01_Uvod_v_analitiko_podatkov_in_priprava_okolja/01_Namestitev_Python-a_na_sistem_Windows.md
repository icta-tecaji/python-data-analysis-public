# Namestitev Python-a na sistem Windows

## Predstavitev namestitvenih opcij
- [Using Python on Windows](https://docs.python.org/3/using/windows.html)
- [Your Python Coding Environment on Windows: Setup Guide](https://realpython.com/python-coding-setup-windows/#setting-up-core-python-coding-software-in-windows)

Unlike most Unix systems and services, **Windows does not include a system supported installation of Python**.

Python 3.11 supports Windows 8.1 and newer. If you require Windows 7 support, please install Python 3.8.

There are a number of different installers available for Windows, each with certain benefits and downsides:
- The **full installer** contains all components and is the best option for developers using Python for any kind of project.
- The **Microsoft Store package** is a simple installation of Python that is suitable for running scripts and packages, and using IDLE or other development environments. It requires Windows 10 and above, but can be safely installed without corrupting other programs. It also provides many convenient commands for launching Python and its tools
- The **nuget.org packages**
- The **embeddable package**

## Uvod v terminal
- [Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)

Windows has two command-line shells: the **Command shell** and **PowerShell**. Each shell is a software program that provides direct communication between you and the operating system or application, providing an environment to automate IT operations.
- The **Command shell** was the first shell built into Windows to automate routine tasks, like user account management or nightly backups, with batch (.bat) files. With Windows Script Host, you could run more sophisticated scripts in the Command shell.
- **PowerShell** was designed to extend the capabilities of the Command shell to run PowerShell commands called cmdlets. Cmdlets are similar to Windows Commands but provide a more extensible scripting language. You can run both Windows Commands and PowerShell cmdlets in PowerShell, but the Command shell can only run Windows Commands and not PowerShell cmdlets.

Windows has created a new, open-source **Windows Terminal** to be a universal console host. It acts as an interface to multiple shells, allowing you to start the Command Prompt, PowerShell, and any other shell that you might have available as different tabs in the same host:

The Windows Terminal is a modern, fast, efficient, powerful, and productive terminal application for users of command-line tools and shells like Command Prompt, PowerShell, and WSL. Its main features include multiple tabs, panes, Unicode and UTF-8 character support, a GPU accelerated text rendering engine, and custom themes, styles, and configurations.
- Download the Windows Terminal from the [Microsoft Store](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701)

Installing it from the Microsoft Store has a few advantages. One advantage is that it ensures that updates come automatically. Another advantage is that it’s painless to install. 

## Konfuguacija sistema Windows

### App Execution Aliases
App execution aliases are a special kind of alias for Windows. For example, if you type python on the command line, Windows will automatically ask you if you want to install the Microsoft Store version of Python.

App execution aliases are a feature to make things easier to get started, but they can interfere with other programs. For instance, when you install pyenv for Windows and install a few Python versions, the app execution aliases will interfere by not allowing you to access those Python versions.

You can search for the app execution alias control panel from the Start menu. The entry is called *Manage app execution aliases*.

![App execution aliases](./images/img03.png)

You can usually turn all of these off, as you already have the Path environment variable to make sure apps are available on the command line.

### Windows Explorer
In an attempt to make Windows Explorer easier to use for non-developer types, it hides some information that you’ll probably want to see, so you should enable the following:
- Show file extensions
- Show hidden files
- Show protected operating system files
- Show the full path in the title bar

You can access these options from the file explorer, which you can open with `Win+E`, click on the File tab in the top left, and choose* Change folder and search options*. Under the View tab, you’ll be able to find these settings.

![Windows Explorer](./images/img04.png)

### Loosening Your Execution Policy
First open up Windows Terminal as an administrator.

> Note: To launch programs as an administrator, you can search for the app in the Start menu, and then right-click on it, and choose Run as administrator.

Once you have an administrator terminal session open, you should be presented with a PowerShell tab.

The execution policy sets how strict your system is about running scripts from other sources. For this tutorial, you’ll want to set it to `RemoteSigned`:
- `Set-ExecutionPolicy RemoteSigned`

You may not see the warning, because the execution policy might already be set. To double-check your setting, you can run `Get-ExecutionPolicy`.

> Without administrator privileges: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Namestitev najnovejše verzije Pythona

Four Python 3.11 installers are available for download - two each for the 32-bit and 64-bit versions of the interpreter.

Download the installer from the [official Python download page](https://www.python.org/downloads/).

After starting the installer, one of two options may be selected:

![Python installer](https://docs.python.org/3/_images/win_installer.png)

- If you select **Install Now**:
    - You will not need to be an administrator (unless a system update for the C Runtime Library is required or you install the Python Launcher for Windows for all users)
    - Python will be installed into your user directory
    - The Python Launcher for Windows will be installed according to the option at the bottom of the first page
    - The standard library, test suite, launcher and pip will be installed
    - If selected, the install directory will be added to your PATH
    - Shortcuts will only be visible for the current user
- Selecting **Customize installation** will allow you to select the features to install, the installation location and other options or post-install actions.

Python is installed in the directory `C:\Users\<username>\AppData\Local\Programs\Python\Python<version>`, where `<username>` is the name of the logged-in user and `<version>` is the installed version, for example `Python38`.

> **Removing the MAX_PATH Limitation**: Windows historically has limited path lengths to 260 characters. This meant that paths longer than this would not resolve and errors would result. In the latest versions of Windows, this limitation can be expanded to approximately 32,000 characters. Your administrator will need to activate the “Enable Win32 long paths” group policy, or set LongPathsEnabled to 1 in the registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`.

Python has been installed. You can start Python by typing `python` in the command prompt (`cmd.exe`) or by clicking on the Python icon in the Start Menu.

> To run Python conveniently from a command prompt, you might consider changing some default environment variables in Windows. While the installer provides an option to configure the PATH and PATHEXT variables for you, this is only reliable for a single, system-wide installation.

## Namestitev več hkratnih verziji Pythona
**Install another version of Python** while retaining the old version. This will allow you to switch between the versions from the command line.

**Environment variables are general-purpose key-value pairs** that are available at many levels of the operating system. They typically contain information about how to run programs, or where to find resources. Python, for instance, runs differently if certain environment variables are set or not.

One of the environment variables you should become familiar with is the **Path environment variable.** Path is a variable that contains a list of paths to directories that contain executables. Path is kept by your system as a way to have programs always close at hand.

You can see the Path environment variable in action whenever you call choco or python from the command line, for instance. You know that the target executable may not be in the current working directory, but Windows can still start it.

To see what paths are in your Path variable, from PowerShell you can call the following command: `(cat ENV:Path) -Split ";"`

> Note: Watch out for having multiple possible choices for any given executable in Path. If, for example, you had a python.exe in two different places in Path, the one to run will always be the first one.

To permanently modify the default environment variables: 
1. Click Start and search for *edit environment variables*, or open System properties, Advanced system settings and click the Environment Variables button. 
2. In this dialog, you can add or modify User and System variables. 
3. To change System variables, you need non-restricted access to your machine (i.e. Administrator rights).
4. Add the Python directory to the `PATH` variable and click OK.
    - `C:\Users\<username>\AppData\Local\Programs\Python\Python<version>`
    - `C:\Users\<username>\AppData\Local\Programs\Python\Python<version>\Scripts\`
    - Sort the entries from the newest to the oldest version.

![Pytohn Environment Variables](./images/img01.png)

> Windows will concatenate User variables after System variables, which may cause unexpected results when modifying PATH.

Open a new terminal and verify the installation was successful by typing `python --version` and `pip --version`. 

To access another Python version use: `python310 --version`.

## Python Launcher for Windows
- [Python Launcher for Windows](https://docs.python.org/3/using/windows.html#python-launcher-for-windows)

The Python launcher for Windows is a utility which aids in locating and executing of different Python versions. It allows scripts (or the command-line) to indicate a preference for a specific Python version, and will locate and execute that version.

Unlike the PATH variable, the launcher will correctly select the most appropriate version of Python. It will prefer per-user installations over system-wide ones, and orders by language version rather than using the most recently installed version.

The launcher is compatible with all available versions of Python, so it does not matter which version is installed. To check that the launcher is available, execute the following command in Command Prompt: 
-  `py`: You should find that the latest version of Python you have installed is started.
- The command displays the currently installed version(s) of Python: `py --list`
- If you have multiple versions of Python installed (e.g., 3.10 and 3.11) you will have noticed that Python 3.11 was started - to launch Python 3.10, try the command: `py -3.10`

## Pyenv za Windows
- [pyenv for Windows](https://github.com/pyenv-win/pyenv-win)

pyenv is a simple python version management tool. It lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.
1. Install pyenv-win in PowerShell: `Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"`
2. Reopen PowerShell
3. Run `pyenv --version` to check if the installation was successful.

Common commands:
- List all Python versions available to pyenv: `pyenv versions`
- Update the local index of Python versions available for install: `pyenv update`.
- Run `pyenv install -l` to check a list of Python versions supported by pyenv-win.
- Install a Python version: `pyenv install <version>`
> Installed versions are saved to: `C:\Users\<user>\.pyenv\pyenv-win\versions`
- Run `pyenv global <version>` to set a Python version as the global version.
- Check which Python version you are using and its path: `pyenv version`
- Test the Python version: `python --version`

Set a version for a specific project:
1. Create a new folder for your project: `mkdir <project>`
2. Navigate to the project folder: `cd <project>`
3. Set a Python version for the project: `pyenv local <version>`
    - Check the Python version: `pyenv version`
    - A `.python-version` file will be created in the project folder. This file contains the Python version that will be used when you navigate to the project folder.
4. Test the Python version: `python --version`

How to update pyenv. Run the following in a Powershell terminal: `&"${env:PYENV_HOME}\install-pyenv-win.ps1"`

## Uvod v Python shell
- [The Interpreter, an Interactive Shell](https://python-course.eu/python-tutorial/interpreter-interactive-shell.php)
- [Interacting With Python](https://realpython.com/interacting-with-python/)

To start the Python shell, open the Command Prompt and run `python` or `py`. You should see the Python shell open with the version number printed to the screen.

When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs (>>>); for continuation lines it prompts with the secondary prompt, by default three dots (...). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt:

![Shell](./images/img02.png)

Now you can type Python commands into the shell. A simple command like `print("Hello World!")` will print the text `Hello World!` to the screen.


When you work interactively, every expression and statement you type in is **evaluated and executed immediately**.

An interactive session will allow you to test every piece of code you write, which makes it an awesome development tool and an excellent place to experiment with the language and test Python code on the fly.

> Note: The first rule of thumb to remember when using Python is that if you’re in doubt about what a piece of Python code does, then launch an interactive session and try it out to see what happens.

Typing an end-of-file character (Control-D on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.

## Osnovni zagon Python skript
- [How to Run Your Python Scripts](https://realpython.com/run-python-scripts/)

A Python interactive session will allow you to write a lot of lines of code, but once you close the session, you lose everything you’ve written. That’s why the usual way of writing Python programs is by using plain text files. By convention, those files will use the `.py` extension. 

A plain text file containing Python code that is intended to be directly executed by the user is usually called **script**, which is an informal term that means top-level program file.

Save the file in your working directory with the name `hello.py`. With the test script ready, you can continue reading.

The most basic and easy way to run a Python script is by using the python command. You need to open a command line and type the word python followed by the path to your script file like this: `python hello.py` Hello World! Then you hit the ENTER button from the keyboard, and that's it. On the other hand, a plain text file, which contains Python code that is designed to be imported and used from another Python file, is called **module**.

So, the main difference between a module and a script is that **modules are meant to be imported**, while **scripts are made to be directly executed**.

## Odstranitev stare verzije Pythona
Once Python has been installed, you can add or remove features through the Programs and Features tool that is part of Windows. Select the Python entry and choose “Uninstall/Change” to open the installer in maintenance mode.

**Uninstall** will remove Python entirely, with the exception of the Python Launcher for Windows, which has its own entry in Programs and Features.

Remove the PATH entry for the Python version you are removing.
 
## Zagon Python skript iz Visual Studio Code
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
