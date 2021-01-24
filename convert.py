import sys

from PIL import Image 
from numpy import asarray
import matplotlib
import matplotlib.pyplot as plt

def to_bin(tile):
	ret = ""

	for l in tile:
		d = map(lambda x: "1" if x else "0", l)
		ret += "db " + ",".join(list(d)) + "\n"

	return ret

def show(tiles):
	matplotlib.use("TKAgg")

	fig = plt.figure(figsize=(8, 16))
	for i in range(0, 128):
		fig.add_subplot(8, 16, i + 1)
		plt.imshow(tiles[i])

	plt.show()

#Read in image, convert to 128x128 black and white
img = Image.open(sys.argv[1]).convert("1").resize((128, 128), Image.ANTIALIAS)

#Switch over to array data
data = asarray(img)

#Break into 8x16 tiles
N = 8
M = 16

tiles = [data[x:x+M,y:y+N] for x in range(0,data.shape[0],M) for y in range(0,data.shape[1],N)]

show(tiles)

font_pack = []
tile_map = []

for tile in tiles:
	d = to_bin(tile)
	
	if d in font_pack:
		i = font_pack.index(d)
		tile_map.append(i)
	else:
		font_pack.append(d)
		tile_map.append(len(font_pack) - 1)

print("db " + str(len(font_pack)))
print("\n".join(font_pack))

print("db " + str(len(tile_map)))
print("db " + ", ".join(str(x) for x in tile_map))
