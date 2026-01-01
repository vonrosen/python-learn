# 1. Initialize an empty list to store tasks
tasks = []

print("--- Welcome to your Python Task Manager ---")

# 2. Start a loop that runs forever until we break it
while True:
    print("\nOptions: [1] Add Task [2] View Tasks [3] Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_task = input("Enter the task description: ")
        tasks.append(new_task) # Adding to the list
        print("Task added!")

    elif choice == "2":
        print("\n--- Your Current Tasks ---")
        if not tasks:
            print("Your list is empty.")
        else:
            # Using a for-loop to print the list with numbers
            for index, item in enumerate(tasks, start=1):
                print(f"{index}. {item}")

    elif choice == "3":
        print("Goodbye!")
        break # This exits the while loop

    else:
        print("Invalid choice, try again.")