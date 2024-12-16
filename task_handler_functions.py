import configparser

class TaskHandler:
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.file_name = self.config['Files']['tasks_files']
        self.fieldnames = ['Task ID', 'Title', 'Description', 'Created_date', 'Created_by', 'Due_date', 'Task_priority', 'Status']
        
    def read_data(self):
        pass
    
    def write_data(self):
        pass
        
    def add_tasks(self):
        pass

    def display_tasks(self):
        pass
    
    def edit_tasks(self):
        pass
    
    def delete_tasks(self):
        pass
    
    def filter_tasks(self):
        pass
    
    def sort_tasks(self):
        pass
    
    