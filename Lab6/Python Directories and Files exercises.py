import os
import shutil

def list_directories_files(path):
    """Lists all directories and files in a given path."""
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All Entries:", os.listdir(path))

def check_access(path):
    """Checks existence and permissions for a given path."""
    print(f"Checking access for: {path}")
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

def check_path(path):
    """Checks if a path exists and extracts filename and directory portion."""
    if os.path.exists(path):
        print("Path exists")
        print("Directory part:", os.path.dirname(path))
        print("Filename part:", os.path.basename(path))
    else:
        print("Path does not exist")

def count_lines(filename):
    """Counts the number of lines in a given file."""
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    with open(filename, 'r', encoding='utf-8') as file:
        print(f"Number of lines in {filename}: {sum(1 for _ in file)}")

def write_list_to_file(filename, data):
    """Writes a list of strings to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(str(item) + '\n')
    print(f"List written to {filename}")

def generate_text_files():
    """Generates 26 text files named A.txt to Z.txt."""
    for i in range(65, 91):  # ASCII A-Z
        with open(f"{chr(i)}.txt", 'w', encoding='utf-8') as file:
            file.write(f"This is file {chr(i)}.txt\nGenerated for testing purposes.")
    print("26 text files generated.")

def copy_file(source, destination):
    """Copies contents of one file to another."""
    if not os.path.exists(source):
        print("Source file does not exist.")
        return
    shutil.copy(source, destination)
    print(f"File {source} copied to {destination}")

def delete_file(path):
    """Deletes a file after checking its existence and access permissions."""
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"File {path} deleted successfully.")
    else:
        print("File does not exist or no permission to delete.")

# Example usage:
# list_directories_files("./my_project")
# check_access("config.yaml")
# check_path("server.log")
# count_lines("data.txt")
# write_list_to_file("output.txt", ["Task 1", "Task 2", "Task 3"])
# generate_text_files()
# copy_file("source.txt", "backup/source_backup.txt")
# delete_file("old_log.txt")
