import tkinter as tk#导入tkinter库 并把tkinter变成tk
import easygui as gui#导入easygui库 并把easygui变成gui
from easygui import *#导入easygui里面的所有模块
from tkinter import *#导入tkinter库里面的所有模块
import os
os.system("start welcome.vbs")#欢迎提示音
root = tk.Tk()
root.title("Windows实用小工具 Powered by 2096779623")#设置title
root.geometry("1900x1000")#设置窗口大小
root.resizable(width=True, height=True)#设置窗口大小可以被更改
root.iconbitmap(".\\ico.ico")#设置图标
gui.msgbox(msg="请不要在带有终端的代码编辑器或运行器打开命令窗口 如VS CODE 不然会无响应!",title="温馨提示",ok_button="确定")#弹窗提示
#下面是框架部分
def guanyu():
    gui.buttonbox("作者QQ:2096779623",choices=("确定","确定","确定","确定","确定","确定"))#弹窗提示
def help():
    gui.msgbox(msg="想要执行什么功能请按对应的按钮  不会的就百度！",title="帮助",ok_button="确定")#弹窗提示
def jsq():
    os.system("calc.exe")
def pmjp():
    os.system("start osk.exe")
def zcb():
    os.system("regedit")
def zcl():
    gui.msgbox(msg="Windows10家庭版没有组策略!按确定继续打开",title="提示",ok_button="确定")
    os.system("gpedit.msc")
def cmd():
    os.system("start cmd")
def powershell():
    os.system("start powershell")
def winversion():
    os.system("start winver")
def UAC():
    os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f ")
    gui.msgbox(msg="操作成功完成! 请重启你的电脑生效",title="提示",ok_button="确定")
def systeminfo():
    os.system("start msinfo32")
def mstsc():
    os.system("mstsc")
def taskmgr():
    os.system("start taskmgr")
def ip():
    os.system("ipconfig /all >> IP.txt")
    os.system("start ip.txt")
    gui.msgbox(msg="生成的文件请手动删除!  文件名为:IP.txt",title="提示",ok_button="确定")
def jh():
    gui.msgbox(msg="这是使用KMS激活方式激活的 继续吗？",title="提示",ok_button="继续")
    os.system("slmgr /skms kms.v0v.bid && slmgr /ato && slmgr.vbs /xpr")
def bluescreen():
    os.system("start .\\bluescreen.bat")
def notepad():
    os.system("start notepad.exe")
def fdj():
    os.system("start Magnify.exe")
def username():
    os.system("start username.bat")
def shutdown():
    os.system("shutdown -s -t 0")
def xiumian():
    os.system("powerctf -h on")
    os.system("shutdown -h")
def sbglq():
    os.system("hdwwiz.cpl")
def xtsx():
    os.system("control.exe system")
def sjckq():
    os.system("eventvwr.exe")
def iexx():
    os.system("inetcpl.cpl")
def xnjsq():
    os.system("perfmon.exe")
def zyjsq():
    os.system("resmon.exe")
def cpql():
    os.system("cleanmgr /sagerun:99")
def draw():
    os.system("start mspaint.exe")
def gn():
    os.system("start OptionalFeatures.exe")
def services():
    os.system("start services.msc")
def slidetoshutdown():
    os.system("start slidetoshutdown.exe")
#下面五行是菜单部分
menubar = tk.Menu(root)
menubar.add_command(label=u"帮助", command=help)#创建菜单
menubar.add_command(label=u"关于", command=guanyu)#创建菜单
menubar.add_command(label=u"退出", command=root.quit)#创建菜单
root.config(menu=menubar)#让菜单显示出来
#下面是按钮部分
#text是设置文字 
#command是设置函数  
#grid设置间距
Button (root, text="计算器",command=jsq).grid(row=1, columnspan=1, pady=1)
Button (root, text="屏幕键盘",command=pmjp).grid(row=2, columnspan=1, pady=1)
Button (root, text="注册表",command=zcb).grid(row=3, columnspan=1, pady=1)
Button (root, text="组策略",command=zcl).grid(row=4, columnspan=1, pady=1)
Button (root, text="CMD命令提示符",command=cmd).grid(row=5, columnspan=1, pady=1)
Button (root, text="powershell",command=powershell).grid(row=6, columnspan=1, pady=1)
Button (root, text="显示windows版本信息",command=winversion).grid(row=7, columnspan=1, pady=1)
Button (root, text="关闭UAC提示框",command=UAC).grid(row=8, columnspan=1, pady=1)
Button (root, text="查看系统信息",command=systeminfo).grid(row=9, columnspan=1, pady=1)
Button (root, text="远程桌面连接",command=mstsc).grid(row=10, columnspan=1, pady=1)
Button (root, text="任务管理器",command=taskmgr).grid(row=11, columnspan=1, pady=1)
Button (root, text="IP信息",command=ip).grid(row=12, columnspan=1, pady=1)
Button (root, text="一键激活Windows",command=jh).grid(row=13, columnspan=1, pady=1)
Button (root, text="蓝屏",command=bluescreen).grid(row=14, columnspan=1, pady=1)
Button (root, text="记事本",command=notepad).grid(row=15, columnspan=1, pady=1)
Button (root, text="放大镜",command=fdj).grid(row=16, columnspan=1, pady=1)
Button (root, text="查看当前用户名",command=username).grid(row=17, columnspan=1, pady=1)
Button (root, text="关机",command=shutdown).grid(row=18, columnspan=1, pady=1)
Button (root, text="休眠",command=xiumian).grid(row=19, columnspan=1, pady=1)
Button (root, text="设备管理器",command=sbglq).grid(row=20, columnspan=1, pady=1)
Button (root, text="系统属性",command=xtsx).grid(row=21, columnspan=2, pady=1)
Button (root, text="事件查看器",command=sjckq).grid(row=22,columnspan=2,pady=1)
Button (root, text="Internet选项",command=iexx).grid(row=23,columnspan=2,pady=1)
Button (root, text="性能监视器",command=xnjsq).grid(row=24,columnspan=2,pady=1)
Button (root, text="资源监视器",command=zyjsq).grid(row=25,columnspan=2,pady=1)
Button (root, text="磁盘清理",command=cpql).grid(row=26,columnspan=2,pady=1)
Button (root, text="画图", command=draw).grid(row=27,columnspan=2,pady=1)
Button (root, text="启用或关闭Windows功能",command=gn).grid(row=28,columnspan=2,pady=1)
Button (root, text="服务",command=services).grid(row=29,columnspan=2,pady=1)
Button (root, text="滑动关机(Windows10)",command=slidetoshutdown).grid(row=30,columnspan=2,pady=1)
root.mainloop()#消息循环 让界面显示出来
