#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBNB Command Interpreter

    This class implements a command-line interpreter for the 
    HBNB (AirBnB Clone) project. It allows users to interact 
    with the application through a command prompt.
    """

    prompt = '(hbnb) '  # Define the custom prompt displayed in the command line

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id.

        Usage: create <class name>

        If the class name is missing, prints ** class name missing **.
        If the class name doesn’t exist, prints ** class doesn't exist **.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance = models.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id.

        Usage: show <class name> <id>

        If the class name is missing, prints ** class name missing **.
        If the class name doesn’t exist, prints ** class doesn't exist **.
        If the id is missing, prints ** instance id missing **.
        If the instance of the class name doesn’t exist for the id, prints ** no instance found **.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = models.storage.all().get(key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file).

        Usage: destroy <class name> <id>

        If the class name is missing, prints ** class name missing **.
        If the class name doesn’t exist, prints ** class doesn't exist **.
        If the id is missing, prints ** instance id missing **.
        If the instance of the class name doesn’t exist for the id, prints ** no instance found **.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name.

        Usage: all [<class name>]

        If the class name doesn’t exist, prints ** class doesn't exist **.
        """
        if arg:
            class_name = arg
            if class_name not in models.classes:
                print("** class doesn't exist **")
                return

            instances = [str(instance) for key, instance in models.storage.all().items() if key.startswith(f"{class_name}.")]
        else:
            instances = [str(instance) for instance in models.storage.all().values()]

        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        If the class name is missing, prints ** class name missing **.
        If the class name doesn’t exist, prints ** class doesn't exist **.
        If the id is missing, prints ** instance id missing **.
        If the instance of the class name doesn’t exist for the id, prints ** no instance found **.
        If the attribute name is missing, prints ** attribute name missing **.
        If the value for the attribute name doesn’t exist, prints ** value missing **.
        """
        args = arg.split(maxsplit=3)
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = models.storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3].strip('"')
        if attribute_name not in instance.__dict__:
            print("** attribute name missing **")
            return

        # Casting attribute value to its appropriate type
        if isinstance(getattr(instance, attribute_name), int):
            attribute_value = int(attribute_value)
        elif isinstance(getattr(instance, attribute_name), float):
            attribute_value = float(attribute_value)

        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_quit(self, arg):
        """Quit command to exit the program.

        Usage: quit

        This command exits the command interpreter.
        """
        return True  # Returning True exits the command loop

    def do_EOF(self, arg):
        """EOF command to exit the program.

        Usage: EOF

        This command exits the command interpreter when the 
        end-of-file (EOF) signal is received (e.g., Ctrl+D).
        """
        return True  # Returning True exits the command loop

    def emptyline(self):
        """Do nothing on empty input line.

        This method overrides the default behavior of executing 
        the last command when the user enters an empty line. 
        By implementing it with pass, it ensures that nothing 
        happens on an empty input line.
        """
        pass  # Override to prevent executing the last command

    def do_help(self, arg):
        """Prints help for commands.

        Usage: help [command]

        This command prints help information for available commands. 
        If a specific command is provided, it shows the help for that 
        command.
        """
        super().do_help(arg)  # Call the default help functionality

if __name__ == '__main__':
    """Main entry point for the command interpreter.

    This block ensures that the command interpreter runs only when 
    the script is executed directly, not when it is imported as a module.
    """
    HBNBCommand().cmdloop()  # Start the command loop for user interaction
