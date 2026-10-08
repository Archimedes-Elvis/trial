import numpy as np

# a tiny 3x3 image (values 0-255)
image = np.array([[100, 120, 130],
                  [200, 210, 220],
                  [50, 60, 70]])

print("Original:\n:", image)
print()
print('First row:', image[0])
print()
print("Center pixel:", image[1,1])
print()
print("Brightened by 20:", image + 20)
print()
print("Crop top-left by 2x2", image[0:2, 0:2])
print()

# challenge: make all pixels < 100 become 0
image[image < 100] = 0
print(image)

