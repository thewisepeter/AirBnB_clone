#!/usr/bin/python3
"""
This module defines the HBNBCommand class, the command interpreter for the AirBnB clone project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class defines the command interpreter for the AirBnB clone project.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Handles the end of file (EOF) condition to exit the program.
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
