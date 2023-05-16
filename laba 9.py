from PIL import Image, ImageFilter
import os

def lab9192():

    x = ["1.png","2.jpg","3.png","4.jpg","5.png"]
    count = 0
    for file in x:
        if file.endswith('.jpg') or file.endswith('.png'):
            count += 1
            img = Image.open(file)
            newimg = img.filter(ImageFilter.EMBOSS)
            newimg.show()
            try:
                os.mkdir("D:/Вузовское/Алгоритмитизация/1 курс, 2 семестр/9lab/kkk")
            except:
                pass
            newimg.save(f"В:/Вузовское/Алгоритмитизация/1 курс, 2 семестр/9lab/kkk/new_img{count}.png")

def lab93():
    rez = 0
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        print("Нужно купить: ")
        for line in lines[1:]:
            product, quantity, price = line.strip().split(',')
            rez += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")
        print(f"Итоговая сумма: {rez} руб.")

