from GetPosColors import GetPosColors
from CheckIcons import CheckIcons
from Comparator import  Comparator
from Builder import Builder

import time
import ast

def Create(nbr_icons_row: int,n_colors: int,final_size: int,must_save_resized_img=False,must_CheckIcons=False):
    begin = time.time()

    all_colors = GetPosColors('test.jpg', nbr_icons_row, n_colors,save_img=must_save_resized_img)

    if must_CheckIcons:
        all_icons_data = CheckIcons(save_csv=True)
    else:
        with open('all_icons_data.txt','r') as f:
            lines = f.readlines()
            all_icons_data = {}
            for line in lines:
                splitted = line.split(';')
                all_icons_data[splitted[0]] = ast.literal_eval(splitted[1])

    matching_icons = Comparator(all_colors, all_icons_data)

    img_result =  Builder(matching_icons, final_size)

    end = round(time.time() - begin, 3)
    print("Total time :", end, 's')
    return img_result

def Initialize(nbr_icons_row: int,n_colors: int,final_size: int):
    Create(nbr_icons_row,n_colors,final_size,must_save_resized_img=True,must_CheckIcons=True)

def GIFCreate(first_frame: int, last_frame: int, step: int, nbr_icons_row: int,final_size: int,must_CheckIcons=False):
    list_gif = []
    real_begin = time.time()
    for i in range(first_frame,last_frame,step):
        list_gif.append(Create(nbr_icons_row,i,final_size,must_CheckIcons=must_CheckIcons))
    print("Beginning GIF creation...")
    list_gif[0].save('./Results/final_gif.gif', save_all=True, append_images=list_gif[1:], optimize=False,
                     duration=400, loop=1)
    real_end = time.time() - real_begin
    print("GIF creatd ! Real total time :", real_end, 's')


if __name__ == "__main__":
    Create(nbr_icons_row=256,n_colors=493,final_size=4096)
    #GIFCreate(first_frame=1,last_frame=32,step=2,nbr_icons_row=256,final_size=1024)