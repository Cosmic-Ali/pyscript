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







