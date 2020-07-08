import imageio


def create_gif(image_list, gif_name, duration=7):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration) # fps

