
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('', bosh_sahifa),
    path('kitoblar/', kitoblar),
    path('w_books/', ayollar_kitoblari),
    path('c_books/', k_soni),
    path('kitob/<int:son>/', bitta_kitob),
    path('author/', h_mualliflar),
    path('muallif/<int:son>/', bitta_muallif),
    path('records/', h_recordlar),
    path('t_mualliflar/', t_mualliflar),
    path('sahifalar/', eng_kop_sahifa),
    path('talabalar/', talabalar),
    path('kutubxonachilar/', h_kutubxonachi),
    path('talaba_edit/<int:pk>/', talaba_update),
    path('kitob_edit/<int:pk>/', kitob_update),
    path('muallif_edit/<int:pk>/', muallif_update),
    path('badiy_kitoblar/', badiy_kitoblar),
    path('oldest_authors/', eng_yoshi_kattalar),
    path('author_delete/<int:son>/', muallif_ochir),
    path('record_edit/<int:pk>/', record_update),


]
