from PIL import Image as image
import string
import random

finalIm = image.open("./binary2.gif")
finalIm.show()

#Finding Co-ordinates of letters in the captcha


start = 0
end = 0
inLetter = False
foundLetter = False
letters = []

for x in range(finalIm.size[0]):
    for y in range(finalIm.size[1]):
        pix = finalIm.getpixel((x,y))
        if (pix!=255):
            inLetter = True

    if (inLetter == True and foundLetter == False):
        foundLetter = True
        start = x

    if (inLetter == False and foundLetter == True):
        foundLetter = False
        end = x
        letters.append((start,end))

    inLetter = False

# Populating training set

nameCount = 0

for letter in letters:
    im2 = finalIm.crop(( letter[0] , 0, letter[1],finalIm.size[1] ))
    im2.save("./trainingSet/"+str(nameCount)+".gif")
    nameCount+=1

#Creating Mask Images

for i in range(6):

    trainingSetImage = image.open("./trainingSet/"+str(i)+".gif")
    
    #finding start

    startTrainingSetImage = 0
    flag = 0

    for y in range(trainingSetImage.size[1]):
        for x in range(trainingSetImage.size[0]):

            pix = trainingSetImage.getpixel((x,y))
            if (pix == 0):
                startTrainingSetImage = y
                flag = 1
                break
            else:
                continue
        
        if (flag==1):
            break

    
    #finding end 

    endTrainingSetImage = 0

    for y in range(startTrainingSetImage+1,trainingSetImage.size[1]):
        flag = 0
        for x in range(trainingSetImage.size[0]):

            pix = trainingSetImage.getpixel((x,y))
            if(pix == 0):
                flag = 1

        if(flag == 0):
            endTrainingSetImage = y
            break

    #saving mask image with random name

    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    maskImage = trainingSetImage.crop((0,startTrainingSetImage,trainingSetImage.size[0],endTrainingSetImage))
    maskImage.save("./maskImages/"+random_string+".gif")    
