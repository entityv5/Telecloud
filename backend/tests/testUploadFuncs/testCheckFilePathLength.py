from utils.uploadFuncs import checkFilePathLength


def testCheckFilePathLengthWithOver4096Characters(capsys):
    checkFilePathLength("a" * 4097)
    captured = capsys.readouterr()
    assert captured.out == "Due to limitations on Telegram, the complete file path must be no more than 4096 characters long.\n"

    checkFilePathLength("a" * 5000)
    captured = capsys.readouterr()
    assert captured.out == "Due to limitations on Telegram, the complete file path must be no more than 4096 characters long.\n"


def testCheckFilePathLengthWithEmptyPath(capsys):
    checkFilePathLength("")
    captured = capsys.readouterr()
    assert captured.out == "No file path was provided.\n"


def testCheckFilePathLengthWithValidPaths():
    assert(checkFilePathLength("backend/tests/dummyFiles/dummyFile1.txt") == True)
    assert(checkFilePathLength("backend/tests/dummyFiles/dummyFile2.txt") == True)
    assert(checkFilePathLength("backend/tests/dummyFiles/dummyFile3.txt") == True)