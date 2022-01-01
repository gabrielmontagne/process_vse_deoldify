from deoldify import device
from deoldify.device_id import DeviceId
from xyy import process_frame, start_server
import deoldify
import fastai
import warnings
from IPython import embed
from deoldify.visualize import torch, get_image_colorizer


def initialize():
    device.set(device=DeviceId.CPU)
    torch.backends.cudnn.benchmark=True
    warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
    colorizer = get_image_colorizer(artistic=True)

    @process_frame
    def deoldify_pixels(pixs, config):
        render_factor = int(config.get('xyy_render_factor', 35))
        image_path = config.get('image_path')
        print(f'DeOldify image {image_path} with render_factor {render_factor}')
        return colorizer.get_transformed_image(
            path=image_path,
            render_factor=render_factor,
            watermarked=False
        )

def main():
    initialize()
    start_server()
    print('running module process_vse_deoldify')


if __name__ == '__main__':
    main()
