#!/usr/bin/python3
"""
This file defines the console class which will
serve as the entry point of the entire project
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB Command Interpreter

    This class implements a command-line interpreter for the 
    HBNB (AirBnB Clone) project. It allows users to interact 
    with the application through a command prompt.
    """

    prompt = '(hbnb) '  # Define the custom prompt displayed in the command line

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
