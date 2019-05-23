# bashere

bashere opens the Windows directories on WSL (Windows Subsystem for Linux).


# Installation

Simply, extract to a folder of your choice, it is fully portable.
An installer with InnoSetup is yet to come.


# Requirements

## Runtime Requirements

- Windows 10, since WSL works on Windows 10.
- WSL must be [installed](Windows Subsystem for Linux).
- no Python is required for bashere itself since it is packed to a Windows .exe file with [PyInstaller](https://www.pyinstaller.org/).


## Development Requirements

- [Python 3](https://www.python.org/)
- `pip install pyinstaller` to bundle the package to an Windows .exe file.
- `pip install pylint` to check the code for pitfalls, optional.
- `pip install pycodestyle` to check the code style, optional.


# Configuration

None, currently.


# Usage

- You can create a shortcut to bashere.exe on your desktop, and drag-and-drop directories.
- You can add bashere.exe to Windows 10 `SendTo` menu.


# FAQ

## Do I need yo install WSL?

Yes, you need to install a Linux distribution from Windows store.
This package has been tested with Ubuntu.

## Does bashere works with git-bash?

Not yet, but there are plans to implement it.


## I have seen `make*.bat` files in the source code. Do I need to install GNU `make`?

No, those files includes Windows specific batch commands.
Only Windows is required to execute them.
`make*` names have been used since it makes sense.


# License

Licensed with 2-clause license ("Simplified BSD License" or "FreeBSD License").
See the [LICENSE.txt](LICENSE.txt) file.


# Legal

All trademarks and registered trademarks are the property of their respective owners.
