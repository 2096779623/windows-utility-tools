import tkinter as tk#导入tkinter库 并把tkinter变成tk
import easygui as gui#导入easygui库 并把easygui变成gui
from easygui import *#导入easygui里面的所有模块
from tkinter import *#导入tkinter库里面的所有模块
import os
import pyautogui #导入pyautogui库
os.system("start welcome.vbs")#欢迎提示音
root = tk.Tk()
root.title("Windows实用小工具 Powered by 2096779623")#设置title
root.geometry("1000x300")#设置窗口大小
root.resizable(width=True, height=True)#设置窗口大小可以被更改
root.iconbitmap(".\\ico.ico")#设置图标
gui.msgbox(msg="请不要在带有终端的代码编辑器或运行器运行本程序！",title="警告",ok_button="确定")#弹窗提示
#下面是框架部分
def memu():
    pass
def guanyu():
    gui.buttonbox("作者QQ:2096779623   github:https://github.com/2096779623/windows-utility-tools/",choices=("确定","确定","确定","确定","确定","确定"))#弹窗提示
def help():
    gui.msgbox(msg="想要执行什么功能请按对应的菜单  不会的请百度 谷歌！",title="帮助",ok_button="确定")#弹窗提示
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
def iewz():
    os.system("start IEpage.bat")
def zdytc():
    os.system("start tc.bat")
def xssz():
    os.system("start desk.cpl")
def win10sz():
    os.system("start ms-settings:wheel")
def dyxx():
    os.system("start powercfg.cpl")
def kzmb():
    os.system("start control.exe")
def rwlms():
    os.system("reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowSecondsInSystemClock /t REG_DWORD /d 1 /f")
    gui.msgbox(msg="重启电脑或重启资源管理器生效!",title="提示",ok_button="确定")
