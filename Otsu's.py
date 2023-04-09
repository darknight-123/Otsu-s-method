import matplotlib.pyplot as plt
import numpy as np
from skimage import filters
from skimage import exposure
img = plt.imread("one_piece.jpg")
img=img[:,:,1]
val = filters.threshold_otsu(img)
hist, bins_center = exposure.histogram(img)

plt.figure(figsize=(9, 4))
plt.subplot(131)
plt.imshow(img, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(132)
plt.imshow(img < val, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(133)
plt.plot(bins_center, hist, lw=2)
plt.axvline(val, color='k', ls='--')

plt.tight_layout()
plt.show()


print(np.array(img < val))