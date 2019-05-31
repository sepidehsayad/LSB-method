from PIL import Image
from PIL import ImageOps

secret_image = Image.open('new_img.bmp','r')

pixel_value_secret_data = list(secret_image.getdata())

k = input("input k")

k_LSB = int(k)

def pixel_value(list_of_values):
    pixel_val=[]
    for i in list_of_values:
        pixel_val+=[i[0]]

    return pixel_val


new_pixel_value_secret_image=[]
new_pixel_value_secret_image=pixel_value(pixel_value_secret_data)

def convert_pixelvalue_to_binary(pixel_val):
    binary_of_pixel_value=[]
    for i in pixel_val:
        binary_of_pixel_value+=['{0:08b}'.format(i)]

    return binary_of_pixel_value
binary_of_secret_image=[]
binary_of_secret_image=convert_pixelvalue_to_binary(new_pixel_value_secret_image)

#print(binary_of_secret_image[0:5])

def extract_data(binary_of_secret_image,k_LSB):
    list_of_data=[]
    for i in range(len(binary_of_secret_image)):
        list_of_data+=[binary_of_secret_image[i][-k_LSB:]]

    return list_of_data
list_of_data=[]
list_of_data=extract_data(binary_of_secret_image,k_LSB)
print(list_of_data[-15:])



