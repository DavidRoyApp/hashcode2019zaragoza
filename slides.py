#!/usr/bin/python
# -*- coding: utf-8 -*-

inFilename = ["./a_example.txt", "./b_lovely_landscapes.txt", "./c_memorable_moments.txt", "./d_pet_pictures.txt", "./e_shiny_selfies.txt"]
outFilename = ["./a_output.txt", "./b_output.txt", "./c_output.txt", "./d_output.txt", "./e_output.txt"]


class Photo(object):
    id1 = 0
    id2 = 0
    h = 'H'
    tags = []
    tagSum = 0
    score= 0

    def __init__(self, id1, id2, h, tags):
        self.id1 = id1
        self.id2 = id2
        self.h = h
        self.tags = tags
        self.tagSum = 0
        self.score = 0

    def toString(self):
        if self.id1 == self.id2:
            return str(self.id1)
        else:
            return str(self.id1)+' '+str(self.id2)

class Slide(object):
    photo = {}

    def __init__(self, photo):
        self.photo = photo

    def toString(self):
        return ' '+self.photo.toString()
    


#MAIN################################3
X=0 #0: el fichero a_xxx.txt , 1 el fichero b_xxx.txt
fh = open(inFilename[X], "r")
totalPhotos = fh.readline()
photoRaws = fh.readlines()
fh.close()

#prepare photos
ALL = [] # todas las fotos
H = [] # las fotos horizontales
V = [] # las verticales
V2 = [] # las verticales emparejadas

for i, photoRaw in enumerate(photoRaws):
    elements = photoRaw.replace('\n','',1).split()
    photo= Photo(i, i, elements[0], elements[2:len(elements)])
    if photo.h == "H":
        H.append(photo)
    else:
        V.append(photo)

# Emparejar las V en V2


# Juntarlas todas
for photo in H:
    ALL.append(photo)
for photo in V2:
    ALL.append(photo)

# Calcular los tags más usados
TAG = {}
for photo in H:
    for tag in photo.tags:
        if tag in TAG:
            TAG[tag]+=1
        else:
            TAG[tag]=1

for photo in V2:
    for tag in photo.tags:
        if tag in TAG:
            TAG[tag]+=1
        else:
            TAG[tag]=1

for photo in ALL:
    for tag in photo.tags:
        photo.tagSum+= TAG[tag]
        photo.score = photo.tagSum


# Calcular array con las fotos de mayor a menor nº de tags
MAXTAGS = []


#prepare slides
ORDERED= []
ORDERED= sorted(ALL, key=lambda x: x.socre,reverse=True)

#write slides
fw = open(outFilename[X], "w")
fw.write(str(len(ORDERED)))
fw.write('\n')
for slide in ORDERED:
    fw.write(slide.toString())
    fw.write('\n')
fw.close()