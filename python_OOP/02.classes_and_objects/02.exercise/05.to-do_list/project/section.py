from .task import Task

class Section:
    def __init__(self, name:str):
        self.name = name
        self.tasks = []
    
    def add_task(self,new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'
    
    def complete_task(self,task_name:str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        new_tasks = [task for task in self.tasks if not task.completed]
        count = len(self.tasks) - len(new_tasks)
        self.tasks = new_tasks
        return f'Cleared {count} tasks.'
    
    def view_section(self):
        tasks_text = "\n".join([task.details() for task in self.tasks])
        return f'Section {self.name}:\n{tasks_text}'

section = Section('sect')
task1 = Task('task1','today')
task2 = Task('task2','tomorrow')

print(task1.details())
print(task1.comments)
print(task1.add_comment('kurec1'))
print(task1.comments)
print(task1.change_name('kur1'))
print(task1.change_due_date('datakurec1'))
print(task1.details())
print(task1.edit_comment(0,'dulugkurec1'))
print(task1.edit_comment(1,'mnogodulugkurec1'))

print(section.add_task(task1))
print(section.add_task(task2))
print(section.view_section())
print(section.clean_section())
print(section.view_section())
print(section.complete_task(task2.name))
print(section.view_section())
print(section.clean_section())
print(section.view_section())