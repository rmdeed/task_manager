# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date


# - Create a function that can register a user
def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = input("New Username: ")
    # - Check if username already exists. If so then print appropriate message and ask again.
    while new_username in username_password.keys():
        print("That username already exists. Try another.")
        new_username = input("New Username: ")

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


# - Create a function that can add a task
def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following:
         - A username of the person whom the task is assigned to,
         - A title of a task,
         - A description of the task and
         - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    while task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        task_username = input("Name of person assigned to task: ")
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


# - Create a function that can view all tasks
def view_all():
    '''Reads the task from task.txt file and prints to the console in the
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling)
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


# - Create a function that can view the users specific tasks
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling)
    '''
    # - Add a task number variable
    task_number = 1
    for t in task_list:
        if t['username'] == curr_user:
            # - Display the task number variable
            disp_str = f"\nTask number: \t {task_number}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            # - Increase the task number variable for each task
            task_number += 1
    select = int(input("Select a task by typing the task number (if you don't want to select a task type '-1'): "))
    if select > 0:
        select_task(select)
    elif select == -1:
        pass


# - Create a function that can select a task
def select_task(num):
    # - presenting the user choices and make sure that the users input is converted to lower case.
    choices = input(f'''What would you like to do to task number {num}:
m - mark the task as complete
e - edit the task
: ''').lower()
    while choices != "m" and choices != "e":
        print("That option isn't available.")
        choices = input(f'''What would you like to do to task number {num}:
m - mark the task as complete
e - edit the task
: ''').lower()
    if choices == "m":
        # - if the user picks m then ask if the task is completed
        complete = input("Is the task complete? Type 'Yes' or 'No': ").capitalize()
        # - If the task is completed then change completed to True
        while complete != "Yes" and complete != "No":
            print("That option isn't available.")
            complete = input("Is the task complete? Type 'Yes' or 'No': ").capitalize()
        if complete == "Yes":
            task = task_list.pop(num - 1)
            task['completed'] = True
            task_list.insert(num - 1, task)
            with open("tasks.txt", "w") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))
            print("Task successfully completed.")
        else:
            # - If the task is not completed then print appropriate message
            print("Please complete the task.")
    elif choices == "e":
        # - if the user picks e then pop task for editing
        task = task_list.pop(num - 1)
        # - if task is already completed print appropriate message
        if task['completed']:
            print("Task can not be edited as it is already complete.")
            task_list.insert(num - 1, task)
        # - if task is not completed present the user with choices and convert to lowercase
        elif not task['completed']:
            edit_choice = input(f'''Pick a part of task number {num} to edit:
u - username of the person to whom the task is assigned
d - due date of the task
: ''').lower()
            # - if the user picks u let them change the username assigned to the task
            if edit_choice == "u":
                task['username'] = input("Enter new username for task to be assigned to: ")
                while task['username'] not in username_password.keys():
                    print("That username doesn't exist. Try another.")
                    task['username'] = input("Enter new username for task to be assigned to: ")
                task_list.insert(num - 1, task)
                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                print("Username successfully edited.")
            # - if the user picks d let them change the due date of the task
            elif edit_choice == "d":
                while True:
                    try:
                        new_task_due_date = input("Enter new date that the task is due (YYYY-MM-DD): ")
                        task['due_date'] = datetime.strptime(new_task_due_date, DATETIME_STRING_FORMAT)
                        break
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")
                task_list.insert(num - 1, task)
                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                print("Due date successfully edited.")


# - Create a function that can output a task overview
def task_overview():
    task_overview_to_write = []
    # - The total number of tasks
    total_overall_tasks = f"The total number of tasks: {len(task_list)}"
    task_overview_to_write.append(total_overall_tasks)
    # - The total number of completed tasks
    completed_tasks = 0
    for t in task_list:
        if t['completed']:
            completed_tasks += 1
    total_completed_tasks = f"The total number of completed tasks: {completed_tasks}"
    task_overview_to_write.append(total_completed_tasks)
    # - The total number of uncompleted tasks
    uncompleted_tasks = 0
    for t in task_list:
        if not t['completed']:
            uncompleted_tasks += 1
    total_uncompleted_tasks = f"The total number of uncompleted tasks: {uncompleted_tasks}"
    task_overview_to_write.append(total_uncompleted_tasks)
    # - The total number of tasks that haven't been completed and that are overdue
    overdue_tasks = 0
    for t in task_list:
        if not t['completed']:
            if t['due_date'] < datetime.now():
                overdue_tasks += 1
    total_overdue_tasks = f"The total number of overdue tasks: {overdue_tasks}"
    task_overview_to_write.append(total_overdue_tasks)
    # - The percentage of tasks that are incomplete
    per_incomplete_tasks = (uncompleted_tasks / len(task_list)) * 100
    percentage_incomplete_tasks = f"The percentage of tasks that are incomplete: {round(per_incomplete_tasks, 2)}%"
    task_overview_to_write.append(percentage_incomplete_tasks)
    # - The percentage of tasks that are overdue
    per_overdue_tasks = (overdue_tasks / uncompleted_tasks) * 100
    percentage_overdue_tasks = f"The percentage of tasks that are overdue: {round(per_overdue_tasks, 2)}%"
    task_overview_to_write.append(percentage_overdue_tasks)
    with open("task_overview.txt", "w") as task_file:
        task_file.write("\n".join(task_overview_to_write))


