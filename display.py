import BBP
from PIL import Image, ImageOps, ImageTk
from tqdm import tk
from tqdm.gui import trange, tqdm
import os
import random
import tkinter as tkin
import tkinter.ttk as ttk

import time

class tk_display:
    def __init__(self,wn_size):
        self.wn = tkin.Tk()
        self.wn.title('Pi')
        
        self.canvas = tkin.Canvas(self.wn,width=wn_size*10,height=wn_size*10)
        self.canvas.pack()
    
    
    def display_progress(self,i: int):              
        return tk.ttkrange(i,tk_parent=self.wn)
    
    def diplay_final_product(self,img: Image):
        resize = img.resize((img.width*5,img.height*5))
        new_image = ImageTk.PhotoImage(resize)
            
        self.canvas.create_image((0,0),image=new_image,anchor='nw')
        self.canvas.update()
        self.wn.attributes("-topmost", True)
        time.sleep(3)
        
    
    def update_screen(self,img: Image):
        resize = img.resize((img.width*5,img.height*5))
        new_image = ImageTk.PhotoImage(resize)
            
        self.canvas.create_image((0,0),image=new_image,anchor='nw')
        self.wn.update()
        
    def close(self):
        self.wn.destroy()

if not os.path.isdir('display/'):
    os.mkdir('display/')

