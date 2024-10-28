<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
    <img src='\creations\pixeleted.png' style="height: 25%; width: 25%;" alt="Pixelated Image">
</div>


# HIJIBIJI

Hijibiji is a Bangla word which translates to 'randomly'. This `hijibiji` package creates random things. By things I mean random video, random audio, random image, random points etc. I don't have any idea if this has some real life application. The motivation to create this package came to me when I was random walking in streets of my university campus. So, yeah, here it is. 

## What it generates

- [x] Using the `rand_image()` function of the package images of any dimension with random pixel values can be generated. See an image like this <br> ![here](https://github.com/kmshariat/hijibiji/blob/main/creations/rand_image.png)

- [x] Using the `rand_video()` function of the package animations of any dimension with random pixel values can be generated. See an animation like this <br> ![here](https://github.com/kmshariat/hijibiji/blob/main/creations/rand_video.gif)

- [x] Using the `rand_audio()` function you can see the sound of randomness. Want to know randomness sounds like? Try the package yourself! 

## How to install

```
pip install hijibiji
```

## Requrements

- [x] numpy
- [x] matplotlib
- [x] sounddevice

## Caution! 

The word `random` here doesn't mean actual randomness. The package uses Numpy's random subpackage that uses the  permuted congruential generator-64 (PCG64) algorithm to generate `pseudo random` numbers. 