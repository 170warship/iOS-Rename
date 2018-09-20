#encoding:utf-8 # 支持中文输入
import re
import os
import string
import random
s = os.sep

##获取当前工作目录
root = os.path.abspath('.')
#需要忽略的文件后缀
ignoredTrail = [".py",".c"]
#需要忽略的文件夹
ignoredDirPath   = ["lib",".git"]
#需要匹配的文件后缀
containTrail   = [".h",".m"]


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


#获取所有XIB文件名
def getAllFilesXIB(path):
 allfile=[]
 for dirpath,dirnames,filenames in os.walk(path):
  # print 'dirpath: ' + dirpath 
  if isIgnoredByDirPath(dirpath):
    continue
     
  for name in filenames:
    if name.endswith('.xib'):
      allfile.append(os.path.join(dirpath, name))
    
 return allfile 

def randomString():

  return string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 3)).replace(" ","") + (''.join(random.sample(string.ascii_letters + string.digits, 8)))



endVC = ['VC','vc','viewController','ViewController', 'VIEWCONTROLLER']

endData = ['Data', 'data', 'Model','MODEL','MO']

endView = ['VIEW', 'View', 'view']

endEngine = ['Engine','engine','Manager','MA','manager','Center','center']

endCell = ['Cell','cell','CELL']

endDelegate = ['Delegate','delegate','del','gate','Protocol','PROTOCOL','procotol']

endTool = ['Tool', 'tool', 'Util','util','helper','Helper','Browser','browser','Photo','photo','LIB','lib', 'Image','image','Button']

endArray = [endVC,endData,endView,endEngine,endCell,endDelegate,endTool]


ranDomName1 = ['MXG','MXG','MXG','MXG','MXG','MXG','SYSTM','COL','TOP','RIGHT','MON','CON','ZZZ','YYY','HHH','AAA','BBB','CCC','CIRCLE','PLUS','MEE','NES','MY','YMD','TENCENT']

ranDomName2 = ['The','Fog','TR','Kongjian','Xitong','Lunbotu','Shitu','Tupian','Photo','Xieyi','Text','Rich','Line','Sys','Turn','Rever', 'Tiaozhuan','Control','Noname','Name','Sleep','Date','Weak','Time','Dic','File','Function','Fanfa','Hob','MMM','Program','Net','Device','SheBei','Didian','People','Thing','Shijian','Shang','Shangbao','Other','Yanse','Color','Object','Animate','Dongzuo','Do','Act','Different','Plus','Sub', 'Age','Newer','Login','Register','Yanzhengma','Length','Count','Jihuoma','Run','Loop','Star','Get','Set','Get','Set','Get','Set','Get','Set','Qianmian','Read','Write','Laker','Beijing','Some','Get','Set','In','This','That','String','Number','AAA','Main','Work','Enable','Disable','Check','Ment']

ranDomName3 = ['Welcome','In' ,'Order','To', 'Get','First','1','2','3','4','5','6', 'Need', 'Some', 'Basic', 'Information','First','Comes','Three' 'Pieces', 'The','Suite', 'Head','LLV','MMO','RPG','Game','Random','Test','Length','Count','Shumu','Tree','Heap','String','Number','Ana','Bit','Use','For','Date','Shangbao','Other','Yanse','Color','Object','Button','View','Image','View','Load','Creat']

ranDomName4 = ['Welcome','In' ,'Order','To', 'Get','First','1','2','3','4','5','6', 'Object','Figure','Cele','Mass','Holiday','Calcute','Mean','Wee','Probably','Gate','World','Car','Ba','Age','Giving','Doing','Play','Add','EEE','Change','JSON','Standar','Adavance','Word','Check','SSS','Hos','Vic','Ter','Style','UI','UI','Style','CSS','Html','Test','Text','Tion','Animate','Button','View','Image','Image','View','View','View','Load','Mon']


ranDomName = [ranDomName1, ranDomName2,ranDomName3, ranDomName4]

dicOriginName = {}
dic = {}
def rechangeStr(matched):
  value = matched.group(2)

  randomNum = random.randint(2,4)

  if randomNum == 2:
    if random.random() < 0.38:
      randomNum = 3

  rname = ''

  for index in range(randomNum):
    rnameArr = ranDomName[index]

    rname += rnameArr[random.randint(0,len(rnameArr)-1)]
  
  endStr = ''

  for ends in endArray:
    find = False
    for endValue in ends:
      if value.endswith(endValue):
        endStr = endValue
        find = True
        break

    if find:
      break



  rname += endStr

  if dic.has_key(rname):
    rname = randomString()

  # jsonmodel用protocol与model同名来作处理的，所以要同名替换
  if dicOriginName.has_key(value):
    rname = dicOriginName[value]

  dic[rname] = 1

  dicOriginName[value] = rname   

  return '\n__attribute__((objc_runtime_name("' + rname + '"))) ' + matched.group(1)  



#重命名
def rename(oldName,newName,filePath):
  a = open(filePath,'r') #打开所有文件
  str = a.read()

  # searchObj = re.search(r'\n[ \t]*(@interface[ \t]+([a-zA-Z0-9-_]+)[ \t]*\:[ \t]*[a-zA-Z0-9-_]+[ \t]*\n)', str, re.M|re.I)

  # if searchObj:
  #   print searchObj.group(0)
  #   print rechangeStr(searchObj)

  # searchObj2 = re.search(r'\n[ \t]*(@protocol[ \t]+([a-zA-Z0-9-_]+)[ \t]*(<[a-zA-Z0-9-_]+>)*\n)', str, re.M|re.I)

  # if searchObj2:
  #   print searchObj2.group(0)
  #   print rechangeStr(searchObj2)


  str = re.sub(r'\n[ \t]*(@interface[ \t]+([a-zA-Z0-9-_]+)[ \t]*\:[ \t]*[a-zA-Z0-9-_]+[ \t]*(<[a-zA-Z0-9-_, \t]+>)*[ \t]*\n)', rechangeStr, str)

  str = re.sub(r'\n[ \t]*(@protocol[ \t]+([a-zA-Z0-9-_]+)[ \t]*(<[a-zA-Z0-9-_]+>)*\n)', rechangeStr, str)


  b = open(filePath,'w')
  b.write(str) #再写入
  b.close() #关闭文件
  print "============" + filePath + " finished"



def rechangeXIBStr(matched):
  value = matched.group(1)

  rname = value

  if dicOriginName.has_key(value):
    rname = dicOriginName[value]

  return 'customClass="' + rname + '"'

#重命名XIB里的类
def renameXIBWithHistory(filePath):
  a = open(filePath,'r') #打开所有文件
  str = a.read()

  str = re.sub(r'customClass="([a-zA-Z0-9-_]+)"', rechangeXIBStr, str, re.M|re.I)


  b = open(filePath,'w')
  b.write(str) #再写入
  b.close() #关闭文件
  print "============" + filePath + " finished"




def canChange(filePath):
  file = getFileNameAndExt(filePath)
  if file[1] != '.h':
    return bool(0)

  return bool(1)



fileList = getAllFiles(root)

print len(fileList)

for file in fileList:
  print file
  rename('','',file)

fileListXIB = getAllFilesXIB(root)
for filexib in fileListXIB:
  renameXIBWithHistory(filexib)

