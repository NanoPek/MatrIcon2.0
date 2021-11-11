import ast
from math import sqrt
from PIL import Image



def Builder(matching_icons: dict,res : int,save='result.jpg',show=False):
    total_lenght = 0
    for poss in matching_icons.values():
        total_lenght += len(poss)
    nbr_icons_row = int(sqrt(total_lenght))
    width_icon =  res // nbr_icons_row
    result = Image.new('RGB',(width_icon * nbr_icons_row,width_icon * nbr_icons_row ), color=(255,255,255))
    for icon, pos in matching_icons.items():
        for i_pos in pos:
            real_pos = (i_pos[0]*width_icon,i_pos[1]*width_icon)
            icon_image = Image.open('./Icons/' + icon).resize((width_icon,width_icon))
            result.paste(icon_image,box=(real_pos))
    result.save("./Results/" + save)
    if show:
        result.show()
    return result



if __name__ == "__main__":
    Builder({},2048)