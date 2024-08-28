import matplotlib.pyplot as plt
import numpy as np
import pyhighmap as hmap

if __name__ == "__main__":
    shape = [256, 128]  # out numpy array shape
    frequency = [4, 2]  # spatial frequencies
    seed = 0  # random seed number

    print('Available functions')
    for s in dir(hmap):
        obj = getattr(hmap, s)
        if (not s.startswith('__')) and callable(obj):
            print(' - {}'.format(s))

    print('Available base noises\n', [s for s in dir(hmap.NoiseType) \
                                      if not s.startswith('__')])

    # generate Perlin (output is a 2D numpy array)
    noise_base = hmap.noise(hmap.NoiseType.PERLIN, shape, frequency, seed)

    # fractal layering
    noise_fbm = hmap.noise_fbm(hmap.NoiseType.SIMPLEX2S, shape, frequency, seed)

    noise_fbm = hmap.noise_pingpong(
        hmap.NoiseType.SIMPLEX2S, shape, frequency, seed
    )

    noise_fbm = hmap.noise_ridged(hmap.NoiseType.PERLIN, shape, frequency, seed)

    # remap amplitude interval to [0, 1]
    noise_fbm = hmap.remap(noise_fbm)

    # apply filters

    # noise_base = hmap.remap(noise_base)
    # noise_base = hmap.clamp(noise_base, vmin=0.3, vmax=0.7)

    noise_base = hmap.warp(noise_base, 0.1 * noise_fbm, 0.1 * noise_fbm)

    # noise_fbm = hmap.plateau(noise_fbm, ir=16, factor=1.5)
    # noise_fbm = hmap.smooth_fill(noise_fbm, ir=32, k=0.1)
    noise_fbm = hmap.falloff(noise_fbm)

    plt.figure()
    plt.imshow(noise_base, cmap='jet')

    plt.figure()
    plt.imshow(noise_fbm, cmap='terrain')

    plt.show()
