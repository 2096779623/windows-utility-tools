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
def memu():
    pass
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
def yhwjj():
    os.system("start explorer C:\\Users\\%username%")
def dsgj():
    os.system("start dsgj.bat")
def jsjgl():
    os.system("start compmgmt.msc")
#下面是菜单部分
menubar = tk.Menu(root)
# 创建一个子菜单
gongneng = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"1~10", menu=gongneng)
gongneng.add_command(label=u"计算器", command=jsq)
gongneng.add_command(label=u"屏幕键盘", command=pmjp)
gongneng.add_command(label=u"注册表", command=zcb)
gongneng.add_command(label=u"组策略", command=zcl)
gongneng.add_command(label=u"命令提示符", command=cmd)
gongneng.add_command(label=u"powershell", command=powershell)
gongneng.add_command(label=u"显示Windows版本信息", command=winversion)
gongneng.add_command(label=u"查看系统信息", command=systeminfo)
gongneng.add_command(label=u"远程连接", command=mstsc)
gongneng.add_command(label=u"关闭UAC", command=UAC)
gongneng.add_separator()
gongneng1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"10~20", menu=gongneng1)
gongneng1.add_command(label=u"任务管理器", command=taskmgr)
gongneng1.add_command(label=u"显示IP信息", command=ip)
gongneng1.add_command(label=u"一键激活Windows", command=jh)
gongneng1.add_command(label=u"蓝屏", command=bluescreen)
gongneng1.add_command(label=u"记事本", command=notepad)
gongneng1.add_command(label=u"放大镜", command=fdj)
gongneng1.add_command(label=u"查看当前用户名", command=username)
gongneng1.add_command(label=u"关机", command=shutdown)
gongneng1.add_command(label=u"休眠", command=xiumian)
gongneng1.add_command(label=u"计算机管理", command=jsjgl)
gongneng1.add_separator()
gongneng2 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"20~30", menu=gongneng2)
gongneng2.add_command(label=u"系统属性", command=xtsx)
gongneng2.add_command(label=u"事件查看器", command=sjckq)
gongneng2.add_command(label=u"Internet选项", command=iexx)
gongneng2.add_command(label=u"性能监视器", command=xnjsq)
gongneng2.add_command(label=u"资源监视器", command=zyjsq)
gongneng2.add_command(label=u"磁盘清理", command=cpql)
gongneng2.add_command(label=u"画图", command=draw)
gongneng2.add_command(label=u"启用或关闭Windows功能", command=gn)
gongneng2.add_command(label=u"服务", command=services)
gongneng2.add_command(label=u"滑动关机", command=slidetoshutdown)
gongneng2.add_separator()
menubar.add_command(label=u"帮助", command=help)#创建菜单
menubar.add_command(label=u"关于", command=guanyu)#创建菜单
menubar.add_command(label=u"退出", command=root.quit)#创建菜单
root.config(menu=menubar)#让菜单显示出来
#下面是文字部分
#text是设置文字 
Label(root,
                      text='欢迎使用Windows实用小工具!',
                      compound=CENTER,  # 混合模式,文字在图片的正上方显示
                      font=("微软雅黑", 50),  # 字体和大小
                      fg='blue'  # 前景颜色，就是字体颜色
                      ).pack()


Label(root,
                      text='Powered By 2096779623!',
                      compound=CENTER,  # 混合模式,文字在图片的正上方显示
                      font=("微软雅黑", 50),  # 字体和大小
                      fg='red'  # 前景颜色，就是字体颜色
                      ).pack()
root.mainloop()#消息循环 让界面显示出来
