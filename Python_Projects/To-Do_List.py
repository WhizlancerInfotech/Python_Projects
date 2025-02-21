tasks = []
while True:
    task = input("Enter a task (or type 'exit' to stop): ")
    if task.lower() == 'exit':
        break
    tasks.append(task)

print("Your To-Do List:", tasks)
