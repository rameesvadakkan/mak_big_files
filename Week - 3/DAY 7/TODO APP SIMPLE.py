def new_list():
    file_name = input("Enter the file name for your todo list: ")
    with open(file_name, 'x') as _:
        print(f"New todo list created: {file_name}")
    return file_name

def add_task(filename):
    task = input("Enter a new task: ")
    with open(filename, 'a') as f:
        f.write(task + "\n")
        print("Task added!")

def show_tasks(filename1):
    try:
        with open(filename1, 'r') as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks yet!")
            else:
                print("\n--- Your Tasks ---")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("File not found! Create a new list first.")
while True:
          print("Choice:\n\t1. Create New ToDo list \n\t2. Add New Task \n\t3. Show Tasks Added")
          choice = input("Enter Your choice: ")

          if choice == "1":
              new_list()
          elif choice == "2":
              file__name = input("Enter the file name: ")
              add_task(file__name)
          elif choice == "3":
              filename2 = input("Enter the file name: ")
              show_tasks(filename2)
          else:
               print("Invalid choice!")
