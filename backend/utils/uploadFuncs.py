from utils.miscFuncs import progress


def checkFilePathLength(filePath: str): # planned to implement support for larger file paths soon
    if len(filePath) > 4096:
        print("Due to limitations on Telegram, the complete file path must be no more than 4096 characters long.")
        quit()

    else: pass # move to uploading the file


def uploadFile(app: object, filePath: str):
    try:
        app.send_document("me", filePath, progress=progress, caption=filePath)

    except ValueError:
        print("File(s) not found.")