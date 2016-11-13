# coding: utf-8
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.shortcuts import render, redirect

from simple_forms.apps.core.models import Person,PersonForm,UserForm,User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
"""
def home(request):
    persons = Person.objects.all()
    return render(request, 'core/home.html', { 'persons': persons })



def home(request):
    if not request.user.is_authenticated():
        return render(request, 'core/login.html')
    else:
        persons = Person.objects.filter(user=request.user)



    return render(request, 'core/home.html', {'persons': persons})


"""


def add_person(request):
    if not request.user.is_authenticated():
        return render(request, 'core/login.html')
    else:
        form = PersonForm(request.POST or None,request.FILES )
        if form.is_valid():
            persons = form.save()
            persons.user = request.user
          
            persons.save()

            return redirect('home')
        context = {
            "form": form,
        }
        return render(request, 'core/add_person.html', context)


def home(request):
    if not request.user.is_authenticated():
	
        return render(request, 'core/login.html')
    else:
		logging.info(request.user)
        persons = Person.objects.filter(user=request.user)
        page = request.GET.get('page', 1)
        paginator = Paginator(persons, 2)

        try:
            persons = paginator.page(page)
        except PageNotAnInteger:
            persons= paginator.page(1)
        except EmptyPage:
            persons = paginator.page(paginator.num_pages)


    return render(request, 'core/home.html', {'persons': persons})
"""
def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('home')
    else:
        form = PersonForm()
    return render(request, 'core/add_person.html', { 'form': form })
"""
#===========delete a prson==================
def delete_person(request, person_id):

    if request.method == "POST":

        c = get_object_or_404(Person, pk=person_id)
        c.delete()

        return redirect('home')
    else:
        return redirect('home')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'core/login.html', context)

#=====================doctor login======================
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Person.objects.filter(user=request.user)
                return render(request, 'core/home.html', {'persons': albums})
            else:
                return render(request, 'core/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'core/login.html', {'error_message': 'Invalid login'})
    return render(request, 'core/login.html')

#=================regetser a doctor======================
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Person.objects.filter(user=request.user)
                return render(request, 'core/home.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'core/register.html', context)

#======================edit the patient details
def edit(request, person_id):
    i = get_object_or_404(Person, pk=person_id)


    if request.method == "POST":
        form = PersonForm(request.POST, instance=i)

        if form.is_valid():
          # update main BL
            form.save()


            i.save()

        return redirect("home")
    else:
        form = PersonForm(instance=i)

    return render(request, 'core/add_person.html', {'i': i, 'form': form, 'mode': 'edit'})
#=======================
def foto(request, person_id):
    persons= get_object_or_404(Person, pk=person_id)


    return render(request, 'core/home3.html', {'persons':persons})


def doctor(request):

    return render(request,'core/profile.html')

##search by name or last name
def search(request):
    q = request.GET.get("q", None)

    q1 = request.GET.get("q1", None)

    persons = Person.objects.filter(Q(name=q) & Q(last_name=q1))
    return render(request, 'core/home.html', {'persons':persons})


def date(request):

    if ('q1' in request.GET) and request.GET['q1'].strip():
        date = request.GET['q1']

        persons = Person.objects.filter(date=date)
    return render(request, 'core/home1.html', {'persons':persons})







