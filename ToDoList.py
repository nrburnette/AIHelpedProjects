"""
to-do list application where users can add, view, and mark tasks as completed.
You can implement features like task prioritization, due dates, and
the ability to save and load tasks from a file.
"""

#FIXME: ways to improve-> input validation for all entries, mouse interface for selecting remaining options

#a class used to create a to do item
class Task:
    def __init__(self):
        self.title = input("Enter the title of the task: ")
        self.priority = input("Enter 'High' or 'Low' for the priority level: ")
        self.due_date = input ("Enter the the date due as MM-DD-YY: ")
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nPriority: {self.priority}\nDue Date: {self.due_date}\nStatus: {status}"

#Task blueprint to create instances of tasks within todo list
task1 = Task()

#print task, complete task, reprint task showing completed
print()
print(task1)
print()
task1.mark_as_completed()
print(task1)

