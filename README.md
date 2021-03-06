﻿# Show_Img_in_PC_from_OpenMV_by_UART #  
（OpenMV通过串口传送图片到电脑并显示）  
欢迎大家参考本程序，本程序在OpenMV2 with Window7上测试成功。STM32F4串口最大波特率为921600，在这个波特率下，OpenMV压缩图片质量为90，传送的FPS高于30，可以正常使用。以下是使用本程序需要注意的事项。  

## 配置环境 ##
OpenMV上运行的程序无需额外的模块，PC上运行程序需要opencv等模块的支持。

1. 在PC上安装python：（以我自己环境为例，其他版本自己尝试）  
下载：https://www.python.org/downloads/release/python-2714/  
下载好自己PC对应的安装包，安装时记得勾选上pip工具。  
2. 在PC上安装python串口模块pyserial：
按下Window+R打开运行，输入cmd回车打开CMD窗口，切换目录到python安装目录\Scripts，输入 pip install pyserial[回车]。  
NOTE：CMD中切换盘符，直接输入盘符，例如切换到D盘 D:[回车]，切换目录使用 cd 命令，使用TAB键可以补全命令或名称。  
3. 在PC上安装numpy方法和serial相同。输入 pip install numpy[回车]。  
4. 在PC上安装opencv：  
下载：https://opencv.org/releases.html  
下载2.4版本的windows安装包。直接运行，你会发现是一个解压文件的窗口，随便选择一个目录解压（解压文件安装完毕可以删除），过程中会自动配置环境变量。然后是最重要的，复制解压目录下\build\python\2.7\x64\cv2.pyd 到 python安装目录\Lib\site-packages文件夹里。

如果你顺利执行了以上操作，那么恭喜你PC环境配置完成。你可以在CMD中输入 python[回车]，进入python命令行，此时命令行开头变为>>，然后依次输入 import serial[回车],import numpy[回车],import cv2[回车],如果没有任何提示信息说明安装成功！   
NOTE:有些人可能不习惯没有提示信息，但是，如果你喜欢用python就要习惯“没有提示消息就是最好的消息”这一特点（当然如果你非要输出信息也是可以设置的）。python开发者在开发这门语言时结合了UNIX shell和C语言的习惯，而不提示信息就是UNIX shell的一种哲学思想。

## 如何使用两个python脚本
1. 由于PC的脚本进行了头帧检测，所以先运行PC脚本或者OpenMV脚本都可以。  
2. 有关于串口，PC脚本进行了串口检测，当你正确连接串口，脚本会自动检测并连接，不用改动串口号。OpenMV串口固定为UART3，管脚查询商家提供的管脚图。  
3. 运行过程中，当图片显示窗口位于所有窗口顶端时，按q退出PC端程序。
---
欢迎大家参考和提出建议或意见！
se7en 2018年4月17日 交流QQ群：凡哥OpenMV广场群 564048763