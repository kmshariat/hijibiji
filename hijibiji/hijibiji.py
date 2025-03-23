import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sounddevice as sd


def rand_image(dim, cmap):

    """
    The function makes a two dimensional image 
    with random pixel values

    Parameters:

    dim     :   list
                Dimension of the image

    cmap    :   string
                colormap mode e.g. 'viridis', 'gray'

    Returns:
                None
                Two dimensional image with random pixel values
    """

    if len(dim) != 2 or any(d <= 0 for d in dim):
        raise ValueError("Dimension must be a list of two positive integers.")

    img = np.random.rand(dim[0], dim[1])
    plt.imshow(img, cmap=cmap, interpolation='nearest')
    plt.title(f"Random {dim[0]}x{dim[1]} Image")
    plt.show()




def rand_video(dim, num_frames, cmap):

    """
    The function makes an animation/video
    with pixel values changing randomly

    Parameters:

    dim         :   list 
                    Dimension of the video

    num_frames  :   int
                    No. of frames

    cmap        :   string
                    Colormap mode e.g. 'viridis', 'gray'

    Returns:
                    None
                    An animation/video of randomly changing pixel colors
    """
    if len(dim) != 2 or any(d <= 0 for d in dim):
        raise ValueError("Dimension must be a list of two positive integers.")

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

    duration    :   float
                    Duration of each tone in seconds

    num_tones   :   int
                    Number of random tones to generate

    min_freq    :   int
                    Minimum frequency of generated tones

    max_freq    :   int
                    Maximum frequency of generated tones

    sample_rate :   int
                    Sampling rate

    Returns     :
                    None
                    Audio with random tones
    """

    if sample_rate < 40000:
        raise ValueError("Sampling Rate must be greater than 40000 to avoid alias according to Nyquist-Shannon Theorem")

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

    num_points  :   int
                    No. of scattered points

    range_x     :   list
                    Range of numbers along x axis

    range_y     :   list
                    Range of numbers along y axis

    Returns     :   None
                    A pyplot with randomly scattered points inside a range
    """

    if len(range_x) != 2 and len(range_y) != 2:
        raise ValueError("The ranges must have both upper and lower limit as a list")

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

    if len(range_x) != 2 and len(range_y) != 2:
        raise ValueError("The ranges must have both upper and lower limit as a list")

    x = np.random.uniform(range_x[0], range_x[1], num_points)
    y = np.random.uniform(range_y[0], range_y[1], num_points)

    sizes = np.random.uniform(size_range[0], size_range[1], num_points)
    colors = np.random.rand(num_points)  
    
    plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7, edgecolor="black")
    plt.xticks([range_x[0], range_x[-1]])
    plt.yticks([range_y[0], range_y[-1]])
    plt.title("Randomly Scattered Dots")
    plt.show()

def rand_walk_1d(num_walkers, num_steps):
        
        """
        The function simulates and plots 1D random walks.

        Parameters:

        num_walkers : int
                      Number of walkers
        num_steps   : int
                      Number of steps for each walker

        Returns:
        None
        """
        fig, ax = plt.subplots()
        
        for _ in range(num_walkers):
            x = [0]
            for _ in range(num_steps):
                dx = np.random.choice([-1, 1])
                x.append(x[-1] + dx)
            ax.plot(x, alpha=0.6)

        plt.title(f"{num_walkers} Random Walkers with {num_steps} Steps in 1D")
        plt.xlabel("Steps")
        plt.ylabel("Position")
        plt.show()

def rand_walk_2d(num_walkers, num_steps):
        """
        The function simulates and plots 2D random walks.

        Parameters:
        num_walkers : int
                      Number of walkers
        num_steps   : int
                      Number of steps for each walker

        Returns:
        None
        """
        fig, ax = plt.subplots()
        
        for _ in range(num_walkers):
            x, y = [0], [0]
            for _ in range(num_steps):
                dx, dy = np.random.choice([-1, 1]), np.random.choice([-1, 1])
                x.append(x[-1] + dx)
                y.append(y[-1] + dy)
            ax.plot(x, y, alpha=0.6)

        plt.title(f"{num_walkers} Random Walkers with {num_steps} Steps")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()    


def rand_walk_3d(num_walkers, num_steps):
    """
    The function simulates and plots 3D random walks.

    Parameters:
    num_walkers : int
                  Number of walkers
    num_steps   : int
                  Number of steps for each walker

    Returns:
    None
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for _ in range(num_walkers):
        x, y, z = [0], [0], [0]
        for _ in range(num_steps):
            dx, dy, dz = np.random.choice([-1, 1]), np.random.choice([-1, 1]), np.random.choice([-1, 1])
            x.append(x[-1] + dx)
            y.append(y[-1] + dy)
            z.append(z[-1] + dz)
        ax.plot(x, y, z, alpha=0.6)

    plt.title(f"{num_walkers} Random Walkers with {num_steps} Steps in 3D")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    plt.show()