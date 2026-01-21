import os

# specify the directory (you can change this to any path you want)
directory = "/"

# list all files and folders in the given directory
try:
    contents = os.listdir(directory)
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"You don't have permission to access '{directory}'.")
