import os

def createFile(filePath, fileFullName, content):
    full_path = '%s/%s' % (filePath, fileFullName)
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    file = open(full_path, 'w',encoding="utf-8")
    file.write(content)


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