for i in range(50,200): 
    WIDTH = HEIGHT = i
    is_random = False
    no_digits_of_pi = (WIDTH*HEIGHT*3)+7
    print('---Calulating PI---')
    print(f'\nDecimal places -> {no_digits_of_pi}\n')
    with open('pi.txt','a'):
        pass
    with open('pi.txt','r') as pi_file:
        pi_number = pi_file.read()
        print(len(pi_number))
        if no_digits_of_pi < len(pi_number):
            pi = pi_number[2:no_digits_of_pi]

        else:
            pi_file.close()
            with open('pi.txt','w') as new_pi:
                pi = BBP.get_digits_of_pi(no_digits_of_pi)
                new_pi.write(pi)
                
    img = Image.new(mode='RGB', size=(WIDTH,HEIGHT))
    num = 3

    print('\n\n---Creating Image---\n')
    for i in range(0,4):
        num = 3
        match i:
            case 0:
                colour_mode = 'All'
            case 1:
                colour_mode = 'Blue'
            case 2:
                colour_mode = 'Green'
            case 3:
                colour_mode = 'Red'

        # for row in tk.ttkrange(WIDTH):

        display = tk_display(WIDTH)
        for row in display.display_progress(WIDTH):
            for col in range(HEIGHT):
                if not is_random:
                    hex_1, hex_2, hex_3 = int(pi[num])*28, int(pi[num+1])*28, int(pi[num+2])*28
                else:
                    hex_1, hex_2, hex_3 = int(pi[num])*28+random.randint(-3,3), int(pi[num+1])*28+random.randint(-3,3), int(pi[num+2])*28+random.randint(-3,3)
                
                if colour_mode == 'Red':
                    if hex_1 <= hex_2:
                        hex_1,hex_2 = hex_2,hex_1
                    if hex_2 <= hex_3:
                        hex_2,hex_3 = hex_3,hex_2
                    if hex_1 <= hex_2:
                        hex_1,hex_2 = hex_2,hex_1
                    if hex_2 <= hex_3:
                        hex_2,hex_3 = hex_3,hex_2

                elif colour_mode == 'Green':
                    if hex_1 >= hex_3:
                        hex_1,hex_2 = hex_2,hex_1
                    if hex_2 <= hex_3:
                        hex_2,hex_3 = hex_3,hex_2
                    if hex_1 >= hex_3:
                        hex_1,hex_2 = hex_2,hex_1
                    if hex_2 <= hex_3:
                        hex_2,hex_3 = hex_3,hex_2
                
                elif colour_mode == 'Blue':
                    if hex_1 >= hex_2:
                        hex_1,hex_2 = hex_2,hex_1
                    if hex_2 >= hex_3:
                        hex_2,hex_3 = hex_3,hex_2
                    if hex_1 >= hex_2:
                        hex_1,hex_2 = hex_2,hex_1
                    if hex_2 >= hex_3:
                        hex_2,hex_3 = hex_3,hex_2
                        
                
                        
                img.putpixel(value=(hex_1,hex_2,hex_3),xy=(row,col))
                
                
                num += 3
                for i in range(HEIGHT-1):
                    for j in range(HEIGHT-i-1):
                        if colour_mode == 'Red':
                            if img.getpixel((i,j))[0] >= img.getpixel((i,j+1))[0]:
                                temp = img.getpixel((i,j))
                                img.putpixel((i,j),img.getpixel((j,i+1)))
                                img.putpixel((i,j+1),temp)
                        
                        if colour_mode == 'blue':
                            if img.getpixel((i,j))[2] >= img.getpixel((i,j+1))[2]:
                                temp = img.getpixel((i,j))
                                img.putpixel((i,j),img.getpixel((j,i+1)))
                                img.putpixel((i,j+1),temp)
                                
                        if colour_mode == 'Green':
                            if img.getpixel((i,j))[1] >= img.getpixel((i,j+1))[1]:
                                temp = img.getpixel((i,j))
                                img.putpixel((i,j),img.getpixel((j,i+1)))
                                img.putpixel((i,j+1),temp)
                        
                        if colour_mode == 'All':
                            if img.getpixel((i,j)) >= img.getpixel((i,j+1)):
                                temp = img.getpixel((i,j))
                                img.putpixel((i,j),img.getpixel((j,i+1)))
                                img.putpixel((i,j+1),temp)
                        
            
                for i in range(WIDTH-1):
                    for j in range(WIDTH-i-1):
                        if colour_mode == 'Red':
                            if img.getpixel((j,i))[0] >= img.getpixel((j,i+1))[0]:
                                temp = img.getpixel((j,i))
                                img.putpixel((j,i),img.getpixel((i,j+1)))
                                img.putpixel((j,i+1),temp)
                                
                        if colour_mode == 'Blue':
                            if img.getpixel((j,i))[2] >= img.getpixel((j,i+1))[2]:
                                temp = img.getpixel((j,i))
                                img.putpixel((j,i),img.getpixel((i,j+1)))
                                img.putpixel((j,i+1),temp)
                        
                        if colour_mode == 'Green':
                            if img.getpixel((j,i))[1] >= img.getpixel((j,i+1))[1]:
                                temp = img.getpixel((j,i))
                                img.putpixel((j,i),img.getpixel((i,j+1)))
                                img.putpixel((j,i+1),temp)
                        
                        if colour_mode == 'All':
                            if img.getpixel((j,i)) >= img.getpixel((j,i+1)):
                                temp = img.getpixel((j,i))
                                img.putpixel((j,i),img.getpixel((i,j+1)))
                                img.putpixel((j,i+1),temp)
                img_1 = img
                img_2 = ImageOps.mirror(img_1)
                img_3 = ImageOps.flip(img_2)
                img_4 = ImageOps.flip(img_1)

                full_image = Image.new('RGB',(WIDTH*2,HEIGHT*2))

                full_image.paste(img_3,(0,0))
                full_image.paste(img_4,(WIDTH,0))
                full_image.paste(img_2,(0,HEIGHT))
                full_image.paste(img_1,(WIDTH,HEIGHT))

                display.update_screen(full_image)
                                
        display.diplay_final_product(full_image)
        display.close()
        del display                
                        
        for i in range(HEIGHT-1):
            for j in range(HEIGHT-i-1):
                if colour_mode == 'Red':
                    if img.getpixel((i,j))[0] >= img.getpixel((i,j+1))[0]:
                        temp = img.getpixel((j,i))
                        img.putpixel((i,j),img.getpixel((j,i+1)))
                        img.putpixel((i,j+1),temp)
                    
                if colour_mode == 'blue':
                    if img.getpixel((i,j))[2] >= img.getpixel((i,j+1))[2]:
                        temp = img.getpixel((j,i))
                        img.putpixel((i,j),img.getpixel((j,i+1)))
                        img.putpixel((i,j+1),temp)
                                
                if colour_mode == 'Green':
                    if img.getpixel((i,j))[1] >= img.getpixel((i,j+1))[1]:
                        temp = img.getpixel((j,i))
                        img.putpixel((i,j),img.getpixel((j,i+1)))
                        img.putpixel((i,j+1),temp)
                        
                if img.getpixel((i,j)) < img.getpixel((i,j+1)):
                    temp = img.getpixel((j,i))
                    img.putpixel((i,j),img.getpixel((j,i+1)))
                    img.putpixel((i,j+1),temp)
                        
            
        for i in range(WIDTH-1):
            for j in range(WIDTH-i-1):
                if colour_mode == 'Red':
                    if img.getpixel((j,i))[0] >= img.getpixel((j,i+1))[0]:
                        temp = img.getpixel((i,j))
                        img.putpixel((j,i),img.getpixel((i,j+1)))
                        img.putpixel((j,i+1),temp)
                                
                if colour_mode == 'Blue':
                    if img.getpixel((j,i))[2] >= img.getpixel((j,i+1))[2]:
                        temp = img.getpixel((i,j))
                        img.putpixel((j,i),img.getpixel((i,j+1)))
                        img.putpixel((j,i+1),temp)
                        
                if colour_mode == 'Green':
                    if img.getpixel((j,i))[1] >= img.getpixel((j,i+1))[1]:
                        temp = img.getpixel((i,j))
                        img.putpixel((j,i),img.getpixel((i,j+1)))
                        img.putpixel((j,i+1),temp)
                        
                
                if img.getpixel((j,i)) < img.getpixel((j,i+1)):
                    temp = img.getpixel((i,j))
                    img.putpixel((j,i),img.getpixel((i,j+1)))
                    img.putpixel((j,i+1),temp)
                    
            img_1 = img
            img_2 = ImageOps.mirror(img_1)
            img_3 = ImageOps.flip(img_2)
            img_4 = ImageOps.flip(img_1)

            full_image = Image.new('RGB',(WIDTH*2,HEIGHT*2))

            full_image.paste(img_3,(0,0))
            full_image.paste(img_4,(WIDTH,0))
            full_image.paste(img_2,(0,HEIGHT))
            full_image.paste(img_1,(WIDTH,HEIGHT))

            image_name = "display/"+colour_mode+str(WIDTH)+'x'+str(HEIGHT)+'test.png'
            full_image.save(image_name)
        