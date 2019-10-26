import os
for root, dirs, files in os.walk('.'):
    print(root, dirs, files, end=" ")
    # TODO
    # match the md file, get path, add on the README
