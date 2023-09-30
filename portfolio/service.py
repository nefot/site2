import os
from io import BytesIO

from PIL import Image, ImageGrab, ImageOps


def compress(image, size):
    fixed_width = size
    # Сжатие изображения до 70% качества

    img = Image.open(f"/home/nefot/Рабочий стол/site2/media/portfolio/images/{image}")
    im = ImageOps.contain(img, (720, 500), method=Image.LANCZOS)


    im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=70)

    return im


def compress_all_img():
    for root, dirs, files in os.walk("/home/nefot/Рабочий стол/site2/media/portfolio/images"):
        for file in files:
            print(file)

            img = compress(file, 100)
            os.remove(f"/home/nefot/Рабочий стол/site2/media/portfolio/images/{file}")
            img.save(f"/home/nefot/Рабочий стол/site2/media/portfolio/images/{file}")
            print(img)


if __name__ == '__main__':
    compress_all_img()
#
# def compress_size(image,size):
#     # указываем фиксированный размер стороны
#     fixed_width = size
#     img = Image.open(image_path)
#     # получаем процентное соотношение
#     # старой и новой ширины
#     width_percent = (fixed_width / float(img.size[0]))
#     # на основе предыдущего значения
#     # вычисляем новую высоту
#     height_size = int((float(img.size[0]) * float(width_percent)))
#     # меняем размер на полученные значения
#     new_image = img.resize((fixed_width, height_size))
#     new_image.show()
#     new_image.save('F:/hello2.png')
#     return new_image
