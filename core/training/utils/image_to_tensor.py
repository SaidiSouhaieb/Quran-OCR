import torch
from PIL import Image
import torchvision.transforms as transforms


def convert_image_to_tensor(image_path):
    # Read a PIL image
    image = Image.open(image_path).convert("L")

    transform = transforms.Compose([transforms.PILToTensor()])
    img_tensor = transform(image)

    img_tensor = img_tensor.permute(1, 2, 0)

    return img_tensor
