from django import template
from dongi.models import user
from django.http import HttpResponse
from django.template import context, loader
from .models import user
from django.shortcuts import render
from dongi.forms import userf

# def add(request):
#   if request.method == 'POST':
#      form = AllocationPlanForm(request.POST)
# form.save()
# return render(request, 'page.html', {
# 'form': AllocationPlanForm()
# })


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class userV:
    def index(request):
        users = user.objects.order_by('id')
        template = loader.get_template('user/index.html')
        users_len = len(users)
        context = {
            'users': users,
            'users_len': users_len

        }
        return HttpResponse(template.render(context, request))

    def create(request):
        if request.method == 'POST':
            form = userf(request.POST)
            if form.is_valid():
                form.save()
                return userV.index(request)
        else:
            form = userf()
        context = {
            'form': form,

        }
        template = loader.get_template('user/form.html')
        return HttpResponse(template.render(context, request))

    def delete(request, id):
        user.objects.filter(id=id).delete()
        return userV.index(request)

    def edit(request, id):
        myuser = user.objects.get(id=id)
        if request.method == 'POST':
            form = userf(request.POST, instance=myuser)
            if form.is_valid():
                form.save()
                return userV.index(request)
        else:
            form = userf(instance=myuser)
        context = {
            'form': form
        }
        template = loader.get_template('user/form.html')
        return HttpResponse(template.render(context, request))
