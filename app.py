import datetime
import cowsay # type: ignore
import csv
from priority import Priority
import os
import nanoid  
import pandas as pd
from tabulate import tabulate
import configparser

class TaskTracker:
    
    def __init__(self):
        
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        # print(self.config.sections())
        self._author = self.config['App']['author']
        self._version = self.config['App']['version']
        self.default_greeting = self.config['UI']['greeting_message']
        self.task_file = self.config['Files']['tasks_file']
        self.fieldnames = ['Task ID', 'Title', 'Description', 'Created_date', 'Created_by', 'Due_date', 'Task_priority', 'Status']
 
    def __str__(self):
        self.greet()
        return (f"-----------Task Tracker {self._version} presented by {self._author}-----------")
        
    def greet(self, message = None):
        if message is None:
            return self.default_greeting
        cowsay.cow(message)
        
    def menu(self):
        while True:
            self.update_priorities()
            user_input = int(input("""
                What is your purpose today?
                1. Add a new task
                2. Edit an existing task
                3. Delete a task
                4. Mark a task as complete
                5. View all tasks
                6. Filter tasks
                7. Sort tasks
                8. Exit
                """))
            if user_input == 1:
                self.add_tasks()
                                
            elif user_input == 2:
                self.edit_tasks()
                                
            elif user_input == 3:
                self.delete_task()
                
            elif user_input == 4:
                self.task_status()
                
            elif user_input == 5:
                self.display_tasks()
                
            elif user_input == 6:
                self.filter_tasks()
                
            elif user_input == 7:
                self.sort_tasks()
                
            elif user_input == 8:
                self.greet("Thank you for using the application")
                break
            else:
                self.greet("Invalid input please check your input and retry")
    
    def add_tasks(self):
        
        self.greet("Add a new Task")
        
        # fieldnames = ['Task ID', 'Title', 'Description', 'Created_date', 'Created_by', 'Due_date', 'Task_priority', 'Status']

        # checking if the file exists
        try:
            with open('tasks.csv', 'r') as file:
                pass
        except FileNotFoundError:
            with open('tasks.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames) # type: ignore
                writer.writeheader()
                
        # Now, get task details from user
        task_id = self.get_uid()
        task_title = input("Title: ")
        task_description = input("Task: ")
        created_date = datetime.date.today()
        created_by = input("Enter the author name: ") or self._author
        due_date = self.get_due_date()
        task_priority = Priority(due_date).task_priority()
        status = self.get_task_status()

        # Prepare the data
        data = {
            "Task ID" : task_id,
            "Title": task_title,
            "Description": task_description,
            "Created_date": created_date,
            "Created_by": created_by,
            "Due_date": due_date,
            "Task_priority": task_priority,
            "Status": status
        }
        
        file_exists = os.path.isfile('tasks.csv')
        file_empty = os.stat('tasks.csv').st_size == 0 if file_exists else True
        
        # now append the data
        with open('tasks.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            if file_empty:
                writer.writeheader()
            writer.writerow(data)
        print("Task successfully added!")
    
    def get_uid(self):
        # nanoid library uses a larger alphabet than base64, including uppercase, lowercase and numbers and special characters
        # this is collision resistant, customizable alphabet and numbers, efficient and fast.
        return nanoid.generate(alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", size = 6) 
        
    def get_due_date(self):
        while True:
            date_str = input("Enter due_date in YYYY-MM-DD format: ")
            try:
                return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                print('''Invalid date format
                      Enter date in YYYY-MM-dd format''')

    def get_task_status(self):
        statuses = {1: 'Not Started', 2: 'In Progress', 3: 'Comlpleted'}
        while True:
            try:
                user_choice = int(input('''Enter the status of the task,
                                        1. Not Started
                                        2. In Progress
                                        3. Completed
                                        '''))
                if user_choice in statuses:
                    return statuses[user_choice]
                else:
                    print("Invalid Input! Try again with a valid input")
            except ValueError:
                print("Invalid input!, Please enter a number")
                
    def edit_tasks(self):
        self.greet("Edit an existing Task")
        self.display_tasks()
        pass
    
    def delete_task(self):
        self.greet("Delete a task")
        self.display_tasks()
        pass
    
    def task_status(self):
        self.greet("Check the status of the task")
        pass
    
    def display_tasks(self):
        # self.greet("View all the tasks")
        self.update_priorities()
        df = pd.read_csv('tasks.csv')
        # print(df.to_string()) # this will return in tabular format without any boundaries for cells
        print(tabulate(df, headers = 'keys' , tablefmt='grid'))
    
    def filter_tasks(self):
        self.greet("Filter the tasks")
        while True:
            try:
                filter_condition = int(input('''Enter the basis of filtering:
                                        1. Based on Priority
                                        2. Based on Status
                                        3. Based on Task creation date
                                        4. Based on Title
                                        5. Based on Author
                                        '''))
                
                if filter_condition == 1:
                    self.greet("Filtering based on Priority of the task")
                    self.menu()
                    pass
                elif filter_condition == 2:
                    self.greet("Filtering based on Status of the task")
                    self.menu()
                    pass
                elif filter_condition == 3:
                    self.greet("Filtering based on Task creation date")
                    self.menu()
                    pass
                elif filter_condition == 4:
                    self.greet("Filtering based on Title")
                    self.menu()
                    pass
                elif filter_condition == 5:
                    self.greet("Filtering based on Author")
                    self.menu()
                    pass
                else:
                    print("Please enter a number from 1 to 5")
                    
            except ValueError:
                print("Invlaid input!. Please enter a number from 1 to 5")
            
        
        
        pass
    
    def sort_tasks(self):
        self.greet("Sort the tasks")
        pass
    
    def update_priorities(self):
        # this method is used to update the priorities of the tasks everytime we load them based on the due_days left
        updated_priorities = []
        with open('tasks.csv', 'r') as file:
            reader = csv.DictReader(file)
            for task in reader:
                priority = Priority(task).task_priority()
                task['Task_priority'] = priority
                updated_priorities.append(task)
        with open('tasks.csv', 'w', newline='') as file:
            reader = csv.DictWriter(file, fieldnames=self.fieldnames)
            reader.writeheader()
            reader.writerows(updated_priorities)
        
if __name__ == "__main__":
    task = TaskTracker()
    print(task.greet())
    print(task)
    task.menu()