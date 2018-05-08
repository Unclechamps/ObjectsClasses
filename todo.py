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
        self.exit = False
        self.todo_list = []

    def userOptions(self):
        if self.exit == False:
            selectedOption = input("Enter the number for option: 1. Add task, 2. View all tasks, 3. Remove task, Q. Quit application: ")
            if selectedOption == '1':
                self.add_task()
            elif selectedOption == '2':
                self.list_tasks() #only works if I execute the add_task function and then this one.
            elif selectedOption == '3':
                self.remove_tasks()
            elif selectedOption == 'q' or action == 'Q':
                self.quit()
            else:
                print("Not sure what you are asking for!?")

    def add_task(self):
        number_of_tasks = int(input("How many tasks do you want to enter? "))
        for i in range(1, (number_of_tasks)+1):
            priority = input("What priority (High/Medium/Low): ")
            new_task = input("Enter new task: ")
            task_and_priority = priority + " priority - " + new_task
            self.todo_list.append(task_and_priority)
        print(self.todo_list)
        self.userOptions()

    def list_tasks(self):
        print(self.todo_list)
        self.userOptions()

    def remove_tasks(self):
        task_to_remove = int(input("Which task # do you want to remove? "))-1
        self.todo_list.remove(self.todo_list[task_to_remove])
        print(self.todo_list)
        self.userOptions()

    def quit(self):
        self.exit = True

    def __repr__(self):
        return f"{self.list_description} for {self.date}"

new_todo_list = Todo("Gabe's Todo", "5/7/2018")

new_todo_list.userOptions()
