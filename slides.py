#!/usr/bin/python
# -*- coding: utf-8 -*-

inFilename = ["./a_example.txt", "./b_lovely_landscapes.txt", "./c_memorable_moments.txt", "./d_pet_pictures.txt", "./e_shiny_selfies.txt"]
outFilename = ["./a_output.txt", "./b_output.txt", "./c_output.txt", "./d_output.txt", "./e_output.txt"]


class Photo(object):
    id = 0
    h = 'H'
    tags = []

    def __init__(self, id, h, tags):
        self.id = id
        self.h = h
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
    photo= Photo(i, elements[0], elements[2:len(elements)])
    if (photo.h == "H")
        H.append(photo)
    else:
        V.append(photo)

# Emparejar las V

# Calcular los tags más usados

# Calcular array con las fotos de mayor a menor nº de tags

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