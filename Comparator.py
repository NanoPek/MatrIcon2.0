
def Comparator(all_colors: dict ,all_icons_data: dict,save_csv=False):
    matching_icons = {}
    for color ,pos in all_colors.items():
        best = 256 * 3
        best_icon = ''
        for icon ,dom_color in all_icons_data.items():
            color_diff = abs(color[0] - dom_color[0]) + abs(color[1] - dom_color[1]) + abs(color[2] - dom_color[2])
            if color_diff < best:
                best = color_diff
                best_icon = icon
        if best_icon in matching_icons.keys():
            for i_pos in pos:
                matching_icons[best_icon].append(i_pos)
        else:
            matching_icons[best_icon] = pos

    if save_csv:
        with open('matching_icons.txt','w') as f:
            for key,item in matching_icons.items():
                line = str(key) + ';' + str(item) + '\n'
                f.write(line)

    return matching_icons
