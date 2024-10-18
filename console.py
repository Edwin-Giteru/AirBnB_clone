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

    classes = ["BaseModel", "storage","User", "Place", 
               "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)."""
        return True

    def do_help(self, arg):
        """List available commands."""
        super().do_help(arg)

    def do_create(self, arg):
        """create a new instance of BaseModel and save it to the JSON file"""
        if not arg:
            print("** class name is missing **")

            return
        class_name = arg.strip()
        if class_name not in self.classes:
            print("** class doesn't exist **")

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)
     
    def do_show(self,arg):

        """Prints the string representation of an instance
            based on the class name and id"""
        if not arg:
            print("** class name is missing **")
            return
        args = arg.split()
        
        if len(args) < 2:
            print("** instance id is missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        complete_rep = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()

        if complete_rep in all_instances:
            print(all_instances[complete_rep])
        else:
            print("** no instance found **")
    def do_destroy(self,arg):

        """ Deletes an instance based on the class name and id
         and saves the changes into the JSON file"""
        if not arg:
            print("** class name is missing **")
            return
        full = arg.split()
        class_name = full[0]

        if class_name  not in self.classes:
            print("** class doesn't exist **")
            return

        instance_id = full[1]
        complete = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()

        if complete in all_instances:
            del all_instances[complete]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self,arg):
        """Prints all string representations"""
        all_instances = storage.all()
        if not arg:
            for instance in all_instances.values():
                print(instance)
        else:
            class_name = arg.strip()
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                legit_instances = {
                        key: value for key, value in all_instances.items()
                        if key.startswith(class_name + ".")
                        }
                for instance in legit_instances.values():
                    print(instance)

    def do_update(self, arg):
        """Updates an instance based on the class name"""
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

        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        if attribute_name in ['id', 'created_at', 'updated_at']:
            print("** cannot update id, created_at, or updated_at **")
            return

        instance = objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()
    
    def emptyline(self,arg):
        """ Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

