from django.db import models
import re

class Feedback(models.Model):
    name = models.TextField()
    tel = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Contacts(models.Model):
    email = models.EmailField()
    adress = models.CharField(max_length=200)
    description = models.TextField(verbose_name='описание как добраться')
    for_script = models.TextField(verbose_name='скрипт для отображения карты, копируем только ссылку https... из яндекс конструктор карт')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)


class TitleShortcutIcon(models.Model):
    title = models.CharField(max_length=100, verbose_name='название сайта (надпись на вкладке)')
    img = models.FileField(upload_to='files/', verbose_name='картинка на вкладке')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)


class CarouselHead(models.Model):
    general_img = models.FileField(
        upload_to='files/', verbose_name='первая картинка в слайдере')
    img_1 = models.FileField(upload_to='files/', verbose_name='вторая картинка в слайдере')
    img_2 = models.FileField(upload_to='files/', verbose_name='третья картинка в слайдере')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)


class CarouselTrainer(models.Model):
    general_img = models.FileField(upload_to='files/', verbose_name='первая картинка в слайдере')
    img_1 = models.FileField(upload_to='files/', verbose_name='вторая картинка в слайдере')
    img_2 = models.FileField(upload_to='files/', verbose_name='третья картинка в слайдере')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

class ClubFoto(models.Model):    
    foto = models.FileField(upload_to='files/', verbose_name='foto')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

class Faq(models.Model):
    q_faq = models.CharField(max_length=255, verbose_name='вопрос') 
    a_faq = models.CharField(max_length=255, verbose_name='ответ')  
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

class Filial(models.Model):
    filial = models.CharField(max_length=255, verbose_name='название филиала')
    adr = models.CharField(max_length=255, verbose_name='адрес филиала') 
    way = models.CharField(max_length=255, verbose_name='как добраться до филиала')     
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)



class Menu(models.Model):    
    btn_name_menu = models.CharField(max_length=100, blank=True, verbose_name='надпись на кнопке в шапке')
    item_1 = models.CharField(max_length=100, blank=True, verbose_name='имя ссылки в меню')
    title_1 = models.CharField(max_length=100, blank=True, verbose_name='заголовок блока')
    text_1 = models.TextField(verbose_name='текст блока')
    btn_name_1 = models.CharField(max_length=100, blank=True, verbose_name='надпись на кнопке в блоке')    
    item_club = models.CharField(max_length=100, blank=True, verbose_name='имя ссылки в меню')
    title_club = models.CharField(max_length=100, blank=True, verbose_name='заголовок блока')
    text_club = models.TextField(verbose_name='текст блока')
    item_faq = models.CharField(max_length=100, blank=True, verbose_name='имя ссылки в меню')
    title_faq = models.CharField(max_length=100, blank=True, verbose_name='заголовок блока')      
    item_contacts = models.CharField(max_length=100, blank=True, verbose_name='имя ссылки в меню')
    title_contacts = models.CharField(max_length=100, blank=True, verbose_name='заголовок блока')
    social_img_1 = models.FileField(upload_to='files/', verbose_name='иконка соц.сети')
    social_data_1 = models.CharField(max_length=100, blank=True, verbose_name='ссылка на соц.сеть')
    social_img_2 = models.FileField(upload_to='files/', verbose_name='иконка соц.сети')
    social_data_2 = models.CharField(max_length=100, blank=True, verbose_name='ссылка на соц.сеть')
    tel = models.CharField(max_length=100, verbose_name='поле для телефонного номера, вводить в красивом формате, пример:+7 (955) 893-23-22')
    tel_for_call = models.CharField(max_length=100, blank=True)
    footer = models.TextField(verbose_name='текст футер')

    def __str__(self):
        return self.item_1

    def save(self, *args, **kwargs):
        self.tel_for_call = None
        number = self.tel
        normal_number = re.findall(r"[^ ()-]", number)
        self.tel_for_call = str('').join(map(str, normal_number))
        return super(Menu, self).save(*args, **kwargs)
