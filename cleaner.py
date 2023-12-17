import os
import shutil
import time

def main():
    files_and_folders_to_delete = ["Songs", "songlist.csv"]
    
    time.sleep(5)

    for item in files_and_folders_to_delete:
        try:
            if os.path.isfile(item):
                os.remove(item)
                print(f"{item} (file) deleted successfully.")
            elif os.path.isdir(item):
                shutil.rmtree(item)
                print(f"{item} (folder) deleted successfully.")
            else:
                print(f"{item} not found.")
        except Exception as e:
            print(f"An error occurred while deleting {item}: {str(e)}")

if __name__ == "__main__":
    main()
