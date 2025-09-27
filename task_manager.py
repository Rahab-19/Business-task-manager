# Function to register a new user
def reg_user():
    with open('user.txt', 'r') as f:
        users = [line.strip().split(', ')[0] for line in f]

    while True:
        new_username = input("Enter new username: ")
        if new_username in users:
            print("Username already exists. Try a different username.")
        else:
            break

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")

    if new_password == confirm_password:
        with open('user.txt', 'a') as f:
            f.write(f"\n{new_username}, {new_password}")
        print("User registered successfully.")
    else:
        print("Passwords do not match. User not registered.")


# Function to add a new task
def add_task():
    assigned_user = input("Enter the username for the task: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")

    from datetime import date
    assigned_date = date.today().strftime("%Y-%m-%d")
    completed = "No"

    with open('tasks.txt', 'a') as f:
        f.write(
            f"\n{assigned_user}, {title}, {description}, "
            f"{assigned_date}, {due_date}, {completed}"
        )

    print("Task added successfully.")


# Function to view all tasks
def view_all():
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    for task in tasks:
        task_details = task.strip().split(', ')
        print(f"Assigned to: {task_details[0]}")
        print(f"Title: {task_details[1]}")
        print(f"Description: {task_details[2]}")
        print(f"Date Assigned: {task_details[3]}")
        print(f"Due Date: {task_details[4]}")
        print(f"Completed: {task_details[5]}")
        print("-" * 40)


# Function to view tasks assigned to the current user
def view_mine(username):
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    user_tasks = [
        task for task in tasks
        if task.strip().split(', ')[0] == username
    ]

    for i, task in enumerate(user_tasks, 1):
        task_details = task.strip().split(', ')
        print(f"Task {i}:")
        print(f"Title: {task_details[1]}")
        print(f"Description: {task_details[2]}")
        print(f"Date Assigned: {task_details[3]}")
        print(f"Due Date: {task_details[4]}")
        print(f"Completed: {task_details[5]}")
        print("-" * 40)


# Admin-only function to view completed tasks
def view_completed():
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    completed_tasks = [
        task for task in tasks
        if task.strip().endswith("Yes")
    ]

    for task in completed_tasks:
        task_details = task.strip().split(', ')
        print(f"Assigned to: {task_details[0]}")
        print(f"Title: {task_details[1]}")
        print(f"Description: {task_details[2]}")
        print(f"Date Assigned: {task_details[3]}")
        print(f"Due Date: {task_details[4]}")
        print(f"Completed: {task_details[5]}")
        print("-" * 40)


# Admin-only function to delete a task
def delete_task():
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

    task_num = int(input("Enter the number of the task to delete: "))

    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        with open('tasks.txt', 'w') as f:
            f.writelines(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")


# Admin-only function to generate task and user reports
def generate_reports():
    from datetime import datetime

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    total_tasks = len(tasks)
    completed_tasks = sum(
        1 for task in tasks if task.strip().endswith("Yes")
    )
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = 0
    today = datetime.today()

    for task in tasks:
        task_details = task.strip().split(', ')
        due_date = datetime.strptime(task_details[4], "%Y-%m-%d")
        if task_details[5] == "No" and due_date < today:
            overdue_tasks += 1

    with open('task_overview.txt', 'w') as f:
        f.write(f"Total tasks: {total_tasks}\n")
        f.write(f"Completed tasks: {completed_tasks}\n")
        f.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        f.write(f"Overdue tasks: {overdue_tasks}\n")
        f.write(
            f"Percentage incomplete: "
            f"{uncompleted_tasks / total_tasks * 100:.2f}%\n"
        )
        f.write(
            f"Percentage overdue: "
            f"{overdue_tasks / total_tasks * 100:.2f}%\n"
        )

    with open('user.txt', 'r') as f:
        users = [line.strip().split(', ')[0] for line in f]

    with open('user_overview.txt', 'w') as f:
        f.write(f"Total users: {len(users)}\n")
        f.write(f"Total tasks: {total_tasks}\n")

        for user in users:
            user_tasks = [
                task for task in tasks
                if task.strip().split(', ')[0] == user
            ]
            num_user_tasks = len(user_tasks)
            if num_user_tasks == 0:
                continue
            completed = sum(
                1 for task in user_tasks
                if task.strip().endswith("Yes")
            )
            uncompleted = num_user_tasks - completed
            overdue = 0
            for task in user_tasks:
                task_details = task.strip().split(', ')
                due_date = datetime.strptime(
                    task_details[4], "%Y-%m-%d"
                )
                if task_details[5] == "No" and due_date < today:
                    overdue += 1
            f.write(f"\nUser: {user}\n")
            f.write(f"Tasks assigned: {num_user_tasks}\n")
            f.write(
                f"Percentage of total tasks: "
                f"{num_user_tasks / total_tasks * 100:.2f}%\n"
            )
            f.write(
                f"Completed: "
                f"{completed / num_user_tasks * 100:.2f}%\n"
            )
            f.write(
                f"Uncompleted: "
                f"{uncompleted / num_user_tasks * 100:.2f}%\n"
            )
            f.write(
                f"Overdue: "
                f"{overdue / num_user_tasks * 100:.2f}%\n"
            )


# Admin-only function to display report statistics
def display_statistics():
    import os
    if not os.path.exists('task_overview.txt') or \
       not os.path.exists('user_overview.txt'):
        generate_reports()

    with open('task_overview.txt', 'r') as f:
        print(f.read())

    with open('user_overview.txt', 'r') as f:
        print(f.read())


# Login function
def login():
    with open('user.txt', 'r') as f:
        users = {
            line.strip().split(', ')[0]: line.strip().split(', ')[1]
            for line in f
        }

    while True:
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print("Login successful.")
            return username
        else:
            print("Invalid credentials. Please try again.")


# Main program function
def main():
    username = login()

    while True:
        if username == 'admin':
            menu = input('''\nSelect an option:
r  - register user
a  - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete a task
ds - display statistics
gr - generate reports
e  - exit
: ''').lower()
        else:
            menu = input('''\nSelect an option:
a  - add task
va - view all tasks
vm - view my tasks
e  - exit
: ''').lower()

        if menu == 'r' and username == 'admin':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine(username)
        elif menu == 'vc' and username == 'admin':
            view_completed()
        elif menu == 'del' and username == 'admin':
            delete_task()
        elif menu == 'ds' and username == 'admin':
            display_statistics()
        elif menu == 'gr' and username == 'admin':
            generate_reports()
        elif menu == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


# Ensures the program starts when the file is run
if __name__ == "__main__":
    main()
