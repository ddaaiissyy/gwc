from PIL import Image

def load_img(x):
    img = Image.open(x)
    return img

def show_img(img):
    img.show()

def save_img(img_object, img):
    img_object.save(img)

img = load_img("obama.jpg")
show_img(img)
save_img(img, "obama2.jpg")

#should return a new image object with filter applied 
def obamicon(img_object):
    #  create new empty list which you will put all new pixel values into (HINT: USE APPEN)
     
     
    original_pixel = img_object.getdata()
    # use for loop to iterate through every single pixel
    # at every pixel, sum up the RGB values 
    # use conditionals and boolean checks to determine which new color to change to 