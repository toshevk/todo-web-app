FILEPATH = 'tasks.txt'


def get_todos(file_location=FILEPATH):
    """ Return a list of to-do items written in tasks.txt """
    with open(file_location, 'r') as file_local:
        tasks_todo_local = file_local.readlines()
    return tasks_todo_local


def write_todos(content, file_location=FILEPATH):
    """ Update file with to-do items list. """
    with open(file_location, 'w') as file_local:
        file_local.writelines(content)


# print(__name__)
if __name__ == "__main__":
    print("Hello from functions module")
    print(get_todos())
