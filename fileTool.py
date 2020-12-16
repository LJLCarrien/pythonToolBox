import os
import shutil

# 创建文件 isReplace 同名覆盖
def createFile(filePath, fileFullName, content,isReplace=True):
    full_path = '%s/%s' % (filePath, fileFullName)
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    if not isReplace:
        index=1
        while os.path.exists(full_path):
            full_path='%s/%s(%s)' % (filePath, fileFullName,index)
            index=index+1
    file = open(full_path, 'w',encoding="utf-8")
    file.write(content)
    print("outJson: ",full_path)

# 获取指定后缀文件
def getAllFileListInClude(foldPath,includeSuffix,bFoldName=False):
    fileList = []
    for foldName, childFold, childFiles in os.walk(foldPath):
        for fileName in childFiles:
            if not fileName.find(includeSuffix) ==-1:
                if bFoldName:
                    fileName=os.path.join(foldName,fileName)
                fileList.append(fileName)
                print ("fileName: %s" %fileName)
    return fileList

def delFold(foldPath,delFoldState):
    """
    删除该文件夹里的所有文件
    delFoldState: 0:删除子文件，保留所有文件夹 1：删除子文件和子文件夹 2：删除子文件、子文件夹和自身目录
    """
    for foldabsPath, childFolds, childFiles in os.walk(foldPath):
        for fileName in childFiles:
            print(foldabsPath,fileName)
            filePath=os.path.join(foldabsPath,fileName)
            os.remove(filePath)
        print(foldabsPath)
        if not foldabsPath==foldPath and delFoldState>=1:
            shutil.rmtree(foldabsPath)
    if delFoldState==2:
        shutil.rmtree(foldPath)
