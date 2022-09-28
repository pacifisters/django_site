from django.contrib import admin
from app_site.models import CarouselHead, CarouselTrainer, Menu, TitleShortcutIcon, Contacts, Feedback, ClubFoto, Faq, Filial


class ContactsInline(admin.TabularInline):
    model = Contacts


class CarouselTrainerInline(admin.TabularInline):
    model = CarouselTrainer


class CarouselHeadInline(admin.TabularInline):
    model = CarouselHead


class TitleShortcutIconInline(admin.TabularInline):
    model = TitleShortcutIcon

class ClubFotoInline(admin.TabularInline):
    model = ClubFoto

class FaqInline(admin.TabularInline):
    model = Faq

class FilialInline(admin.TabularInline):
    model = Filial


class MenuAdmin(admin.ModelAdmin):
    inlines = [TitleShortcutIconInline, CarouselHeadInline, CarouselTrainerInline,
               ContactsInline, ClubFotoInline, FaqInline, FilialInline]
    list_display = ['item_1', ]
    fieldsets = (
        ('Брэнд и кнопка в шапке', {
            'fields': ('btn_name_menu',),
            'classes': ['collapse']
        }),
        ('Контакты соц.сети', {
            'fields': ('social_img_1', 'social_data_1', 'social_img_2', 'social_data_2', 'tel',),
            'classes': ['collapse']
        }),
        ('Блок приветствие', {
            'fields': ('item_1', 'title_1', 'text_1', 'btn_name_1',),
            'classes': ['collapse']
        }),        
        ('Блок о клубе', {
            'fields': ('item_club', 'title_club', 'text_club',),
            'classes': ['collapse']
        }),
        ('Блок faq', {
            'fields': ('item_faq', 'title_faq',),
            'classes': ['collapse']
        }),
        ('Блок контакты', {
            'fields': ('item_contacts', 'title_contacts',),
            'classes': ['collapse']
        }),
        
        ('футер', {
            'fields': ('footer',),
            'classes': ['collapse']
        })
    )


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'tel', 'email', 'message', 'create_at', ]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Feedback, FeedbackAdmin)
