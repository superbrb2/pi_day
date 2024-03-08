import BBP
from PIL import Image, ImageOps
from tqdm import tqdm
import os

# 314 width and height
WIDTH = HEIGHT = int(input('What dimesions?: '))

if not os.path.isdir(str(WIDTH)+'x'+str(HEIGHT)+'/'):
    os.mkdir(str(WIDTH)+'x'+str(HEIGHT)+'/')

print('---Calulating PI---')
print(f'\nDecimal places -> {(WIDTH*HEIGHT*3)+5}\n')
pi = BBP.get_digits_of_pi((WIDTH*HEIGHT*3)+5)
img = Image.new(mode='RGB', size=(WIDTH,HEIGHT))
num = 3

print('\n\n---Creating Image---\n')
for i in range(0,4):
    num = 3
    match i:
        case 0:
            colour_mode = 'Red'
        case 1:
            colour_mode = 'Blue'
        case 2:
            colour_mode = 'Green'
        case 3:
            colour_mode = 'All'

    for row in tqdm(range(WIDTH)):
        for col in range(HEIGHT):
            hex_1, hex_2, hex_3 = int(pi[num])*28, int(pi[num+1])*28, int(pi[num+2])*28
            
            if colour_mode == 'Red':
                if hex_1 <= hex_2:
                    hex_1,hex_2 = hex_2,hex_1
                if hex_2 <= hex_3:
                    hex_2,hex_3 = hex_3,hex_2
                if hex_1 <= hex_2:
                    hex_1,hex_2 = hex_2,hex_1

            elif colour_mode == 'Green':
                if hex_1 >= hex_3:
                    hex_1,hex_2 = hex_2,hex_1
                if hex_2 <= hex_3:
                    hex_2,hex_3 = hex_3,hex_2
                if hex_1 >= hex_3:
                    hex_1,hex_2 = hex_2,hex_1
            
            elif colour_mode == 'Blue':
                if hex_1 >= hex_2:
                    hex_1,hex_2 = hex_2,hex_1
                if hex_2 >= hex_3:
                    hex_2,hex_3 = hex_3,hex_2
                if hex_1 >= hex_2:
                    hex_1,hex_2 = hex_2,hex_1
                    
            img.putpixel(value=(hex_1,hex_2,hex_3),xy=(row,col))
            
            num += 3
            
            for i in range(HEIGHT-1):
                for j in range(HEIGHT-i-1):
                    if img.getpixel((i,j)) < img.getpixel((i,j+1)):
                        temp = img.getpixel((i,j))
                        img.putpixel((i,j),img.getpixel((i,j+1)))
                        img.putpixel((i,j+1),temp)
                    
        
            for i in range(WIDTH-1):
                for j in range(WIDTH-i-1):
                    if img.getpixel((i,j)) < img.getpixel((i,j+1)):
                        temp = img.getpixel((i,j))
                        img.putpixel((j,i),img.getpixel((i,j+1)))
                        img.putpixel((j,i+1),temp)
        
    for i in range(HEIGHT-1):
        for j in range(HEIGHT-1):
            if img.getpixel((i,j)) >= img.getpixel((i,j+1)):
                temp = img.getpixel((i,j))
                img.putpixel((i,j),img.getpixel((i,j+1)))
                img.putpixel((i,j+1),temp)
                    
        
    for i in range(WIDTH-1):
        for j in range(WIDTH-1):
            if img.getpixel((i,j)) >= img.getpixel((i,j+1)):
                temp = img.getpixel((i,j))
                img.putpixel((j,i),img.getpixel((i,j+1)))
                img.putpixel((j,i+1),temp)

    img_1 = img
    img_2 = ImageOps.mirror(img_1)
    img_3 = ImageOps.flip(img_2)
    img_4 = ImageOps.flip(img_1)

    full_image = Image.new('RGB',(WIDTH*2,HEIGHT*2))

    full_image.paste(img_1,(0,0))
    full_image.paste(img_2,(WIDTH,0))
    full_image.paste(img_4,(0,HEIGHT))
    full_image.paste(img_3,(WIDTH,HEIGHT))


    full_image.save(str(WIDTH)+'x'+str(HEIGHT)+'/'+colour_mode+str(WIDTH)+'x'+str(HEIGHT)+'.png')
    

