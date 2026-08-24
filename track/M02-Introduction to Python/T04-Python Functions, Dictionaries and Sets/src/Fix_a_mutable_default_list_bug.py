def add_task(task,tasks=None):
    if tasks is None:
        tasks=[]
    tasks.append(task)
    return tasks
print(add_task("Python"))
print(add_task("Java"))