from utils.miscFuncs import uploadProgress


def testUploadProgressWithRegularValues():
    assert uploadProgress(1, 10) == (1, 10)
    assert uploadProgress(256, 512) == (256, 512)
    assert uploadProgress(111222333, 999888777) == (111222333, 999888777)


def testUploadProgressWithIrregularValues():
    assert uploadProgress(24, 12) == (24, 12)
    assert uploadProgress(999888777, 111222333) == (999888777, 111222333)


def testUploadProgressWith0():
    assert uploadProgress(0, 10) == (0, 10)