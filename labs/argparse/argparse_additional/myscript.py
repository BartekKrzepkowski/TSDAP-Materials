import argparse
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
from skimage import io

parser = argparse.ArgumentParser()
parser.add_argument('--inputfile', type=str, required=True)
parser.add_argument('--x', type=int)
parser.add_argument('--y', type=int)
parser.add_argument('--xy', type=int)

args = parser.parse_args()


def gaussian_smooth(inputfile, x, y, xy):
    image = io.imread(inputfile)
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    if not (x or y or xy):
        sigma = 2
    if xy:
        sigma = xy
    elif x and y:
        sigma = (x, y)
    filtered_img = gaussian_filter(image, sigma)
    plt.figure(figsize=(10, 10))
    plt.imshow(filtered_img)
    plt.show()

if __name__ == '__main__':
    gaussian_smooth(args.inputfile, args.x, args.y, args.xy)