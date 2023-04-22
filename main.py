import os
import shutil
import subprocess


def convertBackSlash(string):
    return string.replace("\\", "/")

def copyFile(origin, dst):
    listWayDst = dst.split('/')

    wayDst = listWayDst.pop(-1)
    if os.path.isdir(wayDst):
        os.mkdir()

    shutil.copy(origin, dst)

def deleteFile(file):
    os.remove(file)


def writeFileBatCopy(name, origin, dest='/'):
    script = f'@echo off\nif not exist TCLE_HEMATO.pdf (\nxcopy "{origin}"\n) else (\n   echo.\n   )'

    with open(name+'.bat', 'w') as f:
        f.write(script)

def executeFileCode(file, type=''):
    if type != '':
        subprocess.call([f'{type}', f'{file}'])
    else:
        subprocess.call([f'{file}'])
