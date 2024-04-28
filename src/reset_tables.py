import os
import pandas
import shutil


def reset_tables_v2():
    for working_files in os.listdir("tables"):
        if working_files.endswith("csv"):
            os.unlink("tables\\" + working_files)
            print("Deleted: " + working_files)
    for backup_files in os.listdir("tables\\backups"):
        if backup_files.endswith("csv"):
            print("Restored: " + backup_files)
            shutil.copy("tables\\backups\\" + backup_files, "tables")


reset_tables_v2()
