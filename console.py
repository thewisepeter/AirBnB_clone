#!/usr/bin/python3
"""
This module defines the HBNBCommand class, the command interpreter for the AirBnB clone project.
"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class defines the command interpreter for the AirBnB clone project.
    """
    prompt = '(hbnb) '
    valid_classes = ['BaseModel']

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

    def do_create(self, line):
        """
        Create a new instance of BaseModel, saves it (to the JSON file), and prints the id.
        Usage: create <class name>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        if key in instances:
            instance = instances[key]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all or all <class name>
        """
        args = line.split()
        instances = storage.all()

        if not args:
            print([str(instance) for instance in instances.values()])
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        print([str(instance) for instance in instances.values() if type(instance).__name__ == class_name])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        instances = storage.all()
        if key in instances:
            instance = instances[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
