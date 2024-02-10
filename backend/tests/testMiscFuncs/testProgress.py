from utils.miscFuncs import progress


def testProgressWithRegularValues(capsys):
    progress(1, 10)
    captured = capsys.readouterr()
    assert captured.out == "Uploaded 1 of 10 bytes.\n"

    progress(256, 512)
    captured = capsys.readouterr()
    assert captured.out == "Uploaded 256 of 512 bytes.\n"

    progress(111222333, 999888777)
    captured = capsys.readouterr()
    assert captured.out == "Uploaded 111222333 of 999888777 bytes.\n"


def testProgressWithIrregularValues(capsys):
    progress(24, 12)
    captured = capsys.readouterr()
    assert captured.out == "Uploaded 24 of 12 bytes.\n"

    progress(999888777, 111222333)
    captured = capsys.readouterr()
    assert captured.out == "Uploaded 999888777 of 111222333 bytes.\n"


def testProgressWith0(capsys):
    progress(0, 10)
    captured = capsys.readouterr()
    assert captured.out == "Uploaded 0 of 10 bytes.\n"