import sqlite3


connection: object = sqlite3.connect("backend/files.db")
cursor: object = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS files (file TEXT, fileID TEXT)")


def addFile(filePath: str, fileID: str):
    cursor.execute("INSERT INTO files (file, fileID) VALUES (?, ?)", (filePath, fileID))
    
    connection.commit()


def retrieveFile(filePath: str):
    cursor.execute("SELECT fileID FROM files WHERE file = ?", (filePath,))
    
    return cursor.fetchone()


def retrieveAllFilesInDirectory(directory: str):
    cursor.execute("SELECT file, fileID FROM files WHERE file LIKE ?", (f"{directory}%",))
    
    return cursor.fetchall()