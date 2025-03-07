import os
self = "goodies.py"
def cat_time():
    """
    This function creates a directory called "cats" and deletes a directory called "dogs""
    """
    if os.path.exists("dogs"):
     os.rmdir("dogs")
    os.mkdir("cats")
choice = input("Remove goodies.py? (y/n): ")
if choice == "y":
 os.remove(self)
elif choice == "n":
 cat_time()

choice = input("Clean up? (y/n): ")
if choice == "y":
 os.system("rm -rf __pycache__")
elif choice == "n":
 pass