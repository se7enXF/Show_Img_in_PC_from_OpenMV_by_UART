# -*- coding: utf-8 -*
'''
OpenMV串口接收图片数据，PC端程序
作者：se7en,凡哥
2018年4月20日 14:54:27
凡哥OpenMV广场QQ群：564048763
'''

import serial
import serial.tools.list_ports
import numpy as np
import cv2

pic_dir = "F:\\"
port_list = list(serial.tools.list_ports.comports())
#获取串口信息
if len(port_list) <= 0:  
    print("The Serial port can't find!")
else:
    port_list_0 =list(port_list[0])                     #第一个串口
    port_serial = port_list_0[0]                        #串口号
    ser = serial.Serial(port_serial,921600,timeout=0.5)
    ser.bytesize=8                                      #8位字符
    ser.stopbits=1                                      #1位停止位                        
    print("Waiting data from:"+ser.name)
    print("Plot the image window.Receiving data...")
    cv2.namedWindow('OpenMV Image',flags=cv2.WINDOW_NORMAL |
                     cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
    cv2.resizeWindow('OpenMV Image', 160*4,120*4)       #图片放大4倍
    cv2.moveWindow('OpenMV Image',100,100)
    
    while(1):
        head = ser.readline()
        #读取数据头帧，以\n换行结束
        if head == "" or len(head)<15 or head[-15:-12] != "$7$":
            img_t = cv2.imread("wait.jpg")
            cv2.imshow('OpenMV Image',img_t)
            k = cv2.waitKey(20)
            if k == ord('q'):
                cv2.destroyWindow('OpenMV Image')
                break
            continue
        
        pic_W    = int(head[-12:-9])    #图像宽度
        pic_H    = int(head[-9:-6])     #图像高度
        pic_F    = int(head[-6])        #图像类型
        pic_size = int(head[-5:])       #图像大小
        
        if pic_F == 1:
            cv2_formate = cv2.IMREAD_COLOR
        else:
            if pic_F == 3:
                cv2_formate = cv2.IMREAD_GRAYSCALE
            else:
                print("Wrong picture formate.")
                
        data = ''
        data = ser.read(pic_size+2)
        #2种读取串口方法，上面是读取固定长度
        #下面是“直到特征值”形读取方法
        #data = ser.read_until("$",pic_size+2)
        
        if(data[0] != "$" or data[-1] != "$"):
            print("wrong picture data!")
            continue
        if data!="":
            #将图片保存到本地
            '''
            with open(pic_dir+"pic.jpeg","wb") as f:
                f.write(data[1:-1])
                print("picture saved.")
                print(time.strftime('%H:%M:%S',time.localtime(time.time())))
            '''
            img_arr = np.fromstring(data[1:-1], np.uint8)
            img = cv2.imdecode(img_arr,cv2_formate)
            cv2.imshow('OpenMV Image',img)
            #或者使用cv2.imwrite(pic_dir+"pic.jpeg", img)保存图像
        else:
            print("Read data wrong.")
        #按q键退出程序
        k = cv2.waitKey(20)
        if k == ord('q'):
            cv2.destroyWindow('OpenMV Image')
            break
 

       
    
