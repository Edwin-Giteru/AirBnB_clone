AirBnB Clone - The Console

Description
The AirBnB Clone project is a comprehensive series that takes you step by step through the development of a web application similar to AirBnB. This first part revolves around the command-line interpreter, a shell-like environment that lets you create, retrieve, update, and delete objects in the system. It is the foundation for the future aspects of the project, which will include:

Building classes that handle AirBnB objects (e.g., User, City, Place)
File storage management for serializing and deserializing object data
Interfacing with a database, creating APIs, and front-end development

Command Interpreter
The command interpreter works similarly to a Unix shell. It allows you to manage AirBnB objects through various commands. This interpreter will be used in future projects to handle file storage, databases, APIs, etc.

How to Start
To start the command interpreter, you simply need to run the following command in your terminal:

    $ ./console.py
How to Use
Once the interpreter starts, you will see a prompt that looks like this:

(hbnb)
You can now enter commands to interact with your objects.

Commands:
help : List all available commands
quit : Exit the command interpreter
EOF (Ctrl+D): Exit the command interpreter

GitHub Workflow
Branches and Pull Requests
To ensure efficient collaboration in your team, follow these GitHub practices:

Branching:

Each feature or bug fix should be developed in its own branch.
Follow a branch naming convention, such as feature/feature-name or fix/issue-description.
Pull Requests:

Once a feature is complete, submit a pull request (PR) to merge your changes back into the main branch.
Ensure that the code passes all tests and Pycodestyle checks before submitting the PR.
Review and approve each PR before merging.

Unit Testing and Code Style
All files, classes, and functions are thoroughly tested using Python’s unittest module.

Ensure your code passes Pycodestyle checks for clean and readable code. You can run the check using:


