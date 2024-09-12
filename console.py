#!/usr/bin/python3
"""
This file defines the console class which will
serve as the entry point of the entire project
"""

import cmd
from models.base_model import BaseModel
from models.engine import storage

class HBNBCommand(cmd.Cmd):
    """HBNB Command Interpreter

    This class implements a command-line interpreter for the 
    HBNB (AirBnB Clone) project. It allows users to interact 
    with the application through a command prompt.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_help(self, arg):
        """Prints help for commands."""
        super().do_help(arg)

    def do_create(self, class_name):
        """Creates a new instance of BaseModel, saves it, and prints the id.

        Usage: create <class name>
        """
        if not class_name:
            print("** class name missing **")
            return
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance.

        Usage: show <class name> <id>
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().pop(key, None)
        if instance is None:
            print("** no instance found **")
        else:
            storage.save()  # Save changes to the JSON file

    def do_all(self, class_name=""):
        """Prints string representation of all instances.

        Usage: all or all <class name>
        """
        if class_name and class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        instances = storage.all()
        if class_name:
            instances = {k: v for k, v in instances.items() if k.startswith(class_name)}

        print([str(instance) for instance in instances.values()])

    def do_update(self, args):
        """Updates an instance based on the class name and id.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        
        attribute_value = " ".join(args[3:]).strip('"')  # Handle quoted strings
        
        # Update the instance attribute
        if attribute_name in ["name", "email"]:  # Assuming these are valid attributes
            setattr(instance, attribute_name, attribute_value)
            instance.save()  # Save changes to the JSON file

if __name__ == '__main__':
    """Main entry point for the command interpreter."""
    HBNBCommand().cmdloop()