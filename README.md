# BombAPK

此脚本使用Python集成了Android逆向中常用的一些工具，力求省去各自繁琐的命令，方便自写脚本的整合，最终在一个终端下完成各种工具的调用。

## 工具

- APK反编译：apktool d
- 回编译APK：apktool b
- APK签名：signapk
- 提取dex：unzip
- dex转jar：dex2jar
- JAVA反编译：jd-gui
- APK优化：zipalign
- 入口Activity：AmStart
- Unicode互转汉字：Unicode

## 使用

只需要记住2-3个参数即可，当然也可以使用快速版脚本，见最后：

`-t`：指定利用工具的ID

`-i`：指定输入的文件或目录

`-o`：指定输出的文件或目录（自带默认）

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
            11 = Unicode
    
usage: BombAPK.py [-h] [-t {0,1,2,3,4,5,6,7,10,11}] [-i INPUT] [-o OUTPUT]
                  [-v]

Some common assembler / disassembler tools in Android development

optional arguments:
  -h, --help            show this help message and exit
  -t {0,1,2,3,4,5,6,7,10,11}, --tool {0,1,2,3,4,5,6,7,10,11}
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

APK反编译：

```
[Go0s]: ~/Desktop/BombAPK ✗ master
➜  python BombAPK.py -t 1 -i crackme.apk 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: java -jar /Users/Go0s/Desktop/BombAPK/bin/apktool.jar d -f crackme.apk -o crackme-debug
I: Using Apktool 2.3.1 on crackme.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /Users/Go0s/Library/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
[+] This command completed execution.
```

回编译APK：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 2 -i crackme-debug 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme-debug
[+] Current command: java -jar /Users/Go0s/OtherAPP/Git/BombAPK/bin/apktool.jar b crackme-debug -o crackme-debug.apk
I: Using Apktool 2.3.1
I: Checking whether sources has changed...
I: Smaling smali folder into classes.dex...
I: Checking whether resources has changed...
I: Building resources...
I: Building apk file...
I: Copying unknown files/dir...
[+] This command completed execution.
```

APK签名：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 3 -i crackme.apk 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: java -jar /Users/Go0s/Desktop/BombAPK/bin/signapk/signapk.jar /Users/Go0s/Desktop/BombAPK/bin/signapk/testkey.x509.pem /Users/Go0s/Desktop/BombAPK/bin/signapk/testkey.pk8 crackme.apk crackme-S.apk
[+] This command completed execution.
```

提取dex：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 4 -i crackme.apk 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: unzip crackme.apk classes.dex -d crackme-dex
Archive:  crackme.apk
  inflating: crackme-dex/classes.dex  
[+] This command completed execution.
```

dex转jar：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 5 -i crackme-dex/classes.dex 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme-dex/classes.dex
[+] Current command: bash /Users/Go0s/OtherAPP/Git/BombAPK/bin/dex2jar/d2j-dex2jar.sh --force crackme-dex/classes.dex -o crackme-dex/classes.jar
dex2jar crackme-dex/classes.dex -> crackme-dex/classes.jar
[+] This command completed execution.
```

JAVA反编译：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 6 -i crackme-dex/classes.jar 
[+] BombBombAPK ready to start.
[+] Current command's input: crackme-dex/classes.jar
[+] Current command: java -jar /Users/Go0s/OtherAPP/Git/BombAPK/bin/jd-gui.jar crackme-dex/classes.jar
[+] This command completed execution.
```

APK优化：

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 7 -i crackme.apk
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: /Users/Go0s/OtherAPP/Git/BombAPK/bin/zipalign -f -v 4 crackme.apk crackme-Z.apk
Verifying alignment of crackme-Z.apk (4)...
      62 res/layout/activity_main.xml (OK - compressed)
     554 res/menu/main.xml (OK - compressed)
     865 AndroidManifest.xml (OK - compressed)
    1544 resources.arsc (OK)
    3996 res/drawable-hdpi/background.png (OK)
    9676 res/drawable-hdpi/ic_launcher.png (OK)
   15704 res/drawable-mdpi/ic_launcher.png (OK)
   18880 res/drawable-xhdpi/ic_launcher.png (OK)
   28300 res/drawable-xxhdpi/ic_launcher.png (OK)
   46230 classes.dex (OK - compressed)
  283646 META-INF/MANIFEST.MF (OK - compressed)
  284138 META-INF/CERT.SF (OK - compressed)
  284662 META-INF/CERT.RSA (OK - compressed)
Verification succesful
[+] This command completed execution.
```

