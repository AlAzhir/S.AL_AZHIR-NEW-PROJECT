#install pillow if you havent-DONE
#import pillow-DONE
#open up the image we want to resize using python-DONE
#print the current size of that image
#specify the size we wanna change it to
#save the new resized image


from PIL import Image

def resize_image(size1,size2):
    image=Image.open('logo.jpg')
    print(f"Current size:{image.size}")

    resized_image=image.resize(500,500)
    resized_image.save('logo-500.jpeg')
