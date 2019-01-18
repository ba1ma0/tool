'''此脚本主要是用来监控某个文件夹中文件增删改查变化情况用于审计时文件的变化'''
#-*- coding:utf-8 -*-
# Python 3.6
# Author: 白猫 <cyber-security@qq.com>
# Date: 2019-1-18 13:57:54
import sys,time,logging
from module import printc
try:
    import watchdog
    from watchdog.observers import Observer
    from watchdog.events import LoggingEventHandler,FileSystemEventHandler
except:
    msg="\n[-] 检测到你还没有安装依赖包PIL,请使用命令pip install PIL 进行安装"
    printc.printf(msg,'red')
#该函数主要是检测某文件夹中文件的变化情况    
def showChangeInfo(path):
    msg = """ 
  ______ _ _                              _ _             _                   
 |  ____(_| |                            (_| |           (_)                  
 | |__   _| | ___   _ __ ___   ___  _ __  _| |_ ___  _ __ _ _ __   __ _       
 |  __| | | |/ _ \ | '_ ` _ \ / _ \| '_ \| | __/ _ \| '__| | '_ \ / _` |      
 | |    | | |  __/ | | | | | | (_) | | | | | || (_) | |  | | | | | (_| |_ _ _ 
 |_|    |_|_|\___| |_| |_| |_|\___/|_| |_|_|\__\___/|_|  |_|_| |_|\__, (_(_(_)
                                                                   __/ |      
                                                                  |___/       
"""
    printc.printf(msg,'yellow')
    class LoggingEventHandler(FileSystemEventHandler):
        """Logs all the events captured."""
        #文件被移动时显示白色
        def on_moved(self, event):
            super(LoggingEventHandler, self).on_moved(event)
            t = time.strftime("%Y-%m-%d %X",time.localtime())
            what = 'directory' if event.is_directory else 'file'
            msg = t + " - Moved %s: from %s to %s" %(what,event.src_path,event.dest_path)
            print(msg)
        #文件创建时显示绿色(green)
        def on_created(self, event):
            super(LoggingEventHandler, self).on_created(event)
            t = time.strftime("%Y-%m-%d %X",time.localtime())
            what = 'directory' if event.is_directory else 'file'
            msg = t + " - Created %s: %s"%(what,event.src_path)
            printc.printf(msg,'green')
       #文件删除时显示红色(red)
        def on_deleted(self, event):
            super(LoggingEventHandler, self).on_deleted(event)
            t = time.strftime("%Y-%m-%d %X",time.localtime())
            what = 'directory' if event.is_directory else 'file'
            msg = t + " - Deleted %s: %s" %(what,event.src_path)
            printc.printf(msg,'red')
        #文件修改时显示蓝色(blue)
        def on_modified(self, event):
            super(LoggingEventHandler, self).on_modified(event)
            t = time.strftime("%Y-%m-%d %X",time.localtime())
            what = 'directory' if event.is_directory else 'file'
            msg = t + " - Modified %s: %s" %(what,event.src_path)
            printc.printf(msg,'blue')    
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    showChangeInfo()