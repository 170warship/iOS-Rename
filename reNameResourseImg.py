#encoding:utf-8 # 支持中文输入
import re
import os
import string
import random

##获取当前工作目录
root = os.path.abspath('.')
#需要忽略的文件后缀
ignoredTrail = [".h",".m",".c"]
#需要忽略的文件夹
ignoredDirPath   = ["lib",".git",".imageset"]
#需要匹配的文件后缀
containTrail   = [".png",".jpg",".jpeg",".imageset"]


renameOrigin  = "mingxing_"

renameAfter  = "mxolnetwork_"


#获取文件名和后缀
def getFileNameAndExt(filename):
 (filepath,tempfilename) = os.path.split(filename);
 (shotname,extension) = os.path.splitext(tempfilename);
 return shotname,extension

#是否是需要根据后缀忽略的文件
def isIgnoredByTrail(filePath):
  file = getFileNameAndExt(filePath)
  for trail in ignoredTrail:
    if file[1] == trail:
      # print "忽略文件:" + filePath
      return bool(1)
  return bool(0)

#是否是需要根据后缀匹配的文件
def isContainByTrail(filePath):
  file = getFileNameAndExt(filePath)
  for trail in containTrail:
    if file[1] == trail:
      # print "忽略文件:" + filePath
      return bool(1)
  return bool(0)
  
#是否根据文件夹路径葫芦
def isIgnoredByDirPath(dirpath):
  for path in ignoredDirPath:
    if string.find(dirpath,path) != -1:
      # print "忽略目录：" + dirpath
      return bool(1)
    else:
      # print "匹配目录：" + dirpath
      continue
  return bool(0)


#获取所有文件名与文件夹名
def getAllFilesAndDirectory(path):
  allfile=[]
  for dirpath,dirnames,filenames in os.walk(path):
    # print 'dirpath: ' + dirpath 
    if isIgnoredByDirPath(dirpath):
      continue


    # 目录也可要改
    for dirname in dirnames:
      if isIgnoredByTrail(dirname):
        continue
      elif isContainByTrail(dirname):
        allfile.append(os.path.join(dirpath, dirname))

     
    for name in filenames:
      if isIgnoredByTrail(name):
        continue
      elif isContainByTrail(name):
        allfile.append(os.path.join(dirpath, name))

  return allfile

def rechangeStr(matched):
  return '/' +  renameAfter + matched.group(1)


def changeResourceImgName(infile):
  str = re.sub(r'/' + renameOrigin + '([^\n\/]+)$', rechangeStr, infile)
  print str
  os.rename(infile, str)




fileList = getAllFilesAndDirectory(root)

print len(fileList)

for file in fileList:
  print file
  changeResourceImgName(file)
