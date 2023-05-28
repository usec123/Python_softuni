todo_list = []

def add_task(task):
    todo_list.append(task)
    print('Task added successfully')
    
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print('Task removed successfully')
    else: print('Task not found in the To-Do List')

def view_tasks():
    if todo_list:
        print('Tasks:')
        for task in todo_list:
            print(task)
    else:
        print('No tasks in the To-Do List')

while True:
    print('1. Add task')
    print('2. Remove task')
    print('3. View tasks')
    print('4. Exit')
    
    cmd = input('Enter your choice (1-4):')
    
    if cmd == '1':
        add_task(input('Enter task: '))
    elif cmd == '2':
        remove_task(input('Enter task to remove: '))
    elif cmd == '3':
        view_tasks()
    elif cmd == '4':
        print('Exiting the program')
        break
    else:
        print('Invalid choice. Please try again!')
    print()
    