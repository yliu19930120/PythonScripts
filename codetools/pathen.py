#-*- coding:utf-8 -*-
import os

class CodeReplace(object):

    def __init__(self,rootPath):
        self.old = '"code", java.getCode()'
        self.new = '"id", java.getId()'
        self.rootPath = rootPath
        self.repFileList = []
    def run(self):
        self.recursionReplace(self.rootPath)
        self.log_write()
    #替换文本
    def replace(self,_file):
        rep = None
        with open(_file, 'r', encoding='UTF-8') as f:
            content = f.read()
            if(self.old in content):
                rep = content.replace(self.old, self.new)

        if  not rep is None:
            with open(_file, 'w', encoding='UTF-8') as f:
                f.write(rep)
                self.repFileList.append(_file)
                print('替换文件:', _file, '文件完成')

    #递归读取文件
    def recursionReplace(self,path):
        pathDir = os.listdir(path)  # 获取当前路径下的文件名，返回List
        for s in pathDir:
            newDir = os.path.join(path, s)  # 将文件名加入到当前文件路径后面
            if os.path.isfile(newDir):  # 如果是文件
                if os.path.splitext(newDir)[1] == ".java":  # 判断是否是java文件
                    self.replace(newDir)  # 替换文本
                    pass
            else:
                self.recursionReplace(newDir)  # 如果不是文件，递归这个文件夹的路径
    #更改日期指写入文件
    def log_write(self):
        log = os.path.abspath(os.path.join(os.path.dirname(self.rootPath), ".."))+'\\replog.log'
        with open(log, 'w', encoding='UTF-8') as f:
            for content in self.repFileList:
                f.write(content)
                f.write('\n')
        print('替换文件记录写入:',log,'文件')



if __name__ == '__main__':
    rootPath = 'E:\code\workspace\workspace\dataAnalyseCommons'
    codeReplace = CodeReplace(rootPath)
    codeReplace.run()