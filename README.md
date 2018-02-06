# BombAPK

此脚本使用Python集成了Android逆向中常用的一些工具，力求省去各自繁琐的命令，方便自写脚本的整合，最终在一个终端下完成各种工具的调用。

### 工具

- APK反编译：apktool d
- 回编译APK：apktool b
- APK签名：signapk
- 提取dex：unzip
- dex转jar：dex2jar
- JAVA反编译：jd-gui
- APK优化：zipalign
- 入口Activity：AmStart

### 使用

查看帮助文档：

```
[Go0s]: ~/Desktop/BombAPK ✗ master
➜  python BombAPK.py -h

      /\_/\          ____                  _       _    ____  _  __
    =( °w° )=       | __ )  ___  _ __ ___ | |__   / \  |  _ \| |/ /
   . ((   )) .      |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ | |_) | ' / 
  \  )   (  //      | |_) | (_) | | | | | | |_) / ___ \|  __/| . \ 
   \(__ __)//       |____/ \___/|_| |_| |_|_.__/_/   \_\_|   |_|\_\
    
    Usage: python BombAPK.py [-h] -t[ToolID] -i[Input] [options]
    -t [ToolID] List:
            1 = apktool d
            2 = apktool b
            3 = signapk
            4 = classes.dex
            5 = dex2jar
            6 = jd-gui
            7 = zipalign
            10 = AmStart
    
usage: BombAPK.py [-h] [-t {0,1,2,3,4,5,6,7,10}] [-i INPUT] [-o OUTPUT] [-v]

Some common assembler / disassembler tools in Android development

optional arguments:
  -h, --help            show this help message and exit
  -t {0,1,2,3,4,5,6,7,10}, --tool {0,1,2,3,4,5,6,7,10}
                        Selectable tools
  -i INPUT, --input INPUT
                        Source file or source directory
  -o OUTPUT, --output OUTPUT
                        Destination file or destination directory
  -v, --version         The current version number of all the tools
```

查看其中工具的版本号：

```
[Go0s]: ~/Desktop/BombAPK ✗ master
➜  python BombAPK.py -v
dex2jar : 2.1
jd_gui : 1.4.0
smali : 2.2.2
baksmali : 2.2.2
apktool : 2.3.1
[-] The specified tool ID number
[-] Please look at the help document [-h]
```

