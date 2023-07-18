#!/usr/bin/python3
"""
This module contains the unittests for console.py
"""
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for HBNBCommand class
    """

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_help_quit(self):
        expected_output = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_show(self):
        expected_output = "Usage: show <class> <id> or <class>.show(<id>)\n" \
            "        Display the string representation of a class instance of a given id."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_all(self):
        expected_output = "Usage: all or all <class> or <class>.all()\n" \
            "        Display string representations of all instances of a given class.\n" \
            "        If no class is specified, displays all instantiated objects."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_count(self):
        expected_output = "Usage: count <class> or <class>.count()\n" \
                "        Retrieve the number of instances of a given class."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_create(self):
        expected_output = "Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...\n" \
                "        Create a new class instance with given keys/values and print its id."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_destroy(self):
        expected_output = "Usage: destroy <class> <id> or <class>.destroy(<id>)\n" \
                "        Delete a class instance of a given id."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_update(self):
        expected_output = "Usage: update <class> <id> <attribute_name> <attribute_value> or\n" \
                "       <class>.update(<id>, <attribute_name>, <attribute_value>) or\n" \
                "       <class>.update(<id>, <dictionary>)\n" \
                "        Update a class instance of a given id by adding or updating\n" \
                "        a given attribute key/value pair or dictionary."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_EOF(self):
        expected_output = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_help_help(self):
        expected_output = "List available commands with \"help\" or detailed help with \"help cmd\"."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_quit(self):
        """
        Test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """
        Test EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            self.assertEqual(f.getvalue(), "\n")

    def test_emptyline(self):
        """
        Test emptyline command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(HBNBCommand().onecmd(""))
            self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """
        Test help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertNotEqual(f.getvalue(), "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertNotEqual(f.getvalue(), "")

    def test_create(self):
        """
        Test create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertNotEqual(f.getvalue(), "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertNotEqual(f.getvalue(), "")

    def test_show(self):
        """
        Test show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 12345"))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_destroy(self):
        """
        Test destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 12345"))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_all(self):
        """
        Test all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertNotEqual(f.getvalue(), "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertNotEqual(f.getvalue(), "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertNotEqual(f.getvalue(), "")

    def test_count(self):
        """
        Test count command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count BaseModel"))
            self.assertNotEqual(f.getvalue(), "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count User"))
            self.assertNotEqual(f.getvalue(), "")

    def test_update(self):
        """
        Test update command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 12345"))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_default(self):
        """
        Test default behavior
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("invalid_command"))
            self.assertEqual(f.getvalue(),
                             "*** Unknown syntax: invalid_command\n")
    
    def test_all_base_model(self):
        # Create a few instances of BaseModel
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all BaseModel")
            output_str = output.getvalue().strip()
            self.assertIn(instance1.__str__(), output_str)
            self.assertIn(instance2.__str__(), output_str)
            self.assertIn(instance3.__str__(), output_str)
    
    def test_all_user(self):
        # Create a few instances of User
        instance1 = User()
        instance2 = User()
        instance3 = User()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all User")
            output_str = output.getvalue().strip()
            self.assertIn(instance1.__str__(), output_str)
            self.assertIn(instance2.__str__(), output_str)
            self.assertIn(instance3.__str__(), output_str)

    def test_all_with_updated_instance(self):
        # Create an instance of BaseModel
        instance = BaseModel()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all BaseModel")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)

        # Update the instance
        instance.name = "Updated Instance"

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all BaseModel")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)
    
    def test_all_review(self):
        # Create a few instances of Review
        instance1 = Review()
        instance2 = Review()
        instance3 = Review()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all Review")
            output_str = output.getvalue().strip()
            self.assertIn(instance1.__str__(), output_str)
            self.assertIn(instance2.__str__(), output_str)
            self.assertIn(instance3.__str__(), output_str)

    def test_all_with_updated_instance(self):
        # Create an instance of Review
        instance = Review()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all Review")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)

        # Update the instance
        instance.text = "Updated Review"

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all Review")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)

    def test_all_state(self):
        # Create a few instances of State
        instance1 = State()
        instance2 = State()
        instance3 = State()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all State")
            output_str = output.getvalue().strip()
            self.assertIn(instance1.__str__(), output_str)
            self.assertIn(instance2.__str__(), output_str)
            self.assertIn(instance3.__str__(), output_str)

    def test_all_with_updated_instance(self):
        # Create an instance of State
        instance = State()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all State")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)

        # Update the instance
        instance.name = "Updated State"

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all State")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)

    def test_all_city(self):
        # Create a few instances of City
        instance1 = City()
        instance2 = City()
        instance3 = City()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all City")
            output_str = output.getvalue().strip()
            self.assertIn(instance1.__str__(), output_str)
            self.assertIn(instance2.__str__(), output_str)
            self.assertIn(instance3.__str__(), output_str)

    def test_all_with_updated_instance(self):
        # Create an instance of City
        instance = City()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all City")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)

        # Update the instance
        instance.name = "Updated City"

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all City")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)
    
    def test_all_amenity(self):
        # Create a few instances of Amenity
        instance1 = Amenity()
        instance2 = Amenity()
        instance3 = Amenity()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all Amenity")
            output_str = output.getvalue().strip()
            self.assertIn(instance1.__str__(), output_str)
            self.assertIn(instance2.__str__(), output_str)
            self.assertIn(instance3.__str__(), output_str)

    def test_all_with_updated_instance(self):
        # Create an instance of Amenity
        instance = Amenity()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all Amenity")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)

        # Update the instance
        instance.name = "Updated Amenity"

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all Amenity")
            output_str = output.getvalue().strip()
            self.assertIn(instance.__str__(), output_str)

    def test_all_place(self):
        # Create a few instances of Place
        instance1 = Place()
        instance2 = Place()
        instance3 = Place()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all Place")
            output_str = output.getvalue().strip()
            self.assertIn(instance1.__str__(), output_str)
            self.assertIn(instance2.__str__(), output_str)
            self.assertIn(instance3.__str__(), output_str)




if __name__ == "__main__":
    unittest.main()
