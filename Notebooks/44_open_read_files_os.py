import os

# Gets us the current directory (getcwd)
print(os.getcwd())

# List files and items in the specified directory or the current one if absent path parameter
print(os.listdir())
print(os.listdir("Milestone_Project"))

# Commands for deleting Files

os.unlink('')     # Deletes a file from the specified Path
os.rmdir('')      # Deletes a directory but it must be empty first



print("------------------------")
# Import Shell Utilities module
import shutil

# Move files by providing path to file and destination path
shutil.move("currentpathtofile", "destinationpath")


print("------------------------")
import send2trash

# Safer method to delete files by sending them to the trash bin with the component above
send2trash.send2trash("send_me_to_trash.txt")

# Creates a tree of the directory specified
os.walk()