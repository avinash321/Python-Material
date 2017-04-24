import os
if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"
print os.system(command)
