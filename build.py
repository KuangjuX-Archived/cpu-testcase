import os 
import shutil

inst_dir = "src/inst"
inst_array = []

for root, dirs, files in os.walk(inst_dir, topdown=False):
    if root == inst_dir:
        for file in files: 
            file = file[:-2]
            print("编译用户程序: " + file)
            os.system("make USER_PROGRAM?=" + file)

print("编译成功")

