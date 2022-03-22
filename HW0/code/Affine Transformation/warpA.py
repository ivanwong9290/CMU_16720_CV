import numpy as np

def warp(im, A, output_shape):
    """ Warps (h,w) image im using affine (3,3) matrix A
    producing (output_shape[0], output_shape[1]) output image
    with warped = A*input, where warped spans 1...output_size.
    Uses nearest neighbor interpolation."""
    (h, w) = output_shape

    warped = np.zeros((h, w))
    for i in range(0, h):
        for j in range(0, w):
            det = np.array([i, j, 1]).T
            src = np.linalg.inv(A) @ det
            (x, y, _) = src.astype(int)

            if x < 0 or x >= h:
                warped[i, j] = 0
            elif y < 0 or y >= w:
                warped[i, j] = 0
            else:
                warped[i, j] = im[x, y]

    return warped
