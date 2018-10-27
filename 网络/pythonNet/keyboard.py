#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import  os  
import  sys
import  tty, termios
import time    

if __name__ == '__main__':
    print ("Reading form keybord")
    print ("""   i
j  k  l
   m""")
    print ('press Q to quit')
    while True:
        fd=sys.stdin.fileno()
        old_settings=termios.tcgetattr(fd)
        #old_settings[3]= old_settings[3] & ~termios.ICANON & ~termios.ECHO  
        try:#整形文件描述符
            tty.setraw(fd)
            ch=sys.stdin.read(1)#标准化输出 跟input 差不多　
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  
            #print 'error'
        if ch=='i':
            print ('move forward')
        elif ch=='m':
            print ('move back')
        elif ch=='a':
            print ("turn left!")
        elif ch=='s':
            print ("turn down!")
        elif ch=='d':
            print ("turn right!")
        elif ch=='w':
            print ("turn on!")
        elif ch=='k':
            print ("stop motor!")
        elif ch=='q':
            print ("shutdown!")
            break
        elif ord(ch)==0x3:
            #这个是ctrl c
            print ('shutdown')
            break
        print ("Reading form keybord")
        print ("""   i
j  k  l
   m""")
        print ('press Q or ctrl+c to quit')
        #rate.sleep()


