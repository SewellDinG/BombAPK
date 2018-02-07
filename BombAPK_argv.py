#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import subprocess


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\33[93m'
    WARNING = '\033[91m'
    FAIL = '\033[35m'
    ENDC = '\033[0m'


class BombAPK(object):
    def __init__(self, ToolID, Input):
        self.ToolID = ToolID
        self.Input = Input
        self.flag = 0

    def run(self, cmd):
        print(Color.OKBLUE + "[+] Current command: " + cmd + Color.ENDC)
        subprocess.call(cmd, shell=True)
        # try捕捉处理异常
        self.flag = 1

    def u2c(self, ustr):
        self.ustr = ustr
        print(self.ustr.encode('utf-8').decode('unicode_escape'))

    def c2u(self, cstr):
        self.cstr = cstr
        print(self.cstr.decode('utf-8').encode('unicode_escape'))

    def main(self):
        print
        # 输入信息
        if self.Input != None:
            print(Color.HEADER +
                  "[+] BombBombAPK ready to start." + Color.ENDC)
            print(Color.OKBLUE +
                  "[+] Current command's input: " + self.Input + Color.ENDC)
        # 工具调用
        if self.ToolID == "1":
            tool = sys.path[0] + "/bin/apktool.jar"
            cmd = "java -jar " + tool + " d -f " + \
                self.Input + " -o " + self.Input[:-4] + "-debug"
            self.run(cmd)
        elif self.ToolID == "2":
            tool = sys.path[0] + "/bin/apktool.jar"
            cmd = "java -jar " + tool + " b " + self.Input + \
                " -o " + self.Input[:-6] + "-debug.apk"
            self.run(cmd)
        elif self.ToolID == "3":
            tool = sys.path[0] + "/bin/signapk"
            cmd = "java -jar " + tool + "/signapk.jar " + tool + "/testkey.x509.pem " + \
                tool + "/testkey.pk8 " + self.Input + \
                " " + self.Input[:-4] + "-S.apk"
            self.run(cmd)
        elif self.ToolID == "4":
            cmd = "unzip " + self.Input + \
                " classes.dex -d " + self.Input[:-4] + "-dex"
            self.run(cmd)
        elif self.ToolID == "5":
            tool = sys.path[0] + "/bin/dex2jar/d2j-dex2jar.sh"
            cmd = "bash " + tool + " --force " + \
                self.Input + " -o " + self.Input[:-4] + ".jar"
            self.run(cmd)
        elif self.ToolID == "6":
            tool = sys.path[0] + "/bin/jd-gui.jar"
            cmd = "java -jar " + tool + " " + self.Input
            self.run(cmd)
        elif self.ToolID == "7":
            tool = sys.path[0] + "/bin/zipalign"
            cmd = tool + " -f -v 4 " + self.Input + \
                " " + self.Input[:-4] + "-Z.apk"
            self.run(cmd)
        elif self.ToolID == "10":
            tool = sys.path[0] + "/bin/AmStart"
            cmd = "bash " + tool + " " + self.Input
            self.run(cmd)
        elif self.ToolID == "11":
            ucstr = self.Input
            print(Color.WARNING +
                  "[!] Unicode to Chinese, pay attention to quotation marks" + Color.ENDC)
            if "\\" in ucstr:
                self.u2c(ucstr)
            else:
                self.c2u(ucstr)
        # 结束提示
        if self.flag == 1:
            print(Color.HEADER +
                  "[+] This command completed execution." + Color.ENDC)


if __name__ == '__main__':
    banner = '''\

      /\_/\          ____                  _       _    ____  _  __
    =( °w° )=       | __ )  ___  _ __ ___ | |__   / \  |  _ \| |/ /
   . ((   )) .      |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ | |_) | ' / 
  \\  )   (  //      | |_) | (_) | | | | | | |_) / ___ \|  __/| . \ 
   \\(__ __)//       |____/ \___/|_| |_| |_|_.__/_/   \_\_|   |_|\_\\
    
    Usage: python BombAPK.py [ToolID] [Input]
    ToolID List:
            1 = apktool d
            2 = apktool b
            3 = signapk
            4 = classes.dex
            5 = dex2jar
            6 = jd-gui
            7 = zipalign
            10 = AmStart
            11 = Unicode
    '''
    print(Color.OKYELLOW + banner + Color.ENDC)
    try:
        ToolID = sys.argv[1]
        Input = sys.argv[2]
    except IndexError:
        ToolID = "0"
        Input = "0"
        print(Color.WARNING +
              "[!] Please enter the ID tools and source files." + Color.ENDC)
    # print ToolID, Input
    bombapk = BombAPK(ToolID, Input)
    bombapk.main()
