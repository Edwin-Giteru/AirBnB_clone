#!/usr/bin/python3
"""
This module defines the command interpreter for the AirBnB clone project.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter for AirBnB clone."""
    prompt = '(hbnb) '

    classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)."""
        return True

    def do_create(self, arg):
        """create a new instance of BaseModel and save it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.strip()
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()  # Dynamically create an instance
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()

        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id and saves the changes into the JSON file."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()

        if key in all_instances:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name."""
        all_instances = storage.all()
        result = []
        
        if not arg:
            for instance in all_instances.values():
                class_name = instance.__class__.__name__
                instance_id = instance.id
                result.append("[{}] ({}) {}".format(class_name, instance_id, instance.__dict__))
        else:
            class_name = arg.strip()
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                for key, instance in all_instances.items():
                    if key.startswith(class_name):
                        instance_id = instance.id
                        result.append("[{}] ({}) {}".format(class_name, instance_id, instance.__dict__))
        
        print(result)

    def default(self, line):
        """
        This method is called when an unrecognized command is entered.
        It will handle commands in the format: <class name>.all()
        """
        if '.' in line:
            try:
                # Split the command into <class name> and <method>
                class_name, method = line.split('.', 1)
                method = method.strip("()")

                if class_name in self.classes and method == "all":
                    self.do_all(class_name)
                else:
                    print("** invalid syntax **")
            except ValueError:
                print("** invalid syntax **")
        else:
            print("** unknown command: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()

