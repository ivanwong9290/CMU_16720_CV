import numpy as np

def SSD(u, v):
    return np.sum((u.flatten()-v.flatten())**2)/(u.shape[0]*u.shape[1])

def align(ch1, ch2):
    min_ssd = 10000000
    shift_row, shift_col = 0, 0
    for i in range(-30, 30):
      for j in range(-30, 30):
        ssd = SSD(ch1, np.roll(np.roll(ch2, i, axis=0), j, axis=1))
        if ssd < min_ssd:
          min_ssd = ssd
          shift_row = i
          shift_col = j
          
    return np.roll(np.roll(ch2, shift_row, axis=0), shift_col, axis=1)

def alignChannels(red, green, blue):
    """Given 3 images corresponding to different channels of a color image,
    compute the best aligned result with minimum abberations

    Args:
      red, green, blue - each is a HxW matrix corresponding to an HxW image

    Returns:
      rgb_output - HxWx3 color image output, aligned as desired"""
      
    aligned_green = align(red, green)
    aligned_blue = align(red, blue)

    return np.dstack((np.dstack((red, aligned_green)), aligned_blue))

