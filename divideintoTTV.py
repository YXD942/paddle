import os
import random
import shutil
from shutil import copy2
datadir_normal = "D:/10data/annotations"#（图片文件夹）
datadir_origin = "D:/10data"

all_data = os.listdir(datadir_normal)
num_all_data = len(all_data)
print( "num_all_data: " + str(num_all_data) )
index_list = list(range(num_all_data))

random.shuffle(index_list)
num = 0

all_Odata = os.listdir(datadir_origin)
num_all_Odata = len(all_Odata)
print( "num_all_Odata: " + str(num_all_Odata) )
index_Olist = list(range(num_all_Odata))
#创建用于保存源文件的文件夹
os.mkdir("D:/10data/images")
os.mkdir("D:/10data/images/train")#（将训练集放在这个文件夹下）
Otrain = "D:/10data/images/train"
os.mkdir("D:/10data/images/val")#（将验证集放在这个文件夹下）
Oval = "D:/10data/images/val"
os.mkdir("D:/10data/images/test")#（将测试集放在这个文件夹下）
Otest = "D:/10data/images/test"

trainDir = "D:/10data/annotations/train"#（将训练集放在这个文件夹下）
if not os.path.exists(trainDir):
    os.mkdir(trainDir)
        
validDir = "D:/10data/annotations/val"#（将验证集放在这个文件夹下）
if not os.path.exists(validDir):
    os.mkdir(validDir)
        
testDir = "D:/10data/annotations/test"#（将测试集放在这个文件夹下）        
if not os.path.exists(testDir):
    os.mkdir(testDir)
        
for i in index_list:
    fileName = os.path.join(datadir_normal, all_data[i])
    if num < num_all_data*0.6:
        #print(str(fileName))
        copy2(fileName, trainDir)
    elif num>num_all_data*0.6 and num < num_all_data*0.8:
        #print(str(fileName))
        copy2(fileName, validDir)
    else:
        copy2(fileName, testDir)
    num += 1

train_data = os.listdir(trainDir)
val_data = os.listdir(validDir)
test_data = os.listdir(testDir)
for i in index_Olist:
    fileName = os.path.join(datadir_origin, all_Odata[i])
    print(all_Odata[i])
    print(train_data)
    if  all_Odata[i].find('.jpg') != -1 and all_Odata[i].find('.json') == -1:
        if all_Odata[i].strip('.jpg') + '.png' in train_data:
            copy2(fileName,Otrain)
        elif all_Odata[i].strip('.jpg') + '.png' in val_data:
            copy2(fileName,Oval)
        elif all_Odata[i].strip('.jpg') + '.png' in test_data:
            copy2(fileName,Otest)
        else:
            continue
    else:
        continue