from utils.uploadFuncs import checkFilePath


def testCheckFilePathWithOver4096Characters(capsys):
    checkFilePath("a" * 4097)
    captured = capsys.readouterr()
    assert captured.out == "Due to limitations on Telegram, the complete file path must be no more than 4096 characters long.\n"

    checkFilePath("a" * 5000)
    captured = capsys.readouterr()
    assert captured.out == "Due to limitations on Telegram, the complete file path must be no more than 4096 characters long.\n"


def testCheckFilePathWithEmptyPath(capsys):
    checkFilePath("")
    captured = capsys.readouterr()
    assert captured.out == "No file path was provided.\n"


def testCheckFilePathWithValidPaths():
    assert(checkFilePath("backend/tests/dummyFiles/dummyFile1.txt") == True)
    assert(checkFilePath("backend/tests/dummyFiles/dummyFile2.txt") == True)
    assert(checkFilePath("backend/tests/dummyFiles/dummyFile3.txt") == True)


def testCheckFilePathWithInvalidPaths(capsys):
    checkFilePath("backend/tests/dummyFiles/dummyFile4.txt")
    captured = capsys.readouterr()
    assert captured.out == "The file path provided does not exist.\n"

    checkFilePath("backend/tests/dummyFiles/dummyFile5.txt")
    captured = capsys.readouterr()
    assert captured.out == "The file path provided does not exist.\n"


def testCheckFilePathWithEmptyFiles(capsys):
    checkFilePath("backend/tests/dummyFiles/emptyDummyFile.txt")
    captured = capsys.readouterr()
    assert captured.out == "The file provided is empty.\n"