def user_overview():
    user_overview_to_write = []
    # - The total number of users registered
    total_num_users = f"The total number of users registered: {len(username_password)}"
    user_overview_to_write.append(total_num_users)
    # - The total number of tasks
    total_overall_tasks = f"The total number of tasks: {len(task_list)}"
    user_overview_to_write.append(total_overall_tasks)
    # - User specifics
    total_users = []
    for user in username_password:
        each_user = []
        # - Username
        each_user.append(f"Username: {user}")
        # - The total number of tasks assigned to that user
        total_user_tasks = 0
        for t in task_list:
            if user == t['username']:
                total_user_tasks += 1
        each_user.append(f"The total number of tasks assigned to {user}: {total_user_tasks}")
        # - The percentage of the total number of tasks that have been assigned to that user
        if total_user_tasks > 0:
            per_total_user_tasks = round((total_user_tasks / len(task_list)) * 100, 2)
            each_user.append(f"The percentage of the total number of tasks that have been assigned to {user}: "
                             f"{per_total_user_tasks}%")
        else:
            per_total_user_tasks = 0
            each_user.append(f"The percentage of the total number of tasks that have been assigned to {user}: "
                             f"{per_total_user_tasks}%")
        # - The percentage of the tasks assigned to that user that have been completed
        completed_user_tasks = 0
        for t in task_list:
            if user == t['username']:
                if t['completed']:
                    completed_user_tasks += 1
        if completed_user_tasks > 0:
            per_completed_user_tasks = round((completed_user_tasks / total_user_tasks) * 100, 2)
            each_user.append(f"The percentage of the tasks assigned to {user} that have been completed: "
                             f"{per_completed_user_tasks}%")
        else:
            per_completed_user_tasks = 0
            each_user.append(f"The percentage of the tasks assigned to {user} that have been completed: "
                             f"{per_completed_user_tasks}%")
        # - The percentage of the tasks assigned to that user that must still be completed
        if total_user_tasks > 0:
            per_incomplete_user_tasks = round(100 - per_completed_user_tasks, 2)
            each_user.append(f"The percentage of the tasks assigned to {user} that must still be completed: "
                             f"{per_incomplete_user_tasks}%")
        else:
            per_incomplete_user_tasks = 0
            each_user.append(f"The percentage of the tasks assigned to {user} that must still be completed: "
                             f"{per_incomplete_user_tasks}%")
        # - The percentage of the tasks assigned to that user that have not yet been completed and are overdue
        overdue_tasks = 0
        for t in task_list:
            if user == t['username']:
                if t['due_date'] < datetime.now():
                    overdue_tasks += 1
        if overdue_tasks > 0:
            per_overdue_user_tasks = round((overdue_tasks / total_user_tasks) * 100, 2)
            each_user.append(f"The percentage of the tasks assigned to {user} that have not yet been completed "
                             f"and are overdue: {per_overdue_user_tasks}%")
        else:
            per_overdue_user_tasks = 0
            each_user.append(f"The percentage of the tasks assigned to {user} that have not yet been completed "
                             f"and are overdue: {per_overdue_user_tasks}%")
        total_users.append(each_user)
        join_total_users = ["\n".join(i) for i in total_users]
    user_overview_to_write.extend(join_total_users)
    with open("user_overview.txt", "w") as task_file:
        task_file.write("\n\n".join(user_overview_to_write))


DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

# ====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        task_overview()
        user_overview()
    elif menu == 'ds' and curr_user == 'admin':
        # - If the user is an admin they can display from the generated reports
        # - Create task_overview.txt and user_overview.txt if they don't exist
        if not os.path.exists("task_overview.txt"):
            task_overview()
        if not os.path.exists("user_overview.txt"):
            user_overview()
        # - display information from task overview and user overview.
        with open("task_overview.txt", "r") as task_overview_file:
            task_overview_read = task_overview_file.read()
        print("-----------------------------------")

        print("TASK OVERVIEW\n")
        print(task_overview_read)
        with open("user_overview.txt", "r") as user_overview_file:
            user_overview_read = user_overview_file.read()
        print("-----------------------------------")
        print("USER OVERVIEW\n")
        print(user_overview_read)
        print("-----------------------------------")
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
