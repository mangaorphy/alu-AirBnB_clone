#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB Command Interpreter"""
    
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True  # Returning True exits the command loop

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True  # Returning True exits the command loop

    def emptyline(self):
        """Do nothing on empty input line"""
        pass  # Override to prevent executing the last command

    def do_help(self, arg):
        """Prints help for commands"""
        super().do_help(arg)  # Call the default help functionality

if __name__ == '__main__':
    HBNBCommand().cmdloop()