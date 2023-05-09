from PIL import Image


def lab81():
    im = Image.open('деп.jpg')
    im_crop = im.crop((10, 10, 300, 400))
    im_crop.save('new.jpg')
    im_crop.show()


def lab82():
    spisok = {"День победы": "деп.jpg", "Праздник всех женщин": "конецсвета.jpg", "Новый год": "нг.jpg",
              "День рождение": "др.jpg"}
    vopr = input("Какой сейчас праздник? ")
    if vopr in spisok:
        image = Image.open(spisok[vopr])
        image.show()
    else:
        print("Такой открытки нет, попробуйте еще раз")


def lab83():
    from PIL import Image, ImageDraw, ImageFont

    name = input("Введите имя получателя: ")
    filename = "др.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("arial.ttf", 30)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 100, 15),
        name + "- самый лучший",
        font=font,
        fill=('red')
    )
    img.show()
