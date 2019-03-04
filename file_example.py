import math
import numpy as np
import time
import random

files = [
    'a_example.txt',
    'b_lovely_landscapes.txt',
    'c_memorable_moments.txt',
    'd_pet_pictures.txt',
    'e_shiny_selfies.txt'
]

selectedFiles = [
    files[2]
]


tagsIndexCount = 0
tagsDictionary = {}

class Photo(object):
    id = 0
    h = 'H'
    tags = np.array([])

    def __init__(self, id, h, tags):
        self.id = id
        self.h = h
        self.tags = np.array([tagsDictionary[tag] for tag in tags])       

class Slide(object):
    photos = []
    tags = np.array([])

    def __init__(self, photos):
        self.photos = photos
        self.tags = np.array([])
        if len(photos) == 1:
            self.tags = photos[0].tags
        else:
            self.tags = np.unique(np.concatenate((photos[0].tags, photos[1].tags)))
    def toString(self):
        return ' '.join([str(x.id) for x in self.photos])

def slideCompare( s1, s2):
    intersect = len(np.intersect1d(s1.tags, s2.tags, True))
    # intersect = 0
    # for t1 in s1.tags:
    #     for t2 in s2.tags:
    #         if t1 == t2:
    #             intersect +=1
    #             break
    left = len(s1.tags) - intersect
    right = len(s2.tags) - intersect
    return min(intersect, left, right)

def photoScore(p1, p2):
    intersect = len(np.intersect1d(p1.tags, p2.tags, True))
    return len(p1.tags) + len(p2.tags) - intersect

def intersections(p1, p2):
    return len(np.intersect1d(p1.tags, p2.tags, True))

def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if len(x.tags) > len(pivot.tags):
                less.append(x)
            elif len(x.tags) == len(pivot.tags):
                equal.append(x)
            elif len(x.tags) < len(pivot.tags):
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

def sortHighEnd(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if len(x.tags) < len(pivot.tags):
                less.append(x)
            elif len(x.tags) == len(pivot.tags):
                equal.append(x)
            elif len(x.tags) > len(pivot.tags):
                greater.append(x)
        # Don't forget to return something!
        return sortHighEnd(less)+equal+sortHighEnd(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

def sortRandom(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            value = random.randint(0,2)
            if value == 0:
                less.append(x)
            elif value == 1:
                equal.append(x)
            elif value == 2:
                greater.append(x)
        # Don't forget to return something!
        return sortRandom(less)+equal+sortRandom(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

for filename in selectedFiles:
    print ('[Opening file READ...')

    fh = open(filename,"r")
    totalPhotos = fh.readline()
    photosRaw = fh.readlines()
    fh.close()

    print ('...READ file finished]')
    print ('')
    print ('[Creating tag dictionary...')
    for i, photo in enumerate(photosRaw):
        elements = photo.replace('\n','',1).split()
        tags = elements[2:len(elements)]
        for tag in tags:
            tagsDictionary[tag] = tagsIndexCount
            tagsIndexCount += 1

    print ('\ttotal different tags = ['+str(len(tagsDictionary))+']')
    print ('..done]')
    print ('')
    print ('[Creating photo objects...')
    #prepare photos
    photos = []
    for i, photo in enumerate(photosRaw):
        elements = photo.replace('\n','',1).split()
        photos.append(Photo(i, elements[0], elements[2:len(elements)]))

    print ('...done]')
    print ('')
    print ('[sorting photos by tags amount...')

    photos = sort(photos)

    print ('...done]')
    print ('')
    print ('[grouping photos...')
    photosH = []
    photosV = []

    for p in photos:
        if p.h == 'H':
            photosH.append(p)
        else :
            photosV.append(p)

    print ('...done]')
    print ('')
    print ('TOTAL OF HORIZONTALS = ['+str(len(photosH))+']')
    print ('TOTAL OF VERTICALS = ['+str(len(photosV))+']')
    print ('')
    print ('[Creating slides...')

    slides = []
    print ('\t...horizontals...')
    for p in photosH:
        slides.append(Slide([p]))
    print ('\t...verticals...')
    counterPhotosvOrdered = 0
    # for i,p in enumerate(photosV):
    #     if (i % 2 == 0) and (i != 0):
    #         slides.append(Slide([photosV[i], photosV[i-1]]))
    while len(photosV) > 1:
        index = len(photosV)-1
        p1 = photosV.pop(index)
        index -= 1
        bestIndex = index
        bestScore = 0
        counterPhotosvOrdered += 1
        if counterPhotosvOrdered == 10:
            counterPhotosvOrdered = 0
            print ('\t...photos left = ['+str(len(photosV))+']')
        while index > 0:
            score = photoScore(p1, photosV[index])
            if score > bestScore:
                bestScore = score
                bestIndex = index
            if intersections(p1 , p2) == 0:
                break

            index -= 1
        p2 = photosV.pop(index)
        slides.append(Slide([p1,p2]))

    print ('...done]')
    print ('')
    print ('[Sorting slides by tags amount...')
    slides = sortHighEnd(slides)
    print ('...done]')
    print ('')
    print ('TYPE OF slides.tags = ' + str(type(slides[0].tags[0])))
    print ('')
    print ('[Ordering slides...')

    slidesOrdered = []

    print ('first index = ' +str(len(slides[0].tags)))
    print ('last index = ' + str(len(slides[len(slides)-1].tags)))
    tagsFactor = math.log10(tagsIndexCount)
    slidesOrdered.append(slides.pop(len(slidesOrdered ) - 1))
    slideCounter = 0
    execTimeAppending = 0
    execTimeComparing = 0
    execTimePrinting = 0
    counterSlidesOrdered = 0
    bestResult = 999999999
    totalScore = 0
    lastIterations = 0
    while len(slides) > 0:
        iterations = 0
        maxResult = 0
        currentSlide = slidesOrdered[slideCounter]
        counter = len(slides) - 1
        index = len(slides) - 1
        counterSlidesOrdered += 1
        timePrint = time.time()
        if counterSlidesOrdered == 100:
            counterSlidesOrdered = 0
        print ('\ttime Comparing=['+str(execTimeComparing)+'] time Appending=['+str(execTimeAppending)+']' + '] time Printing  =[' + str(execTimePrinting) + ']')
        print ('\tslides left = [' + str(len(slides)) + '] last tags amount = [' + str(len(currentSlide.tags)) + '] score = ['+str(totalScore)+'] iterations = ['+str(lastIterations)+'] highScore = ['+str(totalScore + len(slides)*bestResult)+']') #
        execTimePrinting += (time.time() - timePrint)
        while counter > 0:
            timeCompare = time.time()
            result = slideCompare(slides[counter], currentSlide)
            execTimeComparing += (time.time() - timeCompare)
            if result > maxResult:
                maxResult = result
                index = counter
            if result >= bestResult:
                break
            if (maxResult * 3) > len(currentSlide.tags):
                break
            # if iterations > 100:
            #     break
            iterations += 1
            counter -= 1
        timePop = time.time()
        lastIterations = iterations
        totalScore += maxResult
        if maxResult > 0:
            bestResult = maxResult
        slidesOrdered.append(slides.pop(index))
        execTimeAppending += (time.time() - timePop)
        slideCounter += 1
        

    print ('...slides ordered]')
    print ('')
    print ('[Opening file WRITE...')

    #write slides
    fw = open("result_" + filename, "w")
    fw.write(str(len(slidesOrdered)))
    fw.write('\n')
    for slide in slidesOrdered:
        fw.write(slide.toString())
        fw.write('\n')
    fw.close()

    print ('...file WRITE finished]')