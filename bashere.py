#!/usr/bin/env python
# -*- coding: utf-8 -*-


r"""
bashere opens the Windows directories on WSL (Windows Subsystem for Linux).
"""

import os
import sys


def get_bash_path():
    r"""
    Returns the path of bash.exe.

    Note that is is tricky, see the comment below from Peter Jones:

    https://notepad-plus-plus.org/community/topic/15776/windows-10-subsystem-bash-exe-not-found

    My idea is that you’re using 32b NPP in 64b windows, so you’re getting the
    system32 vs syswow64 windows-lies-to-you
    (excuse me, File System Redirector).

    If you are in 32b NPP (? > Debug Info will say Notepad++ v7.5.6 (32-bit)),
    then try running c:\windows\sysnative\bash.exe ... instead.

    If that’s not it, please supply the Debug Info, along with other
    information that might be relevant to help us debug your problem.
    """
    # TODO: 4 better detection for bash.exe path.
    # process_path = "C:\\Windows\\System32\\bash.exe"
    # process_path = "%WINDIR%\\System32\\bash.exe"
    process_path = "c:\\windows\\sysnative\\bash.exe"
    return process_path


def open_bash_in(dir_name):
    """
    Opens bash in the corresponding directory.
    """
    dir_before = os.getcwd()
    os.chdir(dir_name)
    process_path = get_bash_path()
    os.system(process_path)
    os.chdir(dir_before)


def get_item_path(item):
    """
    Returns the directory name of the item.
    If the item is an existing directory, it will be returned as it is.
    If the item is an existing file, its directory will be returned.
    Otherwise, None will be returned.
    :param item: a file or folder.
    :type item: str
    """
    result = None
    if os.path.isdir(item):
        result = item
    elif os.path.isfile(item):
        result = os.path.split(item)[0]
    return result


def main():
    """
    entry point of the module.
    """
    # TODO: 5 check whether help wanted?

    # TODO: 5 what to do if there are more than 1 param?
    item = sys.argv[1]
    item_path = get_item_path(item)
    if item_path:
        open_bash_in(item_path)
    else:
        # TODO: 5 show some help here.
        pass


if __name__ == '__main__':
    main()
