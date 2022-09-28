from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import FormMixin
from app_site.models import CarouselHead, Menu, CarouselTrainer, TitleShortcutIcon, Contacts, ClubFoto, Faq, Filial
from app_site.forms import FeedbackForm
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail


class FileDetail(FormMixin, ListView):
    model = CarouselHead
    template_name = 'index.html'
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.get()
        context['carousel'] = CarouselHead.objects.get()
        context['carousel_trainer'] = CarouselTrainer.objects.get()        
        context['title_icon'] = TitleShortcutIcon.objects.get()
        context['contacts'] = Contacts.objects.get()
        context['fotos'] = ClubFoto.objects.all() 
        context['foto1'] = ClubFoto.objects.get(pk=1)           
        context['faqs'] = Faq.objects.all()
        context['filials'] = Filial.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.get_form()

    def form_valid(self, form):
        form.save()
        message = str(f"{form.cleaned_data['name']} спрашивает: {form.cleaned_data['message']}, контакты: {form.cleaned_data['tel']} , {form.cleaned_data['email']}")
        send_mail('Сообщение с сайта', message, settings.EMAIL_HOST_USER, ['pacifisters@gmail.com'])
        return super().form_valid(form)
