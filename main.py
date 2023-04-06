import os
import shutil
import time

src_file = 'prova01-T3-sol.pdf'
dst_file = 'teste/prova01-T3-sol.pdf'


def copyFile(origem, dst):
    listWayDst = dst.split('/')

    wayDst = listWayDst.pop(-1)
    if os.path.isdir(wayDst):
        os.mkdir()

    shutil.copy(origem, dst)

def deleteFile(file):
    os.remove(file)


copyFile(src_file, dst_file)
time.sleep(10)
deleteFile(dst_file)
