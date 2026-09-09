def get_todos(filepath="todo.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open('todo.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg , filepath="todo.txt"):
    """ Write  the to-do items list in the text file."""
    with open('todo.txt', 'w') as file:
        file.writelines(todos_arg)
print("Hello from functions")