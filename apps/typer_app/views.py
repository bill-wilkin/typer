from django.shortcuts import render, redirect
from ..login_reg_app.models import User, UserManager
from ..typer_app.models import *
import random
from django.utils import dateparse
# Create your views here.

# Renders main dashboard


def dashboard(request):
    if "user_id" not in request.session:
        return redirect("/")
    this_user = User.objects.filter(id=request.session.get('user_id'))
    context = {
        'user': this_user[0]
    }
    print(this_user[0].first_name)
    return render(request, 'dashboard.html', context)


def race_page(request):
    if "user_id" not in request.session:
        return redirect("/")
    rando = random.randint(1, len(Target.objects.all()))
    random_target = Target.objects.get(id=rando)
    print(rando)
    context = {
        'target': random_target,
    }
    return render(request, 'race.html', context)


def finish(request):
    if "user_id" not in request.session or request.method != 'POST':
        return redirect("/")
    
    this_user = User.objects.filter(id=request.session['user_id'])
    this_target = Target.objects.get(id=request.POST['target_id'])
    time_string = f"{int(request.POST['minutes']):02}:{int(request.POST['seconds']):02}"
    fraction_minute = (int(
        request.POST['minutes']*60) + int(request.POST['seconds']))/60
    words_per_minute = (
        len(this_target.content.split()) / fraction_minute)
    print(
        f"word count: {len(this_target.content.split())}, correct: {request.POST['num_correct']}, total: {request.POST['total_char']}")
    new_session = Session.objects.create(
        taken_by=this_user[0],
        target=Target.objects.get(id=request.POST['target_id']),
        time=time_string,
        wpm=words_per_minute,
        accuracy=(int(request.POST['num_correct'])/int(request.POST['total_char'])*100))

    return redirect('/type/results-page')


def results_page(request):
    if "user_id" not in request.session:
        return redirect("/")
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'session': Session.objects.last()
    }
    return render(request, 'results.html', context)
