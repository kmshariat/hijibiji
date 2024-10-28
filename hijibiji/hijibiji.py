import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sounddevice as sd

# font setup
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'



def rand_image(dim, cmap):

    """
    The function makes a two dimensional image 
    with random pixel values

    Parameters:

    dim     : Dimension of the image
    cmap    : colormap mode e.g. 'viridis', 'gray'

    Returns:

    Two dimensional image with random pixel values
    """

    img = np.random.rand(dim[0], dim[1])
    plt.imshow(img, cmap=cmap, interpolation='nearest')
    plt.title(f"Random {dim[0]}x{dim[1]} Image")
    plt.show()




def rand_video(dim, num_frames, cmap):

    """
    The function makes an animation/video
    with pixel values changing randomly

    Parameters:

    dim         : Dimension of the video
    num_frames  : No. of frames
    cmap        : Colormap mode e.g. 'viridis', 'gray'

    Returns:

    An animation/video of randomly changing pixel colors
    """

    fig, ax = plt.subplots()
    image = np.random.rand(*dim)
    im = ax.imshow(image, cmap=cmap, interpolation='nearest')
    
    def update(frame):
        new_image = np.random.rand(*dim)
        im.set_array(new_image)
        return [im]

    ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=100)
    
    plt.xticks([])
    plt.yticks([])
    plt.title("Random Pixel Animation")
    plt.show()




def rand_audio(duration=0.3, num_tones=5, min_freq=200, max_freq=2000, sample_rate=42000):
    
    """
    The function generates
    random audio to hear
    
    Parameters:

    duration    : Duration of each tone in seconds
    num_tones   : Number of random tones to generate
    min_freq    : Minimum frequency of generated tones
    max_freq    : Maximum frequency of generated tones
    sample_rate : Sampling rate

    Returns:

    Audio with random tones
    """

    for i in range(num_tones):

        freq = np.random.uniform(min_freq, max_freq)
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        tone = 0.5 * np.sin(2 * np.pi * freq * t)
        
        sd.play(tone, samplerate=sample_rate)
        sd.wait() 



def rand_points(num_points, range_x, range_y):

    """
    The function makes a pyplot of 
    randomly scattered points in some range

    Parameters:

    num_points  : No. of scattered points
    range_x     : Range of numbers along x axis
    range_y     : Range of numbers along y axis

    Returns:

    A pyplot with randomly scattered points inside a range
    """

    x = np.random.uniform(range_x[0], range_x[1], num_points)
    y = np.random.uniform(range_y[0], range_y[1], num_points)
    
    plt.scatter(x, y, color='#018c65', marker='+')
    plt.xticks([range_x[0], range_x[-1]])
    plt.yticks([range_y[0], range_y[-1]])
    plt.title("Randomly Scattered Points")
    plt.show()




def rand_dots(num_points, range_x, range_y, size_range=[50,500]):

    
    """
    The function makes a pyplot of 
    randomly scattered dots with random sizes

    Parameters:

    num_points  : No. of scattered dots
    range_x     : Range of numbers along x axis
    range_y     : Range of numbers along y axis

    Returns:

    A pyplot with randomly scattered points inside a range
    """

    x = np.random.uniform(range_x[0], range_x[1], num_points)
    y = np.random.uniform(range_y[0], range_y[1], num_points)

    sizes = np.random.uniform(size_range[0], size_range[1], num_points)
    colors = np.random.rand(num_points)  
    
    plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7, edgecolor="black")
    plt.xticks([range_x[0], range_x[-1]])
    plt.yticks([range_y[0], range_y[-1]])
    plt.title("Randomly Scattered Dots")
    plt.show()

rand_image([16, 20], 'viridis')