def godmode():
    os.system("md GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
    os.system("explorer.exe GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
def gbwd():
    os.system("start gbwd.bat")
    gui.msgbox(msg="重启电脑生效!",title="提示",ok_button="确定")
def admin():
    os.system("net localgroup administrators %username% /add")
def networkreset():
    os.system("netsh winsock reset")
    os.system("ipconfig/release")
    os.system("ipconfig/renew")
    gui.msgbox(msg="重启电脑生效!",title="提示",ok_button="确定")
def rd():
    os.system("start rd.bat")
def IEzy():
    os.system("start IEzy.bat")
def saolei():
    os.system("start winmine.exe")
def xqdz():
    os.system("start telnet towel.blinkenlights.nl")
def td():
    os.system("start td.bat")
def msg():
    os.system("start msg.bat")
def gxwjjglq():
    os.system("start fsmgmt.msc")
def adduser():
    os.system("start adduser.bat")
def clearcache():
    os.system("clean.bat")
def lookwifipwd():
    os.system("start lookwifipwd.bat")
def bf():
    os.system("music.bat")
def jsbf():
    os.system("taskkill /im wmplayer.exe /f")
def startup():
    os.system("start explorer.exe shell:Startup")
def ljwifi():
    os.system("start lj.bat")
def fjwifi():
    os.system("start fjwifi.bat")
def systemsx():
    os.system("start control.exe /name Microsoft.System")
def qxdsgj():
    os.system("shutdown -a")
def desktopbk():
    os.system("start desktopbk.bat")
def computername():
    os.system("echo 当前计算机名称为:%COMPUTERNAME%")
def cpuhx():
    os.system("echo CPU核心数:%NUMBER_OF_PROCESSORS%")
def cpujg():
    os.system("echo CPU架构:%PROCESSOR_ARCHITECTURE%")
def bluetooth():
    os.system("start ms-settings:bluetooth")
def mryy():
    os.system("start explorer.exe shell:::{17cd9488-1228-4b2f-88ce-4298e93e0966}")
def wlgxzx():
    os.system("start explorer.exe shell:::{8E908FC9-BECC-40f6-915B-F4CA0E70D03D}")
def wechat():
    os.system("start wechat.bat")
def downfile():
    os.system("start down.bat")
def qx():
    os.system("echo 当前运行权限为:")
    os.system("whoami")
def yjxx():
    os.system("start yjxx.bat")
def win7qd():
    os.system("start msconfig /4")
def win10qd():
    os.system("start taskmgr")
def dsgjtip():
    os.system("start zdydsgj.bat")
def xtyl():
    os.system("start xtyl.bat")
def M2():
    os.system(".\\M2\\NSudo.exe")
def wine():
    os.system("start wine.bat")
def kong():
    pass
def bbh():
    os.system("start bbh.bat")
def fbl():
    x,y = pyautogui.size()#获取当前屏幕分辨率
    print("当前屏幕分辨率为:")
    print(x,y)
def github():
    os.system("start https://github.com/2096779623/windows-utility-tools/")
#下面是菜单部分
menubar = tk.Menu(root)
# 创建亿个子菜单
gongneng = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"1~10", menu=gongneng)#创建菜单
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
menubar.add_cascade(label=u"10~20", menu=gongneng1)#创建菜单
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
menubar.add_cascade(label=u"20~30", menu=gongneng2)#创建菜单
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
gongneng3 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"30~40", menu=gongneng3)#创建菜单
gongneng3.add_command(label=u"打开当前用户文件夹", command=yhwjj)
gongneng3.add_command(label=u"定时关机", command=dsgj)
gongneng3.add_command(label=u"用IE打开网站", command=iewz)
gongneng3.add_command(label=u"自定义弹窗", command=zdytc)
gongneng3.add_command(label=u"显示设置", command=xssz)
gongneng3.add_command(label=u"Windows10设置", command=win10sz)
gongneng3.add_command(label=u"电源选项", command=dyxx)
gongneng3.add_command(label=u"控制面板", command=kzmb)
gongneng3.add_command(label=u"在任务栏显示秒数(win10)", command=rwlms)
gongneng3.add_command(label=u"上帝模式", command=godmode)
gongneng3.add_separator()
gongneng4 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"40~50", menu=gongneng4)#创建菜单
gongneng4.add_command(label=u"关闭Windows Defender", command=gbwd)
gongneng4.add_command(label=u"把当前用户添加到管理员用户组", command=admin)
gongneng4.add_command(label=u"网络重置", command=networkreset)
gongneng4.add_command(label=u"开热点", command=rd)
gongneng4.add_command(label=u"修改IE浏览器主页", command=IEzy)
gongneng4.add_command(label=u"扫雷(win7)", command=saolei)
gongneng4.add_command(label=u"星球大战(彩蛋)", command=xqdz)
gongneng4.add_command(label=u"修改时间和日期", command=td)
gongneng4.add_command(label=u"用Msg发送消息", command=msg)
gongneng4.add_command(label=u"共享文件夹管理器", command=gxwjjglq)
gongneng4.add_separator()
gongneng5 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"50~60", menu=gongneng5)#创建菜单
gongneng5.add_command(label=u"创建一个本地用户", command=adduser)
gongneng5.add_command(label=u"清理缓存", command=clearcache)
gongneng5.add_command(label=u"查看电脑连接过的WIFI密码", command=lookwifipwd)
gongneng5.add_command(label=u"静默播放音乐", command=bf)
gongneng5.add_command(label=u"结束静默播放音乐", command=jsbf)
gongneng5.add_command(label=u"打开启动文件夹", command=startup)
gongneng5.add_command(label=u"连接开放或已保存密码的WIFI", command=ljwifi)
gongneng5.add_command(label=u"查看附件WIFI信息", command=fjwifi)
gongneng5.add_command(label=u"系统属性", command=systemsx)
gongneng5.add_command(label=u"取消定时关机", command=qxdsgj)
gongneng5.add_separator()
gongneng6 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"60~70", menu=gongneng6)#创建菜单
gongneng6.add_command(label=u"获取当前桌面背景(win10)", command=desktopbk)
gongneng6.add_command(label=u"查看当前计算机名称", command=computername)
gongneng6.add_command(label=u"查看CPU核心数量", command=cpuhx)
gongneng6.add_command(label=u"查看CPU架构", command=cpujg)
gongneng6.add_command(label=u"蓝牙", command=bluetooth)
gongneng6.add_command(label=u"设备管理器", command=sbglq)
gongneng6.add_command(label=u"设置默认应用程序", command=mryy)
gongneng6.add_command(label=u"网络和共享中心", command=wlgxzx)
gongneng6.add_command(label=u"微信多开", command=wechat)
gongneng6.add_command(label=u"下载文件", command=downfile)
gongneng6.add_separator()
gongneng7 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=u"70~80", menu=gongneng7)#创建菜单
gongneng7.add_command(label=u"查看当前用户权限", command=qx)
gongneng7.add_command(label=u"查看硬件信息", command=yjxx)
gongneng7.add_command(label=u"管理启动项(win7)", command=win7qd)
gongneng7.add_command(label=u"管理启动项(win10)", command=win10qd)
gongneng7.add_command(label=u"自定义定时关机提示内容", command=dsgjtip)
gongneng7.add_command(label=u"调节系统音量", command=xtyl)
gongneng7.add_command(label=u"最高权限运行程序", command=M2)
gongneng7.add_command(label=u"更改win+e弹出程序", command=wine)
gongneng7.add_command(label=u"修改密钥和版本号", command=bbh)
gongneng7.add_command(label=u"获取当前屏幕分辨率", command=fbl)
gongneng7.add_separator()
menubar.add_command(label=u"帮助", command=help)#创建菜单
menubar.add_command(label=u"关于", command=guanyu)#创建菜单
menubar.add_command(label=u"github链接", command=github)#创建菜单
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
