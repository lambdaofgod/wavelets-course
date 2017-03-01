from numpy import sqrt
import pywt
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

gray_plotter = lambda img: plt.imshow(img, cmap='gray', vmax = 255, vmin=0)

def plot_linear_layout(imgs, plotter = gray_plotter):
  N = len(imgs)
  gs = GridSpec(1, N)
  gs.update(wspace=0, hspace=0)
  plot_with_gs(imgs, gs, plotter, N)

def plot_rectangular_layout(imgs, plotter = gray_plotter):
  N = len(apxs)
  n = int(sqrt(len(imgs)))
  gs = GridSpec(n, n)
  gs.update(wspace=0, hspace=0)
  plot_with_gs(imgs, gs, plotter, N)

def plot_with_gs(imgs, gridspec, plotter, N):
  for i in range(N):
    img = imgs[i]
    plt.subplot(gridspec[i])
    plotter(img)
    plt.axis('off')
  plt.show()

