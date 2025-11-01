# Install Python3, PIP and VEnv

## 1 - Check if Python 3 is installed

```bash
python3 --version
```

_If you see something like 3.10.x, you are good to go. Otherwise, install it manually (next step)._

## 2 - Install Python 3, PIP and VEnv

Install the following packages:
- Python3: main interpreter.
- PIP: stands for Pip Installs Packages. It's a Python package manager.
- VEnv: Virtual Environment. Creates virtual environments in such way that dependencies do solely apply only to the virtual environment but not the global one.

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

## 3 - Verify the installation

Just check that everything works smoothly.

```bash
python3 --version
python3 -m pip --version
```

_The parameter used alongside python3 command stands for "module"._

## 4 - Set up a virtual environment

This step is not mandatory but still strongly recommended since it isolates workspaces.

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
```

Where:
- *_python3 -m venv venv_*: runs the python3 interpreter, tells *venv* module to create a virtual environment named _venv_. In other words, it creates a sanbox where packages can be locally installed without affecting other projects nor your system's Python installation.
- *_source venv/bin/activate_*: runs _source_ shell command so that _venv/bin/activate_ script is executed. This way, $PATH is updated so that running Python or PIP now points to the ones inside _venv/_, not the system wide ones.
- *_pip install --upgrade pip_*: update pip inside the environment to the latest version. Additionally, it installs _setuptools_ (helps build and install Python packages that include setup.py) and _wheel_ (a binary format for faster installs).

Deactivate anytime with:

```bash
deactivate
```

## 5 - Install development essentials

Again, this step is optional but highly recommended.

```bash
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

## 6 - Developer tools

These are core engineering tools. They provide some help with formatting, linting, type checking and tests.

```bash
pip install black pylint mypy pytest
```

## 7 - Check environment packages list

Retrieve the lkist of packages managed by PIP in the local virtual environment.

```bash
pip list
```

_Optional, same tha latest commands above._
