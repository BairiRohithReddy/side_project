## Finalized Requirements

1. **Task Class**
   - Attributes:
     - Unique identifier (string)
     - Task title (string)
     - Task description (string)
     - Created date (date)
     - Created by (string)
     - Due date (date)
     - Priority (string)
     - Status (string, e.g., "Not Started", "In Progress", "Completed")

2. **Task Management**
   - Create a new task
   - Edit an existing task
   - Delete a task
   - Mark a task as complete
   - View all tasks
   - Filter tasks by priority or status
   - Sort tasks by due date or priority

3. **Priority Assignment**
   - Calculate days left until due date
   - Assign priority based on days left:
     - Critical: <= 3 days
     - High: <= 10 days
     - Medium: <= 20 days
     - Low: <= 30 days
     - No priority: > 30 days

4. **User Interface**
   - Display a menu with options:
     1. Add a new task     <!--implemented -->
     2. Edit an existing task
      - Display all the tasks
      - let the user pick the task to be edited 
      - modify the task and update the tasks.csv
     3. Delete a task
      - first display all the tasks
      - let the user choose the task id to be deleted
      - remove the task from the tasks.csv
     4. Mark a task as complete
      - first display all the tasks and then let the user specify the task id.
      - then modify the task status accordingly
     5. View all tasks    <!-- Implemented -->
     6. Filter tasks
      - tasks can be filtered based on their priority
     7. Sort tasks
      - tasks can be sorted based on the days left
     8. Exit <!-- implemented -->

5. **Data Persistence** <!-- implemented -->
   - Save tasks to a file (e.g., JSON or CSV)
   - Load tasks from file when the program starts

6. **Input Validation** <!-- implemented but needs to check again  -->
   - Validate user inputs for dates, priorities, and other fields

7. **Error Handling**
   - Implement proper error handling for invalid inputs or operations

8. **Task Display**
   - Show all existing tasks after each operation
   - Display "You are up to date. Please create a new task to track." if no tasks exist

9. **Search Functionality**
   - Allow users to search for tasks by title or description

10. **Reporting**
    - Generate a summary report of tasks by priority or status

11. **User Authentication**
    - Implement a simple user login system to track who created each task

12. **Due Date Notifications**
    - Alert users of upcoming or overdue tasks when they start the application

