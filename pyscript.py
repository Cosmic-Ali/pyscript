'''Description: This function takes a python code, and runs it in a py file using another subprocess,
and then deletes that file after execution.

Parameters: 

positional argument - code
    Input the code that you want to run as the only argument in the function.

keyword argument - del_script
    By default, del_script = False. This deletes the script upon completion of execution.
    Enter True to return path of the saved script


Note- 1. Include all the requirements/libraries (eg: import cv2) within the code.

      2. If you are including cv2.imshow(), make sure you also include cv2.waitkey(time)
         and do not leave it's argument empty, nor keep 0. And then include, cv2.DestroyAllWindows()

         When viewing a video, make sure to assign a quit key, to quit the loop

'''

import os

# def imshow(code):
#     file_path = '/Users/ali/Desktop/data_science/ML/computer_vision/imshow/file.py'
#     with open(file_path,'w') as file:
#         file.write(f'''{code}''')
        

#     with open(file_path,'r') as file:
#         exec(file.read())

#     os.remove(file_path)    # Deleting the file



import subprocess
import sys

def pyscript(code,del_script = True):
    # 1) Path to the “other” interpreter you want
    other_python = "/usr/local/bin/python3" # For Mac OS           # ← adjust as needed
    # on Windows it might be: r"C:\Python38\python.exe"

    # 2) Write out your generated script
    script_path = '/Users/ali/Desktop/data_science/ML/computer_vision/script/bin/file.py'
    with open(script_path, "w") as f:
        f.write(code)

    # 3) Spawn a new process running that interpreter on your file
    result = subprocess.run(
        [other_python, script_path],
        # capture_output=True,    # if you want to capture stdout/stderr
        # text=True,              # get output as string instead of bytes
    )

    # print("=== STDOUT ===")
    # print(result.stdout)
    # print("=== STDERR ===")
    # print(result.stderr)

    if del_script == True:
        os.remove(script_path)
        pass
    else:
        return script_path







