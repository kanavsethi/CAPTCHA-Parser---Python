import requests
from PIL import Image as image
from io import BytesIO

n = int(input("Enter number of images you wish to import in the Captcha Images Directory: "))

for j in range(n):
    
    res = requests.get("https://vtop.vit.ac.in/student/captcha.asp")
    i = image.open(BytesIO(res.content))
    i.save("./captchaImages/"+str(j)+".gif")