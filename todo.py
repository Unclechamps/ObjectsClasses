# You are responsible for creating a TODO list app. Here are the requested features for the TODO list app:
# - User should be able to view all the tasks
# - User should be able to remove the tasks
# - User should be able to quit the app when "q" is pressed
# HARD MODE:
# - User should be able to enter priority of the task
# - User should be able to sort the tasks based on priority

class Todo:
    def __init__(self, list_description, date):
        self.list_description = list_description
        self.date = date
        self.todo_list = []

    def add_task(self):
        number_of_tasks = int(input("How many tasks do you want to enter? "))
        for i in range(1, (number_of_tasks)+1):
            priority = input("What priority (High/Medium/Low): ")
            new_task = input("Enter new task: ")
            task_and_priority = priority + " priority - " + new_task
            self.todo_list.append(task_and_priority)
        print(f"A total of {number_of_tasks} task(s) have been added to your list.")
        print(self.todo_list)

    def list_tasks(self):
        print(self.todo_list)

    def remove_tasks(self):
        task_to_remove = input("Which task do you want to remove? ")
        self.todo_list.remove(task_to_remove)
        print(self.todo_list)

    def quit(self):
        pass

    def __repr__(self):
        return f"{self.list_description} for {self.date}"

new_todo_list = Todo("Gabe's Todo", "5/7/2018")

action = input("Enter the number for option: 1. Add task, 2. View all tasks, 3. Remove task, Q. Quit application: ")

if action == '1':
    new_todo_list.add_task()
elif action == '2':
    new_todo_list.list_tasks() #only works if I execute the add_task function and then this one.
elif action == '3':
    new_todo_list.remove_tasks()
elif action == 'q' or action == 'Q':
    new_todo_list.quit()
else:
    print("Not sure what you are asking for!?")
