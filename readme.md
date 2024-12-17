# **Task Tracker Documentation**

This documentation provides a comprehensive overview of the Task Tracker project, detailing its structure, functionality, and implementation. The Task Tracker is a command-line application designed to help users manage their tasks efficiently.

## Project Overview

The Task Tracker is a Python-based application that allows users to create, manage, and track tasks. It provides a range of features including task creation, editing, deletion, status updates, filtering, and sorting. The application uses a CSV file for data persistence and implements priority assignment based on due dates.

## Core Components

### TaskTracker Class

The `TaskTracker` class is the main component of the application. It handles the user interface, task management, and file operations.

Key features:
- Initialization with configuration settings
- Menu-driven interface
- Task management operations (add, edit, delete, update status)
- Task display and filtering
- Priority updates

### Priority Class

The `Priority` class is responsible for calculating and assigning task priorities based on due dates.

Key features:
- Calculates days left until the due date
- Assigns priority levels (OVERDUE, Critical, High, Medium, Low, No Priority)

## Functionality

### 1. Task Management

#### Adding a New Task
- Users can add new tasks with details such as title, description, due date, and author.
- A unique task ID is automatically generated using the `nanoid` library.
- The task is saved to a CSV file (`tasks.csv`).

#### Editing an Existing Task
- Displays all tasks and allows the user to select a task for editing.
- Updates the selected task in the CSV file.

#### Deleting a Task
- Shows all tasks and prompts the user to choose a task ID for deletion.
- Removes the selected task from the CSV file.

#### Marking a Task as Complete
- Displays all tasks and allows the user to specify a task ID to mark as complete.
- Updates the task status in the CSV file.

### 2. Task Display and Filtering

#### Viewing All Tasks
- Reads tasks from the CSV file and displays them in a tabular format using the `tabulate` library.

#### Filtering Tasks
- Allows filtering based on priority, status, creation date, title, or author.

#### Sorting Tasks
- Implements sorting functionality based on due date or priority.

### 3. Priority Assignment

- Automatically calculates and assigns priorities based on the due date.
- Updates priorities each time tasks are loaded or displayed.

### 4. User Interface

- Presents a menu-driven interface with options for various operations.
- Uses the `cowsay` library for greeting messages.

### 5. Data Persistence

- Utilizes a CSV file (`tasks.csv`) for storing task data.
- Implements reading from and writing to the CSV file.

### 6. Input Validation

- Validates user inputs for dates, task statuses, and menu selections.
- Provides error messages for invalid inputs.

### 7. Configuration

- Uses a `config.ini` file to store application settings.
- Includes author name, version, and default greeting message.

## Implementation Details

### Libraries Used

- `datetime`: For date handling and calculations
- `cowsay`: For displaying greeting messages
- `csv`: For reading and writing CSV files
- `os`: For file operations
- `nanoid`: For generating unique task IDs
- `pandas`: For data manipulation
- `tabulate`: For formatting task displays
- `configparser`: For reading configuration files

### File Structure

- `TaskTracker.py`: Main application file
- `priority.py`: Contains the Priority class
- `config.ini`: Configuration file
- `tasks.csv`: Data storage file

### Key Methods

- `__init__`: Initializes the TaskTracker with configuration settings
- `menu`: Displays the main menu and handles user input
- `add_tasks`: Adds a new task to the system
- `edit_tasks`: Allows editing of existing tasks
- `delete_task`: Removes a task from the system
- `task_status`: Updates the status of a task
- `display_tasks`: Shows all tasks in a tabular format
- `filter_tasks`: Implements task filtering functionality
- `sort_tasks`: Implements task sorting functionality
- `update_priorities`: Updates task priorities based on current date

## Future Enhancements

1. Implement search functionality for tasks by title or description
2. Add a reporting feature to generate summaries by priority or status
3. Implement user authentication for tracking task creators
4. Add due date notifications for upcoming or overdue tasks
5. Enhance error handling and input validation
6. Implement unit tests for core functionalities
7. Consider migrating to a database for improved data management

## tl-dr

The Task Tracker project provides a robust foundation for task management with features like priority assignment, data persistence, and a user-friendly interface. Its modular design allows for easy expansion and enhancement, making it a versatile tool for personal or small team task tracking.
