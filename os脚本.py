import os

# 运行cmd命令 关机之灵shutdown -s -t 500  取消是-a
# os.system('notepad')
# os.system('mspaint')
# 关闭应用
# os.system("taskkill /f /im notepad.exe")
# 绝对路径
# print(os.path.abspath(r'./'))
# 导入win包
import win32con
import win32gui
import time

# 找出窗体编号
laji=win32gui.FindWindow('CabinetWClass','回收站')
# 隐藏窗体
#     win32gui.ShowWindow(laji,win32con.SW_HIDE)
# 显示
#     win32gui.ShowWindow(laji, win32con.SW_SHOW)

# while True:
#     time.sleep(1)
#     win32gui.ShowWindow(laji, win32con.SW_SHOW)
#     time.sleep(1)
#     win32gui.ShowWindow(laji,win32con.SW_HIDE)

# with open("脚本.txt","r",encoding='utf-8') as fp:
#     pstr=fp.read()
#
#     def resault(pstr,oldstr,newstr):
#         resault1=pstr.split(oldstr)
#         return newstr.join(resault1)
#
#     a=resault(pstr,'高文博','纪委')
#     with open("脚本.txt", "w", encoding='utf-8') as fs:
#         fs.write(a)

for letter in 'Python':     # 第一个实例
   print ('当前字母 :', letter)