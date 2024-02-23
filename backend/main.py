import os
from utils.uploadFuncs import performUpload

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


    performUpload(app)


    app.stop()


if __name__ == "__main__":
    main()