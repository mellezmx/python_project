#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mellezmx
#
# Created:     06/01/2022
# Copyright:   (c) mellezmx 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import subprocess

def main():
    with open('outpout.txt') as f:
        subprocess.run('dir', shell=True, stdout=f, text=True)


if __name__ == '__main__':
    main()
