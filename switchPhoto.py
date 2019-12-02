# -*- coding:utf-8 -*-
from PIL import Image
import os
from collections import namedtuple

sourcePhotosPath = "G:\photo1"
destPhotosPath = "G:\photo2"
sourcePhotos = []
destPhotos = []
FILETYPE = {"jpg":"jpeg"}   #这里需要自定义后缀名映射关系

#遍历指定文件夹，将所在文件夹下所有照片对象，放入列表中。
def getPhotosInFile(photosPath,photosList):
    fullPhotoPaht = ""
    Photo = namedtuple('Photo',['name','obj'])
    for fileName in os.listdir(photosPath):
        fullPhotoPaht = os.path.join(photosPath,fileName)
        im = Image.open(fullPhotoPaht)
        photo = Photo(fileName,im)
        #w,h = photo.obj.size
        photosList.append(photo)
        #print(photo.name + " " + str(w) + "," + str(h))
    return 0

#修改照片对象为指定名称，像素
def changePhotosAttr():
    global FILETYPE
    for i in range(len(sourcePhotos)):
        if i == len(destPhotos):  #如果遍历sourcePhotos文件数比destPhotos多，那么把destPhotos全部处理完就返回，防止空指针报错
            return 0

        photo = sourcePhotos[i].obj
        photoName = sourcePhotos[i].name
        w2,h2 = photo.size

        photoDest = destPhotos[i].obj
        photoNameDest = destPhotos[i].name
        w1, h1 = photoDest.size

        type = FILETYPE[photoName.split(".")[1]]
        dst = os.path.join(destPhotosPath, photoName)
        w,h = calPixel(w1, h1, w2, h2)
        out =  photoDest.resize((w,h))
        out.save(dst,type)
        print(photoNameDest + " changed !\n")

        """
        src = os.path.join(sourcePhotosPath,photoName)
        dst = os.path.join(destPhotosPath,photoName)
        os.rename(src, dst)
        """
    return 0

#计算像素
def calPixel(w1,h1,w2,h2):
    if(w2 > h2):
        h = h2
        w = int((h2/h1)*w1)
        if(w > w2):
            w = w2
            h = int((w2/w1)*h1)
    else:
        w = w2
        h = int((w2/w1)*h1)
        if(h > h2):
            h = h2
            w = int((h2/h1)*w1)

    #print("(" + str(w1) + "," + str(h1) + ")" + "(" + str(w2) + "," + str(h2) + ")" + "(" + str(w) + "," + str(h) + ")")
    return w,h

#将列表文件，放入指定位置
def putPhotosTo():
    pass


getPhotosInFile(sourcePhotosPath,sourcePhotos)
getPhotosInFile(destPhotosPath,destPhotos)
changePhotosAttr()
