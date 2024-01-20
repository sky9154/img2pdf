from PIL import Image
from os.path import join, basename
from os import listdir
from tqdm import tqdm


def img2pdf (self, path, save_path) -> str:
  self.setWindowTitle('圖片轉換中')

  folder = basename(path)
  pdf_path = join(save_path, f'{folder}.pdf')

  image_list = []

  for image in listdir(path):
    try:
      if Image.open(join(path, image)):
        image_list.append(join(path, image))
    except Exception:
      pass

  sources = [Image.open(file).convert('RGB') for file in tqdm(image_list, desc=folder)]

  sources[0].save(pdf_path, 'pdf', save_all=True, append_images=sources[1:])