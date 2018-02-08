#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import argparse
import subprocess


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\33[93m'
    WARNING = '\033[91m'
    FAIL = '\033[35m'
    ENDC = '\033[0m'


class Tools:
    def __init__(self):
        self.apktool = '2.3.1'
        self.smali = '2.2.2'
        self.baksmali = '2.2.2'
        self.dex2jar = '2.1'
        self.jd_gui = '1.4.0'
        self.jadx = '0.7.0'

    def list_all_member(self):
        print(Color.OKGREEN + "Tool's version:" + Color.ENDC)
        for name, value in vars(self).items():
            print('  %s : %s' % (name, value))
        print(" ")


class BombAPK(object):
    def __init__(self, ToolID, Input, Output):
        self.ToolID = ToolID
        self.Input = Input
        self.Output = Output
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
        # 输入信息
        if self.Input != None:
            print(Color.HEADER +
                  "[+] BombBombAPK ready to start." + Color.ENDC)
            print(Color.OKBLUE +
                  "[+] Current command's input: " + self.Input + Color.ENDC)
        if self.Output != None:
            print(Color.OKBLUE +
                  "[+] Current command's output: " + self.Output + Color.ENDC)
        # 工具调用
        if self.ToolID == "0":
            print(Color.WARNING +
                  "[-] The specified tool ID number" + Color.ENDC)
            print(Color.WARNING +
                  "[-] Please look at the help document [-h]" + Color.ENDC)
        elif self.ToolID == "1":
            tool = sys.path[0] + "/bin/apktool.jar"
            if self.Output != None:
                cmd = "java -jar " + tool + " d -f " + self.Input + " -o " + self.Output
            else:
                cmd = "java -jar " + tool + " d -f " + \
                    self.Input + " -o " + self.Input[:-4] + "-debug"
            self.run(cmd)
        elif self.ToolID == "2":
            tool = sys.path[0] + "/bin/apktool.jar"
            if self.Output != None:
                cmd = "java -jar " + tool + " b " + self.Input + " -o " + self.Output
            else:
                cmd = "java -jar " + tool + " b " + \
                    self.Input + " -o " + self.Input[:-6] + "-debug.apk"
            self.run(cmd)
        elif self.ToolID == "3":
            tool = sys.path[0] + "/bin/signapk"
            if self.Output != None:
                cmd = "java -jar " + tool + "/signapk.jar " + tool + "/testkey.x509.pem " + tool + "/testkey.pk8 " + \
                    self.Input + " " + self.Output
            else:
                cmd = "java -jar " + tool + "/signapk.jar " + tool + "/testkey.x509.pem " + tool + "/testkey.pk8 " + \
                    self.Input + " " + self.Input[:-4] + "-S.apk"
            self.run(cmd)
        elif self.ToolID == "4":
            if self.Output != None:
                cmd = "unzip " + self.Input + " classes.dex -d " + self.Output
            else:
                cmd = "unzip " + self.Input + \
                    " classes.dex -d " + self.Input[:-4] + "-dex"
            self.run(cmd)
        elif self.ToolID == "5":
            tool = sys.path[0] + "/bin/dex2jar/d2j-dex2jar.sh"
            if self.Output != None:
                cmd = "bash " + tool + " --force " + \
                    self.Input + " -o " + self.Output
            else:
                cmd = "bash " + tool + " --force " + \
                    self.Input + " -o " + self.Input[:-4] + ".jar"
            self.run(cmd)
        elif self.ToolID == "6":
            tool = sys.path[0] + "/bin/jd-gui.jar"
            cmd = "java -jar " + tool + " " + self.Input
            self.run(cmd)
        elif self.ToolID == "7":
            tool = sys.path[0] + "/bin/zipalign"
            if self.Output != None:
                cmd = tool + " -f -v 4 " + \
                    self.Input + " " + self.Output
            else:
                cmd = tool + " -f -v 4 " + \
                    self.Input + " " + self.Input[:-4] + "-Z.apk"
            self.run(cmd)
        elif self.ToolID == "8":
            tool = sys.path[0] + "/bin/jadx/bin/jadx"
            if self.Output != None:
                cmd = tool + " " + self.Input + " -d " + self.Output
            else:
                cmd = tool + " " + self.Input + \
                    " -d " + self.Input[:-4] + "-java"
            self.run(cmd)
        elif self.ToolID == "9":
            tool = sys.path[0] + "/bin/jadx/bin/jadx"
            if self.Output != None:
                cmd = tool + " -e " + self.Input + " -d " + self.Output
            else:
                cmd = tool + " -e " + self.Input + \
                    " -d " + self.Input[:-4] + "-gradle"
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
    
    Usage: python BombAPK.py [-h] -t[ToolID] -i[Input] [options]
    -t [ToolID] List:
            1 = apktool d
            2 = apktool b
            3 = signapk
            4 = classes.dex
            5 = dex2jar
            6 = jd-gui
            7 = zipalign
            8 = jadx dex2java
            9 = jadx Gradle
            10 = AmStart
            11 = Unicode
    '''
    print(Color.OKYELLOW + banner + Color.ENDC)
    parser = argparse.ArgumentParser(
        description="Some common assembler / disassembler tools in Android development")
    # 可选参数
    parser.add_argument('-t', '--tool', dest="ToolID",
                        help="Selectable tools", type=str, choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], default='0')
    parser.add_argument('-i', '--input', dest="Input",
                        help="Source file or source directory", type=str)
    parser.add_argument('-o', '--output', dest="Output",
                        help="Destination file or destination directory", type=str)
    # 所有工具的版本号
    parser.add_argument('-v', '--version', dest="Version",
                        help="The current version number of all the tools", action="store_true")
    args = parser.parse_args()
    bombapk = BombAPK(args.ToolID, args.Input, args.Output)
    if args.Version:
        Tools().list_all_member()
    bombapk.main()
