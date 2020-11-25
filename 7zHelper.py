# 环境 pythotn 3.8.5

# 7z x {fileName} -o{outputDirectory} 
# x 表示解压一个文件
# {fileName} 是文件名称或者文件路径的占位符
# -o 表示指定输出路径
# {outputDirectory} 是解压后文件夹的占位符，必须是一个不存在的文件夹。
# 举例：7z x C:\Users\walterlv\demo.7z -oC:\Users\walterlv\demo
def decompressFile(zipfileFullPath,outPutPath):
    decompresscmd="7z x %s -o%s" % (zipfileFullPath, outPutPath)
    runCmd(decompresscmd)

# 7z a {fileName} {outputDirectory} 
# a：将文件添加到压缩档案中
def compressFile(filePath):
    runCmd("7z a %s %s" % (zipfileFullPath, foldPath))


def runCmd(cmdOrder):
    try:
        return os.system(cmdOrder) == 0
    except IOError:
        print('[Failed] IOError : run cmdOrder Error:  %s' % cmdOrder)
        return False