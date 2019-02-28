#!/usr/bin/python
# -*- coding: utf-8 -*-

inFilename = ["./a_example.txt", "./b_lovely_landscapes.txt", "./c_memorable_moments.txt", "./d_pet_pictures.txt", "./e_shiny_selfies.txt"]
outFilename = ["./a_output.txt", "./b_output.txt", "./c_output.txt", "./d_output.txt", "./e_output.txt"]


class Photo(object):
    id1 = 0
    id2 = 0
    h = 'H'
    length = 0
    tags = []

    def __init__(self, id1, id2, h, tags):
        self.id1 = id1
        self.id2 = id2
        self.h = h
        self.length = length
        self.tags = tags

class Slide(object):
    photos = []

    def __init__(self, photos):
        self.photos = photos

    def toString(self):
        return ' '.join([str(x.id) for x in self.photos])
    

def popVertical(photos):
    return 


#MAIN################################3
X=0 #0: el fichero a_xxx.txt , 1 el fichero b_xxx.txt
fh = open(inFilename[X], "r")
totalPhotos = fh.readline()
photoRaws = fh.readlines()
fh.close()

#prepare photos
H = [] # las fotos horizontales
V = [] # las verticales
V2 = [] # las verticales emparejadas

for i, photoRaw in enumerate(photoRaws):
    elements = photoRaw.replace('\n','',1).split()
    photo= Photo(i, i, elements[0], elements[1], elements[2:len(elements)])
    if (photo.h == "H")
        H.append(photo)
    else:
        V.append(photo)

# Emparejar las V en V2

# Calcular los tags más usados
TAG = []

# Calcular array con las fotos de mayor a menor nº de tags
def pairVertical(vPhotos)
    Pairs = []
    for i, photo in enumerate(vPhotos)
        bestScore = 0
        bestMatchId = -1
        for j, check in enumerate(elements[i+1:len(vPhotos)]))
            if(bestScore>sumTags(photo, check))
                Pairs.append(Photo())




def matchingTags(photo1, photo2)
    return len(photo1.tags.intersection(photo2.tags))

def sumTags(photo1, photo2)
    return photo1.length + photo2.length - matchingTags(photo1, photo2) 

#prepare slides
slides = []
for i, p1 in reversed(list(enumerate(photos))):
    if i > 0:
        popPhoto = photos.pop(len(photos) - 1)
        slidePhotos = []
        slidePhotos.append(popPhoto)
        if popPhoto.h == 'V' and i > 0:
            for j, p2 in reversed(list(enumerate(photos))):
                if j > 0:
                    if p2.h == 'V':
                        slidePhotos.append(photos.pop(len(photos)-1))
                        break
        if (slidePhotos[0].h == 'V' and len(slidePhotos) == 2) or slidePhotos[0].h == 'H':
            slides.append(Slide(slidePhotos))


slidesOrdered = []

slidesOrdered = slides


#write slides
fw = open(outFilename[X], "w")
fw.write(str(len(slidesOrdered)))
fw.write('\n')
for slide in slidesOrdered:
    fw.write(slide.toString())
    fw.write('\n')
fw.close()