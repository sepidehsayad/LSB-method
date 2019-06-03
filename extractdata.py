from PIL import Image
from PIL import ImageOps

secret_image = Image.open('new_img.bmp','r')

pixel_value_secret_data = list(secret_image.getdata())
#print(pixel_value_secret_data)
k = input("input k :")
if 1<= int(k) <= 4 :
    print("it okay,see scret data")
else :
    print("enter another k")

    
k_LSB = int(k)



def convert_pixelvalue_to_binary(pixel_val):
    binary_of_pixel_value=[]
    for i in pixel_val:
        binary_of_pixel_value+=['{0:08b}'.format(i)]

    return binary_of_pixel_value
binary_of_secret_image=[]
binary_of_secret_image=convert_pixelvalue_to_binary(pixel_value_secret_data)
#print(binary_of_secret_image[0:30])

#print(binary_of_secret_image[0:5])

def extract_data(binary_of_secret_image,k_LSB):
    list_of_data=[]
    for i in range(len(binary_of_secret_image)):
        list_of_data+=[binary_of_secret_image[i][-k_LSB:]]

    return list_of_data


def one_string(list_of_data):
    string =''
    for i in list_of_data :
        string+=i
    #print(string)
    return string

def spilit_string(string,pix_8_):
    list_k=[]
    for i in range(0,len(string),pix_8_):
        list_k+=[string[i:i+pix_8_]]

    
    return list_k
    
    

def show_new_picture(dec_pixels):
    img = Image.new('L', (512,256))
    img.putdata(dec_pixels)
    img.save("new__img.bmp")
    img.show()

def conver_bin_to_decimal(bin_pixles):
    dec_pixels=[]
    for i in bin_pixles:
        dec_pixels+=[int(i,2)]
    return dec_pixels


list_of_data=[]
list_of_data=extract_data(binary_of_secret_image,k_LSB)
string_of_pixels = one_string(list_of_data)
#print("len",string_of_pixels)
spili_string=[]
spili_string=spilit_string(string_of_pixels,8)
dec_pixels = conver_bin_to_decimal(spili_string)
show_new_picture(dec_pixels)
#print(dec_pixels[0:30])
#print(spili_string[0:30])
#print(list_of_data[0:30])
#print(list_of_data[0:69125])




