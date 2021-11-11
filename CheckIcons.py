import os
from skimage import io
from sklearn.cluster import KMeans

def CheckIcons(save_csv=False):
    all_icons_data = {}
    for (r, d, f) in os.walk('./Icons'):
        f.remove('.gitignore')
        for icon_file in f:
            original = io.imread('./Icons/' + icon_file)
            arr = original.reshape((-1, 3))
            kmeans = KMeans(n_clusters=1, random_state=42).fit(arr)
            centers = kmeans.cluster_centers_[0]
            r,g,b = int(round(centers[0],0)),int(round(centers[1],0)),int(round(centers[2],0))
            all_icons_data[icon_file] = (r,g,b)
    if save_csv:
        with open('all_icons_data.txt','w') as f:
            for key,item in all_icons_data.items():
                line = str(key) + ';' + str(item) + '\n'
                f.write(line)
    return all_icons_data
