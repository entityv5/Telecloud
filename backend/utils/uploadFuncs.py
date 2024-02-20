from utils.miscFuncs import progress
from utils.fileIdsDatabase import addFile
import os


def checkFilePath(filePath: str): # planned to implement support for larger file paths soon
    if len(filePath) > 4096: print("Due to limitations on Telegram, the complete file path must be no more than 4096 characters long.")
        
    elif len(filePath) == 0: print("No file path was provided.")
    
    elif not os.path.exists(filePath): print("The file path provided does not exist.")
    
    elif os.path.getsize(filePath) == 0: print("The file provided is empty.")

    else: return True


def uploadFile(app: object, filePath: str):
    app.send_document("me", filePath, progress=progress, caption=filePath)
    uploadedFile = list(app.get_chat_history("me", limit=1))[0].document.file_id
    
    addFile(filePath, uploadedFile)

    print("File(s) uploaded successfully.")