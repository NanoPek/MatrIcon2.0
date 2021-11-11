import time

import numpy as np
from skimage import io
from sklearn.cluster import KMeans
from skimage.transform import resize


def GetPosColors(image_url: str,nbr_icons_row: int, n_colors: int,save_csv=False,save_img=False):
    original = io.imread(image_url)
    original = resize(original, (nbr_icons_row, nbr_icons_row), anti_aliasing=True)
    io.imsave('resized.jpg', original, quality=100)
    original = io.imread('resized.jpg')
    print("K-Means kernel creation...")
    before = time.time()
    arr = original.reshape((-1, 3))
    kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(arr)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    less_colors = centers[labels].reshape(original.shape).astype(np.uint8)
    after = round(time.time() - before,3)
    print("Kernel created in",after,'s !')

    img_matrice = np.asarray(less_colors)
    all_colors = {}
    w, h, rgb_shape = np.shape(img_matrice)
    for i in range(0, w):
        for j in range(0, h):
            rgb = img_matrice[j][i]
            rgb = tuple(rgb)
            if rgb in all_colors.keys():
                all_colors[rgb].append((i, j))
            else:
                all_colors[rgb] = [(i, j)]

    print(n_colors, "colors palette created !")

    if save_img:
        io.imsave('result.jpg', less_colors, quality=100)
        print('Image saved !')

    if save_csv:
        with open('all_colors.txt','w') as f:
            for key,item in all_colors.items():
                line = str(key) + ';' + str(item) + '\n'
                f.write(line)
    return all_colors
