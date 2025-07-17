from filemanager.file_ops import copy, move, delete

copy("src.txt", "dest.txt")
move("dest.txt", "archive/dest.txt")
delete("archive")
