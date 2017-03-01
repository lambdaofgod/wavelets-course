from numpy import sqrt
import pywt
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def plot_wavelet_approximations(apxs):
  N = len(apxs)
  n = int(sqrt(len(apxs)))
  gs = GridSpec(n, n)
  gs.update(wspace=0, hspace=0)

  for i in range(N):
    img = apxs[i]
    plt.subplot(gs[i])
    plt.imshow(img, cmap='gray')
    plt.axis('off')
  plt.show()
