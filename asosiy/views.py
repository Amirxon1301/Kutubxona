from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def salomlash(request):
    return HttpResponse("Salom, Dunyo")

def bosh_sahifa(request):
    return render(request, 'home.html')

def kitoblar(request):
    if request.method == "POST":
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
        # Kitob.objects.create(
        #     nom=request.POST.get("n"),
        #     janr=request.POST.get("janr"),
        #     sahifa=request.POST.get("s"),
        #     muallif=Muallif.objects.get(id=request.POST.get("muallif"))
        #
        # )
        return redirect("/kitoblar/")
    data = {
        "books" : Kitob.objects.all(),
        "mualliflar" : Muallif.objects.all(),
        "form" : KitobForm()
    }
    return render(request, 'kitoblar.html', data)

def ayollar_kitoblari(request):
    data = {
        "w_books" : Kitob.objects.filter(muallif__jins='Ayol')
    }
    return render(request, 'mashq/ayollar_kitoblari.html', data)

def k_soni(request):
    data = {
        "c_book" : Kitob.objects.filter(muallif__kitoblar_soni__lt=10)
    }
    return render(request, 'mashq/k_soni.html', data )

def bitta_kitob(request, son):

    data= {
        "kitob" : Kitob.objects.get(id=son)
    }
    return render(request, 'mashq/kitob.html', data)

def h_mualliflar(request):
    if request.method == "POST":
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            forma.save()
        # Muallif.objects.create(
        #     ism=request.POST.get("ismi"),
        #     jins=request.POST.get("jinsi"),
        #     kitoblar_soni=request.POST.get("k_s"),
        #     tugilgan_yil=request.POST.get("t_y"),
        #     tirik=request.POST.get("t") == "on"
        # )
        # return redirect("/author/")

    data = {
        "author" : Muallif.objects.all(),
        "forma" : MuallifForm()
    }
    return render(request, 'Mualliflar.html', data)

def bitta_muallif(request, son):
    data = {
        "muallif" : Muallif.objects.get(id=son)
    }
    return render(request,'mashq/muallif.html', data)

def h_recordlar(request):
    data = {
        "records" : Record.objects.all()
    }
    return render(request,'recordlar.html', data)

def t_mualliflar(request):
    data = {
        "t_mualliflar" : Muallif.objects.filter(tirik=True)
    }
    return render(request, 'mashq/tirik_mualliflar.html', data)

def eng_kop_sahifa(request):
    data = {
        "sahifalar" : Kitob.objects.order_by('-sahifa')[:3]
    }
    return render(request, 'mashq/eng_kop_sahifalar.html', data)

def badiy_kitoblar(request):
    data = {
        "badiy_kitoblar" : Kitob.objects.filter(janr="Badiiy")
    }
    return render(request, "mashq/badiy_kitob.html", data)

def eng_yoshi_kattalar(request):
    data = {
        "eng_yoshi_kattalar" : Muallif.objects.all().order_by('tugilgan_yil')[:3]

    }
    return render(request, "mashq/eng_yoshi_kattalar.html", data)
def talabalar(request):
    if request.method == "POST":
        form = TalabaForm(request.POST)
        if form.is_valid():
            Talaba.objects.create(
                ism = form.cleaned_data.get("i"),
                kurs = form.cleaned_data.get("k"),
                kitoblar_soni = form.cleaned_data.get("k_s")
            )
        # Talaba.objects.create(
        #     ism=request.POST.get("ismi"),
        #     kurs=request.POST.get("k"),
        #     kitoblar_soni=request.POST.get("k_s"),
        # )
        return redirect("/talabalar/")
    content = {
        "talabalar": Talaba.objects.all(),
        "form" : TalabaForm()
    }
    return render(request, 'talabalar.html', content)

def bitta_record(request, pk):
    data = {
        "record" : Record.objects.get(id=pk)
    }

def talaba_update(request, pk):
    if request.method == "POST":
        Talaba.objects.filter(id=pk).update(
            kurs=request.POST.get("k"),
            kitoblar_soni=request.POST.get("k_s"),
        )
        return redirect("/talabalar/")
    data = {
        "talaba" : Talaba.objects.get(id=pk)
    }
    return render(request, 'talaba_update.html', data)

def kitob_update(request, pk):
    if request.method == "POST":
        Kitob.objects.filter(id=pk).update(
            janr=request.POST.get("j"),
            sahifa=request.POST.get("s"),
            muallif=Muallif.objects.get(id=request.POST.get("m"))
        )
        return redirect("/kitoblar/")
    data = {
        "kitob" : Kitob.objects.get(id=pk),
        "mualliflar" : Muallif.objects.all(),
        "janrlar" : ["Badiiy", "Ilmiy", "Hujatli"]
    }
    return render(request, 'kitob_update.html', data)

def muallif_update(request, pk):
    if request.method == "POST":
        Muallif.objects.filter(id=pk).update(
            ism=request.POST.get("ismi"),
            kitoblar_soni=request.POST.get("k_s"),
            jins=request.POST.get("jinsi"),

        )
        return redirect("/author/")

    data = {
        "muallif" : Muallif.objects.get(id=pk),
        "jins" : ["Erkak","Ayol"]
    }
    return render(request, 'muallif_update.html', data)

def record_update(request, pk):
    if request.method == "POST":
        Record.objects.filter(id=pk).update(
            qaytarish_sana=request.POST.get()
        )


def h_kutubxonachi(request):

    if request.method == "POST":
        Kutubxonachi.objects.create(
        ism=request.POST.get("ismi"),
        janr=request.POST.get("i_v")


    )
        return redirect("/kutubxonachilar/")
    data = {
        "kutubxonachilar": Kutubxonachi.objects.all()
    }
    return render(request, 'kutubxonachilar.html', data)
