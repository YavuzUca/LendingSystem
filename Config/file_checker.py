import os


def file_checker():
    mydir = ["Backups", "Backups/Users", "Backups/Books", "Backups/Loanitems"]

    for file in mydir:
        check_folder = os.path.isdir(file)

        if not check_folder:
            os.makedirs(file)