入口Activity：调用aapt

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  python BombAPK.py -t 10 -i crackme.apk
[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: bash /Users/Go0s/OtherAPP/Git/BombAPK/bin/AmStart crackme.apk
adb shell am start -D -n com.mzheng.crackme/com.mzheng.crackme.MainActivity
[+] This command completed execution.
```

Unicode转汉字：终端下反斜线属于转义符，输入Unicode时记得引号

```
[Go0s]: ~/Desktop/BombAPK ✗ master
➜  python BombAPK.py -t 11 -i "\u6d4b\u8bd5"
[+] BombBombAPK ready to start.
[+] Current command's input: \u6d4b\u8bd5
[!] Unicode to Chinese, pay attention to quotation marks
测试
```

汉字转Unicode：

```
[Go0s]: ~/Desktop/BombAPK ✗ master
➜  python BombAPK.py -t 11 -i 测试 
[+] BombBombAPK ready to start.
[+] Current command's input: 测试
[!] Unicode to Chinese, pay attention to quotation marks
\u6d4b\u8bd5
```

## 快速版

**BombAPK_argv.py** 脚本并未采用 `argparse` 模块，而是直接使用 `sys.argv[]` 来获取参数；

同时删去了帮助文档以及自定义输出的功能，直接采用默认输出；

```
python BombAPK_argv.py 1 crackme.apk
python BombAPK_argv.py 2 crackme-debug
python BombAPK_argv.py 3 crackme-debug.apk
python BombAPK_argv.py 4 crackme.apk
python BombAPK_argv.py 5 crackme-dex/classes.dex
python BombAPK_argv.py 6 crackme-dex/classes.jar
python BombAPK_argv.py 7 crackme.apk
python BombAPK_argv.py 10 crackme.apk
python BombAPK_argv.py 11 "\u6d4b\u8bd5"
python BombAPK_argv.py 11 测试
```

将脚本 **软连接** 到环境变量自定义目录下，去掉.py后缀，赋予执行权限，方便全局调用；当然也可以重名了为简单好记的命令名字，如：apk

```
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  ln -s /Users/Go0s/Desktop/BombAPK/BombAPK_argv.py /Users/Go0s/OtherAPP/bin/apk
[Go0s]: ~/Desktop/BombAPK ✗ master*
➜  cd /Users/Go0s/OtherAPP/bin 
[Go0s]: ~/OtherAPP/bin 
➜  chmod +x apk
[Go0s]: ~/OtherAPP/bin 
➜  l apk
lrwxr-xr-x  1 Go0s  staff    43B  2  7 20:41 apk -> /Users/Go0s/Desktop/BombAPK/BombAPK_argv.py
```

有多简单好记？只需要提供工具ID和输入。

```
[Go0s]: ~/Desktop/apk 
➜  apk 1 crackme.apk 

      /\_/\          ____                  _       _    ____  _  __
    =( °w° )=       | __ )  ___  _ __ ___ | |__   / \  |  _ \| |/ /
   . ((   )) .      |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ | |_) | ' / 
  \  )   (  //      | |_) | (_) | | | | | | |_) / ___ \|  __/| . \ 
   \(__ __)//       |____/ \___/|_| |_| |_|_.__/_/   \_\_|   |_|\_\
    
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
    

[+] BombBombAPK ready to start.
[+] Current command's input: crackme.apk
[+] Current command: java -jar /Users/Go0s/Desktop/BombAPK/bin/apktool.jar d -f crackme.apk -o crackme-debug
I: Using Apktool 2.3.1 on crackme.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /Users/Go0s/Library/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
[+] This command completed execution.
```

