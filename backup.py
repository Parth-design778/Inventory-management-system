import shutil
class BackUP:
    def __init__(self):
        pass
    def bckup():
        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/pbs.db"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)

        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/inventory.db"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)

        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/user_credentials.db"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)
        
        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/pbs.sqbpro"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)

        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/user_credentials.sqbpro"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)
        
        quit(0)