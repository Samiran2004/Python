import shutil
import datetime
import os

def backupFile(source, destination):
    today = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")  # More robust date/time format
    backupFileName = os.path.join(destination, f"backup_{today}.tar.gz")

    # The fix is here: root_dir is a separate argument
    shutil.make_archive(backupFileName, 'gztar', root_dir=source)  

destination = "/home/samiransamanta/PythonForDevOps/backups"
source = "/home/samiransamanta/PythonForDevOps"
backupFile(source, destination)