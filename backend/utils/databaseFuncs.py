import sqlite3


connection: object = sqlite3.connect("backend/files.db")
cursor: object = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS files (file TEXT, fileID TEXT)")


def addItem(filePath: str, fileID: str = None):
    cursor.execute("INSERT INTO files (file, fileID) VALUES (?, ?)", (filePath, fileID))
    
    connection.commit()


def checkItemExists(filePath: str):
    cursor.execute("SELECT file FROM files WHERE file = ?", (filePath,))
    
    if cursor.fetchone() == None: return False
    else: return True


def retrieveItem(filePath: str):
    cursor.execute("SELECT fileID FROM files WHERE file = ?", (filePath,))
    
    return cursor.fetchone()


def retrieveAllItemsInDirectory(directory: str):
    # return files in the directory along with the subdirectories in that directory
    cursor.execute("SELECT file, fileID FROM files WHERE file LIKE ? OR file NOT LIKE ?", (f"{directory}%/", f"{directory}%/%"))
    items = cursor.fetchall()

    # filter out subdirectories that are not directly in the directory passed in to the function
    filteredItems = [item for item in items if item[0] != directory and item[0].count("/") < directory.count("/") + 2]

    return filteredItems