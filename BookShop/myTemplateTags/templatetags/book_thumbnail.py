from django import template
from PIL import Image, ImageOps
from django.conf import settings
import os


class BookThumbnail():
    def addWatermark(inputImgPath, outputImgPath, watermarkImgPath, size):
        """Метод добавляет водный знак к изображению"""
        baseImg = Image.open(inputImgPath)
        watermarkImg = Image.open(watermarkImgPath)
        width, height = baseImg.size
        watermarkImg.thumbnail(size)
        imgWithWatermark = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        imgWithWatermark.paste(baseImg, (0, 0))
        imgWithWatermark.paste(watermarkImg, (0, height - size[1]), mask=watermarkImg)
        imgWithWatermark.save(outputImgPath, "PNG")

    def myThumbnail(inputImgPath, outputImgPath, size):
        """Метод выполняет маштабирование изображения
            и обрезает его по размеру
        """
        try:
            baseImg = Image.open(inputImgPath)
            newImg = ImageOps.fit(baseImg, size, Image.ANTIALIAS)
            newImg.save(outputImgPath)
            print(outputImgPath)

        except IOError:
            print
            "cannot create thumbnail for", inputImgPath
            return inputImgPath


register = template.Library()


@register.simple_tag()
def book_thumbnail(imgUrl, thumbnailSize = settings.THUMBNAIL_SIZE):
    imgUrl = str(imgUrl)
    saveUrl = str(os.path.join(settings.MEDIA_ROOT, settings.THUMBNAIL_URL)+ os.path.basename(imgUrl))
    print("Save path: " + saveUrl)
    watermarkUrl = os.path.join(settings.STATIC_ROOT, settings.THUMBNAIL_WATERMARK)
    returnImg = '/media/' + str(settings.THUMBNAIL_URL) + os.path.basename(imgUrl)
    print("Return Url img" +returnImg)
    BookThumbnail.myThumbnail(imgUrl, saveUrl, thumbnailSize)
    BookThumbnail.addWatermark(saveUrl, saveUrl, watermarkUrl, (100, 100))
    return returnImg
