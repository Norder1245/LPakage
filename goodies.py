import os
os.system("clear")
self = "goodies.py"
def cat_time():
    """
    This function creates a directory called "cats" and deletes a directory called "dogs""
    """
    if os.path.exists("dogs"):
     os.rmdir("dogs")
    os.mkdir("cats")

