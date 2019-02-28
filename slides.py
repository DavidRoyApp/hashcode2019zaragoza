filename = 'my_scripts/a_example.txt'

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

fh = open(filename,"r")
totalPhotos = fh.readline()
photosRaw = fh.readlines()
fh.close()

#prepare photos
photos = []
for i, photo in enumerate(photosRaw):
    elements = photo.replace('\n','',1).split()
    print elements
    photos.append(Photo(i, elements[0], elements[2:len(elements)]))

#Order photos by tags count
# TODO

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
fw = open("result.txt", "w")
fw.write(str(len(slidesOrdered)))
fw.write('\n')
for slide in slidesOrdered:
    fw.write(slide.toString())
    fw.write('\n')
fw.close()