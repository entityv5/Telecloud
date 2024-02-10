import os
from utils.uploadFuncs import checkFilePathLength, uploadFile

try:
    from pyrogram import Client

except ModuleNotFoundError:
    print("All required modules are not found. Check README.md for more information.")
    quit()

try:
    from credentials import api_id, api_hash

except ModuleNotFoundError:
    print("Credentials file not found. Check README.md for more information.")
    quit()


if os.path.exists("backend/session.session"): app: object = Client("session")

else: app: object = Client("session", api_id=api_id, api_hash=api_hash)


def main():
    app.start()


    filePath: str = input("Enter the file path: ")

    if checkFilePathLength(filePath) == True:
        uploadFile(app, filePath)


    app.stop()


if __name__ == "__main__":
    main()