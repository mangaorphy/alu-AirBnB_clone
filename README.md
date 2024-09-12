# AirBnB Clone: Command Interpreter

## Project Overview

Welcome to the AirBnB clone project! This project aims to create a command interpreter to manage AirBnB objects, serving as the foundation for a fully functional web application. 

## Command Interpreter

The command interpreter allows you to perform various operations on AirBnB objects, such as creating, retrieving, updating, and destroying them. The interpreter will work in both interactive and non-interactive modes.

### Starting the Interpreter

To start the command interpreter, run the following command in your terminal:

```bash
$ ./console.py
```

### Using the Interpreter

Once the interpreter is running, you can enter commands. Here are a few examples:

- **Help Command**: Shows available commands.
  ```bash
  (hbnb) help
  ```
  
- **Quit Command**: Exits the interpreter.
  ```bash
  (hbnb) quit
  ```

### Non-Interactive Mode

You can also run commands in non-interactive mode by echoing commands or piping input:

```bash
$ echo "help" | ./console.py
```

## File Structure

- `console.py`: The main command interpreter file.
- `models/`: Contains the various model classes (e.g., User, State, City, Place).
- `tests/`: Contains unit tests for the project.
- `README.md`: Project description and usage instructions.
- `AUTHORS`: List of contributors to the project.

## Getting Started

### Requirements

- Python 3.8.5
- The `cmd` and `unittest` modules for command handling and testing.

### Documentation

All modules, classes, and functions will include documentation to explain their purpose and usage.

## Authors

- Charlotte Kariza
- Orpheus Mhizha Manga

---
