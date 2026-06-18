"""

 DECODELABS INDUSTRIAL TRAINING KIT - PYTHON PROGRAMMING
 PROJECT 1 : THE TO-DO LIST

"""


# STORAGE (The "Heap")
# my_tasks starts as an empty list. This is the "Zero of Lists" -
# the single variable that will hold ALL our tasks in RAM.
# NOTE: This is volatile memory. Once the program ends, this list
# (and everything in it) disappears. Real engines later move this
# data to permanent Storage (a file or database) - but for Project 1
# our job is just to master the in-memory list itself.



def show_menu():
    """Display the available actions to the user (part of the VIEW / UI layer)."""
    print("\n" + "=" * 30)
    print("        TO-DO LIST")
    print("=" * 30)
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")


def add_task(my_tasks):
    """
    INPUT + PROCESS step.
    Takes text typed by the user, wraps it in a dictionary
    """
    task_text = input("Enter the task you want to add: ").strip()

    if task_text == "":
        print(" Task cannot be empty. Please try again.")
        return

    # Each task is a dictionary -> this is our "table row".
    # "id" acts like a Primary Key, "task" holds the actual description,
    # and "done" tracks whether it has been completed.
    new_task = {
        "id": len(my_tasks) + 1,   # Simple auto incrementing ID
        "task": task_text,
        "done": False
    }

    my_tasks.append(new_task)  # <-- THE KEY SKILL: append() to the list
    print(f' Task added successfully: "{task_text}"')


def view_tasks(my_tasks):
    """
    OUTPUT / DISPLAY step.

    """
    print("\n--- Your Tasks ---")

    if not my_tasks:
        print("(No tasks yet. Add one from the menu!)")
        return

    for index, task in enumerate(my_tasks, start=1):
        status = " Done" if task["done"] else " Pending"
        print(f'{index}. {task["task"]}   [{status}]')


def mark_task_done(my_tasks):
    """Marks a task as done based on user input."""
    view_tasks(my_tasks)
    if not my_tasks:
        return

    try:
        task_num = int(input("\nEnter the task number to mark as done: ").strip())
        if 1 <= task_num <= len(my_tasks):
            my_tasks[task_num - 1]["done"] = True
            print(f' Task {task_num} marked as done!')
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")


def main():
    """
    The main program loop.
    """
    # This is our single in-memory "database" - a list of dictionaries.
    my_tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            mark_task_done(my_tasks)
        elif choice == "4":
            print("Goodbye!  (Remember: this data is volatile and "
                  "will be lost once the program closes.)")
            break
        else:
            print(" Invalid choice. Please enter 1, 2, 3, or 4.")



# This line ensures main() only runs when this file is executed

if __name__ == "__main__":
    main()