from utils.miscFuncs import uploadProgress
from utils.databaseFuncs import checkItemExists, addItem
import os


def checkFilePath(filePath: str): # planned to implement support for larger file paths soon
    if len(filePath) > 4096: print("Due to limitations on Telegram, the complete file path must be no more than 4096 characters long.")
        
    elif len(filePath) == 0: print("No file path was provided.")
    
    elif not os.path.exists(filePath): print("The file path provided does not exist.")
    
    elif os.path.getsize(filePath) == 0: print("The file provided is empty.")

    else: return True


def uploadFile(app: object, filePath: str):
    app.send_document("me", filePath, progress=uploadProgress, caption=filePath)
    uploadedFile = list(app.get_chat_history("me", limit=1))[0].document.file_id


    directories = filePath.split("/")
    currentDirectory = ""

    # create "directories" for the file's path if they don't already exist
    for i in range(len(directories) - 1):
        if directories[i]:
            currentDirectory += f"{directories[i]}/"

            if checkItemExists(currentDirectory) == False:
                addItem(currentDirectory)

    
    addItem(filePath, uploadedFile)

    print(f"File \"{filePath}\" uploaded successfully.")


def performUpload(app: object):
    filePath: str = input("Enter file path: ")


    if checkFilePath(filePath) == True:
        if os.path.isdir(filePath):
            for dirpath, dirnames, filenames in os.walk(filePath):
                for filename in filenames:
                    filePath = os.path.join(dirpath, filename)
                    
                    if checkFilePath(filePath) == True:
                        uploadFile(app, filePath)

        else: uploadFile(app, filePath)