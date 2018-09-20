#encoding:utf-8 # 支持中文输入
from PIL import Image
import re
import os
import string
import random
import math

##获取当前工作目录
root = os.path.abspath('.')
#需要忽略的文件后缀
ignoredTrail = [".h",".m",".c"]
#需要忽略的文件夹
ignoredDirPath   = ["lib",".git"]
#需要匹配的文件后缀
containTrail   = [".png",".jpg",".jpeg"]


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


#获取所有文件名
def getAllFiles(path):
  allfile=[]
  for dirpath,dirnames,filenames in os.walk(path):
    # print 'dirpath: ' + dirpath 
    if isIgnoredByDirPath(dirpath):
      continue
     
    for name in filenames:
      if isIgnoredByTrail(name):
        continue
      elif isContainByTrail(name):
        allfile.append(os.path.join(dirpath, name))

  return allfile



def changeImage(infile):
  im = Image.open(infile)
  
  w,h = im.size

  os.system('sips -z ' + bytes(math.ceil(1.5*h)) + ' ' + bytes( math.ceil(1.5*w) ) + ' ' + infile +' --out ' + infile)
  
  os.system('sips -z ' + bytes(h) + ' ' + bytes(w) + ' ' + infile +' --out ' + infile)
  # im = Image.open(infile)
  # im = im.convert('RGBA')
  # w,h = im.size

  # newsize = 1.3*w, 1.3*h
  # im = im.resize(newsize, Image.NEAREST)

  # newsize = w, h
  # im = im.resize(newsize, Image.NEAREST)

  # im.save(infile)




fileList = getAllFiles(root)

print len(fileList)

for file in fileList:
  print file
  changeImage(file)
