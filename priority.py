import datetime
import os

class Priority:
    
    def __init__(self, due_date):
        self.today = datetime.date.today()
        self.due_date = due_date
    
    def task_priority(self):
        days_left = (self.due_date - self.today).days
        '''
        
            Critical: <= 3 days
            High: <= 10 days
            Medium: <= 20 days
            Low: <= 30 days
            No priority: > 30 days
        '''
        if days_left <= 3:
            return "Critical"
        elif 4 <= days_left <= 10:
            return "High Priority"
        elif 11 <= days_left <= 20:
            return "Medium Priority"
        elif 21 <= days_left <= 30:
            return "Low Priority"
        else:
            return "No Priority"
        
        #return f"This task is of {priority}, days left {days_left}."
                                   
if __name__ == "__main__":
    #due_date = datetime.date(2024, 12, 31) # testing
    a = Priority(due_date)
    a.task_priority()
    #result = a.task_priority()
    #print(result)
