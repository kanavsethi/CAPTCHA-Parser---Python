from PIL import Image as image

im = image.open("./captchaImages/4.gif")
newIm = image.new("P",im.size,255)
finalIm = image.new("P",im.size,255)

#Creating Binary Image

for y in range(1,im.size[1]-1):
    for x in range(im.size[0]):
        pix = im.getpixel((x,y))
        if(pix==1):
            newIm.putpixel((x,y),0)


#Removing Lines

for y in range(1,im.size[1]-1):
    for x in range(im.size[0]):
        upperpixel = im.getpixel((x,y-1))
        lowerpixel = im.getpixel((x,y+1))
        pix = im.getpixel((x,y))
        if(pix==1 and (pix==upperpixel or pix==lowerpixel)):
            finalIm.putpixel((x,y),0)
       
        

newIm.save("binary1.gif")
finalIm.save("binary2.gif")
