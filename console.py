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

    def emptyline(self):
        """
        Handles the case when an empty line is entered.
        It does nothing instead of repeating the last command.
        """
        pass

    def precmd(self, line):
        """
        This method is called just before the command line is interpreted,
        allowing preprocessing of the command.

        Args:
            line (str): The command line string.

        Returns:
            str: The modified command line string.
        """
        return line.strip()

    def postcmd(self, stop, line):
        """
        This method is called just after a command has been executed or
        an error has occurred.

        Args:
            stop (bool): If True, the command loop will exit.
            line (str): The command line string.

        Returns:
            bool: If True, the command loop will exit.
        """
        return stop

    def cmdloop(self):
        """
        Enters the command loop, which repeatedly prompts for commands and
        executes them until the quit command is entered or EOF is reached.
        """
        self.preloop()
        while True:
            try:
                line = input(self.prompt)
                if not line:
                    continue
                stop = self.onecmd(line)
                if stop:
                    break
            except EOFError:
                print()
                break
            except KeyboardInterrupt:
                print("^C")
                continue
        self.postloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
