from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

# Create your views here.
def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/sign-in/?next=%s' % request.path)
	else:
		ship = get_object_or_404(User,email=request.user.email)
	item = Item.objects.all()

	variables = RequestContext(request, {
		'ship': ship,
		'item': item,
	})
	return render_to_response('home.html', variables)

@csrf_exempt
def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			next_one = form.save(commit=False)
			email = request.POST['email']
			password1 = request.POST['password1']
			password2 = request.POST['password2']
			if password1 == password2:
				password = password1
			else:
				print "Password is Wrong ......"
			next_one.set_password(password)
			next_one.email = email
			next_one.save()
			return HttpResponseRedirect('/sign-in')
		else:
			form.errors
	else:
		form = RegisterForm()
	variables = RequestContext(request, {
        'reg_form':form,
        })
	return render_to_response('register.html', variables)

@csrf_exempt
def sign_in(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('home'))
	if request.method == "GET":
		form = LoginForm()
	else:
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			print username
			password = request.POST['password']
			print password
			user = auth.authenticate(username=username, password=password)
			print user
			if user:
				auth.login(request, user)
				return HttpResponseRedirect('/') #redirect after POST
			else:
				return HttpResponseRedirect('/sign-in')
	variables = RequestContext(request, {
    	'form':form,
	})
	return render_to_response('sign_in.html', variables)

def gallery(request):
	item = Item.objects.all() # get(id=1)
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/sign-in/?next=%s' % request.path)
	else:
		ship = get_object_or_404(User,email=request.user.email)

	variables = RequestContext(request, {
		'item':item,
		'ship': ship,
	})
	return render_to_response('gallery.html', variables)

def resized_img(request, img_id=1):
	item = Item.objects.get(id=img_id)

	res_tuple = ['200x200','300x300', '500x500', '600x600']

	variables = RequestContext(request, {
		'item':item,
		'res_tuple': res_tuple,
	})
	return render_to_response('resized_img.html', variables)

@csrf_exempt
def upload(request):
	# print request.user
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/sign-in/?next=%s' % request.path)
	else:
		ship = get_object_or_404(User,email=request.user.email)

	if request.method == "POST":
		form = ItemForm(request.POST, request.FILES)
		if form.is_valid():
			additional =  form.save(commit=False)
			additional.user = request.user
			additional.save()
			return HttpResponseRedirect('/')
		# else:
		# 	form.errors()
	else:
		form = ItemForm()

	variables = RequestContext(request, {
		'ship': ship,
		'up_image': form,
	})
	return render_to_response('upload.html', variables)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/sign-in')

