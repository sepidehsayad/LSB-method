#LSB method
#sepideh sayadkouh

from PIL import Image

host_image = Image.open('baboon512.bmp','r')
#secret_image = Image.open('airplane2.bmp','r')
file = open('secretdata.txt','r')

pixel_value_hostimage = list(host_image.getdata())
#pixel_value_secretimage =list(secret_image.getdata())

print("pixel value hpst :",pixel_value_hostimage[23041])
width, height =host_image.size
#pixel_value_secretimage= [pixel_value_secretimage[i * width:(i + 1) * width] for i in range(height)]


def pixel_value(list_of_values):
    pixel_val=[]
    for i in list_of_values:
        pixel_val+=[i[0]]

    return pixel_val
#print()
#print(new_pixel_value_hostimage)

def size_of_file(file):
    characters = 0
    for line in file:
        characters = characters + len(line)
    return characters

char =size_of_file(file)

def cal_of_k(size_of_file):
    pixels=host_image.size[0]*host_image.size[1]
    #print("pixels",pixels)
    return int(pixels/size_of_file)

k=cal_of_k(char)
print(k)
new_pixel_value_hostimage=[]
new_pixel_value_hostimage=pixel_value(pixel_value_hostimage)
print("pixel value host",new_pixel_value_hostimage[23041])
def convert_pixelvalue_to_binary(pixel_val):
    binary_of_pixel_value=[]
    for i in pixel_val:
        binary_of_pixel_value+=['{0:08b}'.format(i)]

    return binary_of_pixel_value
binary_of_host_image=[]
binary_of_host_image=convert_pixelvalue_to_binary(new_pixel_value_hostimage)
print("binary of host",binary_of_host_image[23041])
#print(len(binary_of_host_image[0]))
#print(type(binary_of_host_image[0]))
file.close()
file=open('secretdata.txt','r')

def list_of_secret_data_k(file):
    linelist = [line.rstrip('\n') for line in file]
    my_lst_str = ''.join(map(str,linelist))
    return my_lst_str

my_lst_str=list_of_secret_data_k(file)

def spilit_value_with_k(string,k):
    list_k=[]
    for i in range(0,len(string),k):
        list_k+=[string[i:i+3]]
    #print(type(list_k[0]))
    return list_k

final_list_secret_data=[]
final_list_secret_data=spilit_value_with_k(my_lst_str,k)
print("secret data final",final_list_secret_data[23041])
#print("host",len(binary_of_host_image))
print("secret",len(final_list_secret_data))     
def LSB(list_secret_data,list_binary_hostimage,k):
    new_pixels=[]
    count=len(list_binary_hostimage[0])-k
    #print("folan",list_binary_hostimage[0][0:count]+list_secret_data[0])
    
    for i in range(0,len(list_secret_data)):
        #if(list_secret_data==[]):
         #   for j in range(len(list_secret_data),len(list_binary_hostimage)+1):
          #      new_pixels +=[list_binary_hostimage[j]]
           # return "its finish"
        #else :
            temp =list_binary_hostimage[i][0:count]+list_secret_data[i]
            new_pixels+=[temp]
    for j in range(len(list_secret_data),len(list_binary_hostimage)):
        new_pixels +=[list_binary_hostimage[j]]
    
    return new_pixels
new_pixels_bin = LSB(final_list_secret_data,binary_of_host_image,k) #new pixels is here !
print("new pixel stegano graphy",new_pixels_bin[23041])
#convert to decimal

def conver_bin_to_decimal(bin_pixles):
    dec_pixels=[]
    for i in bin_pixles:
        dec_pixels+=[int(i,2)]
    return dec_pixels
dec_pixels = conver_bin_to_decimal(new_pixels_bin)
#print(dec_pixels[0:5])
#print(new_pixel_value_hostimage[0:5])
#print(pixel_value_hostimage[0])
def show_new_picture(host_image,pixel_value_hostimage,dec_pixels):
    pixels = host_image.load() # create the pixel map
    #for i in pixel_value_hostimage:  
         #pixel_value_hostimage[i]=(dec_pixels[i],dec_pixels[i],dec_pixels[i])

    for i in range(host_image.size[0]):    # for every col:
        for j in range(host_image.size[1]):    # For every row
             pixels[i,j] = (dec_pixels[i],dec_pixels[i],dec_pixels[i])

    host_image.save("new_img.bmp")
    host_image.show()

show_new_picture(host_image,pixel_value_hostimage,dec_pixels)    


host_image2 = Image.open('new_img.bmp','r')
pixel_value_hostimage2 = list(host_image2.getdata())
print("sec new setan bib",pixel_value_hostimage2[23041])
print("old old pic",pixel_value_hostimage[23041])
