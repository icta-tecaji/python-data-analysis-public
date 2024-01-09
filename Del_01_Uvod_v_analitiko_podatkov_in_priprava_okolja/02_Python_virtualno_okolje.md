# Python virtualno okolje

- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)

## Namestitev virtualnega okolja venv
Each environment can use different versions of package dependencies and Python.

[Python’s venv module](https://docs.python.org/3/library/venv.html) is part of Python’s standard library, and it’s the officially recommended way to create virtual environments since Python 3.5.

>  There are other great third-party tools for creating virtual environments, such as *conda* and *virtualenv*.

Any time you’re working on a Python project that uses external dependencies that you’re installing with pip, it’s best to first create a virtual environment:
- `python -m venv .venv`

Generally, before you start using it, you’ll first activate the environment by executing a script that comes with the installation:
- `.venv\Scripts\activate`

Once you can see the name of your virtual environment—in this case (.venv)—in your command prompt, then you know that your virtual environment is active.

After creating and activating your virtual environment, you can now install any external dependencies that you need for your project:
- `pip install requests`

Because you first created and activated the virtual environment, pip will install the packages in an isolated location.

Update the pip package manager inside the virtual environment:
- `python -m pip install --upgrade pip`

> Suppose you use the optional `--upgrade-deps `argument when creating your virtual environment. In that case, it’ll automatically poll PyPI for the newest versions of pip and setuptools and install them if the local wheel isn’t up-to-date. Try: `python -m venv .venv --upgrade-deps`

List all of the packages installed in the virtual environment:
- `pip list`

Once you’re done working with this virtual environment, you can deactivate it:
- `deactivate`

After executing the deactivate command, your command prompt returns to normal. This change means that you’ve exited your virtual environment. If you interact with Python or pip now, you’ll interact with your globally configured Python environment.

Check the list of packages installed:
- `pip list`

You can see there are no packages installed in the global environment.

If you want to go back into a virtual environment that you’ve created before, you again need to run the activate script of that virtual environment.

## Zakaj potrebujemo virtualno okolje?

The short answer is that **Python isn’t great at dependency management**. If you’re not specific, then pip will **place all the external packages that you install in a folder called `site-packages/`** in your base Python installation.

You can check the paths using sysconfig:
```python
>>> import sysconfig
>>> sysconfig.get_path("purelib")
'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages'
```

Several issues can come up if all of your external packages land in the same folder. 
1. **Avoid System Pollution**
    - (Linux) If you install packages to your operating system’s global Python, these packages will mix with the system-relevant packages. This mix-up could have unexpected side effects on tasks crucial to your operating system’s normal behavior.
2. **Sidestep Dependency Conflicts**
    - One of your projects might require a different version of an external library than another one. If you have only one place to install packages, then you can’t work with two different versions of the same library. This is one of the most common reasons for the recommendation to use a Python virtual environment.
    - If you install two different versions of the same package into your global Python environment, the second installation overwrites the first one.
    - Example:
        - `pip install flask==1.1.4`
        - `pip install flask==2.0.1`
        - `pip list`
        - `pip show flask`
        - Try to do the same with virtual environment
3. **Minimize Reproducibility Issues**
    - If all your packages live in one location, then it’ll be difficult to only pin dependencies that are relevant for a single project.
    - If you use a separate virtual environment for each of your projects, then it’ll be more straightforward to read the project requirements from your pinned dependencies. 
4. **Dodge Installation Privilege Lockouts**
    - In a corporate work environment, you most likely won’t have administrative level of access to the machine that you’re working on.
    - If you use virtual environments, then you create a new installation location within the scope of your user privileges, which allows you to install and work with external packages.

## Kaj je virtualno okolje?

**A Python virtual environment is a folder structure that gives you everything you need to run a lightweight yet isolated Python environment.**

When you create a new virtual environment using the venv module, Python creates a self-contained folder structure and copies or symlinks the Python executable files into that folder structure.

Check the `.venv` folder structure:
- `ls`
- `tree .venv`

A virtual environment folder contains a lot of files and folders, but you might notice that most of what makes this tree structure so long rests inside the site-packages/ folder. 

```
venv\
│
├── Include\
│
├── Lib\
│   │
│   └── site-packages\
│
├── Scripts\
│   ├── Activate.ps1
│   ├── activate
│   ├── activate.bat
│   ├── deactivate.bat
│   ├── pip.exe
│   ├── pip3.10.exe
│   ├── pip3.exe
│   ├── python.exe
│   └── pythonw.exe
│
└── pyvenv.cfg
```

From this bird’s-eye view of the contents of your virtual environment folder, you can zoom out even further to discover that there are three essential parts of a Python virtual environment:
- A copy or a symlink of the Python binary
- A pyvenv.cfg file
- A site-packages directory

To assure that the scripts you want to run use the Python interpreter within your virtual environment, venv modifies the `PYTHONPATH` environment variable that you can access using `sys.path`.

```python
>>> import sys
>>> from pprint import pp
>>> pp(sys.path)
```

Activate the virtual environment: `.venv\Scripts\activate` and try again.

Without an activated virtual environment, this directory is nested within the same folder structure as the Python executable.

## Uporaba in delovanje virtualnega okolja venv
You can change the folder name that contains your virtual environment when you create it by passing a name other than venv. In fact, you’ll often see different names in different projects. Some of them are commonly used:
- `venv`
- `env`
- `.venv`

If you want the convenience of seeing a different command prompt, but you want to keep the folder name descriptive so that you’ll know it contains a virtual environment, then you can pass your desired command prompt name to `--prompt`:
- `python -m venv .venv --prompt="dev-env"`

To delete a virtual environment, you can simply delete the folder that contains it. If you want to delete the virtual environment that you created in this tutorial, then you can run the following command:
- Deactivate the virtual environment: `deactivate`
- `rm .venv`
