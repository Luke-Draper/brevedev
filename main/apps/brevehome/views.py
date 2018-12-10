from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from datetime import datetime 
import re
from .models import UserManager, User, EventManager, Event, GroupManager, Group, LocationManager, Location

	# Page Paths

# - - = - = + = + = - = - - #

	# Allowed when Logged Out

# - - = - = + = + = - = - - #
	# home
def index(request):
	return render(request,"brevehome/index.html")
# - - = - = + = + = - = - - #
	# signup page
def signup(request):
	if check_logged_in(request):
		messages.warning(request, 'You are already logged in and cannot sign up again')
	return render(request,"brevehome/signup.html")

	# signup form submit
def signup_submit(request):
	if check_logged_in(request):
		return redirect("/signup")
	if request.method == "POST":
		errs = User.objects.basic_validator(request.POST)
		print (errs)
		if len(errs) > 0:
			for errkey in errs:
				messages.error(request, errs[errkey])
			return redirect("/signup")
		else:
			user = User.objects.create_user(request.POST)
			user.save()
			request.session["logged_u_id"] = user.id
			messages.success(request, 'Succesfully signed up!')
			return redirect("/user")
	else:
		messages.error(request, 'Improper form submission')
		return redirect("/signup")

# - - = - = + = + = - = - - #
	# login page
def login(request):
	if check_logged_in(request):
		messages.warning(request, 'You are already logged in and cannot log in again')
	return render(request,"brevehome/login.html")
	# login form submit
def login_submit(request):
	if check_logged_in(request):
		return redirect("/login")
	if request.method == "POST":
		if len(request.POST["email"]) < 1 or len(request.POST["password"]) < 1:
			messages.error(request, "All fields are required")
			return redirect("/login")
		else:
			try:
				test_user = User.objects.get(email=request.POST["email"])
				if User.objects.test_login(test_user,request.POST["password"]):
					request.session["logged_u_id"] = test_user.id
					messages.success(request, 'Succesfully logged in!')
					return redirect("/user")
				else:
					messages.error(request, "Email or Password is invalid")
					return redirect("/login")
			except:
				messages.error(request, "Email or Password is invalid")
				return redirect("/login")
	else:
		messages.error(request, 'Improper form submission')
		return redirect("/login")

# - - = - = + = + = - = - - #


	# logout form submit
def logout(request):
	del request.session['logged_u_id']
	check_logged_in(request)
	messages.success(request, 'Succesfully logged out!')
	return redirect("/")

# - - = - = + = + = - = - - #

	# Required Logged in

# - - = - = + = + = - = - - #
	# my dashboard
def my_dashboard(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# a user with id:u_id dashboard (with private/public filter applied)
def dashboard(request):
	return redirect("/")
	# send friend request to user with id:u_id
def friend_request(request):
	return redirect("/")
	# accept friend request from user with id:u_id
def friend_request_accept(request):
	return redirect("/")
	# decline friend request from user with id:u_id
def friend_request_decline(request):
	return redirect("/")
	# unfriend user with id:u_id
def unfriend(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# a group with id:g_id dashboard (with private/public filter applied)
def group(request):
	return redirect("/")
	# send an invitation to join group with id:g_id to user with id:u_id
def group_invite(request):
	return redirect("/")
	# cancel an invitation to join group with id:g_id to user with id:u_id
def group_cancel_invite(request):
	return redirect("/")
	# accept an invitation to join group with id:g_id
def group_accept_invite(request):
	return redirect("/")
	# decline an invitation to join group with id:g_id
def group_decline_invite(request):
	return redirect("/")
	# send an application to join group with id:g_id
def group_apply(request):
	return redirect("/")
	# cancel an application to join group with id:g_id
def group_cancel_apply(request):
	return redirect("/")
	# accept an application to join group with id:g_id from user with id:u_id
def group_accept_application(request):
	return redirect("/")
	# decline an application to join group with id:g_id from user with id:u_id
def group_decline_application(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# a event with id:e_id dashboard (with private/public filter applied)
def event(request):
	return redirect("/")
	# send an invitation to join event with id:e_id to user with id:u_id
def event_invite(request):
	return redirect("/")
	# cancel an invitation to join event with id:e_id to user with id:u_id
def event_cancel_invite(request):
	return redirect("/")
	# accept an invitation to join event with id:e_id with a might attend marker
def event_accept_might_invite(request):
	return redirect("/")
	# accept an invitation to join event with id:e_id with a will attend marker
def event_accept_will_invite(request):
	return redirect("/")
	# decline an invitation to join event with id:e_id
def event_decline_invite(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# new group
def new_group(request):
	return redirect("/")
	# new group form submit
def new_group_submit(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# new event
def new_event(request):
	return redirect("/")
	# new event form submit
def new_event_submit(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# search box page (possibly just in nav)
def search(request):
	return redirect("/")
	# search submit
def search_submit(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# search users result page
def search_user(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# search groups result page
def search_group(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# search events result page
def search_events(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# search locations result page
def search_location(request):
	return redirect("/")
# - - = - = + = + = - = - - #
	# location with name:place_name and coordinates:long,lat,zed page
def location(request):
	return redirect("/")
	# location submit to current location lookup
def location_submit(request):
	return redirect("/")
	# Required Ownership

	# edit my dashboard
def edit_dashboard(request):
	return redirect("/")
	# edit group with id:g_id dashboard (only accessible by owner redirects with flash otherwise)
def edit_group(request):
	return redirect("/")
	# edit event with id:e_id dashboard (with private/public filter applied)
def edit_event(request):
	return redirect("/")


def check_logged_in(request):
	if 'logged_u_id' not in request.session:
		request.session["logged_u_id"] = 0
	if request.session["logged_u_id"] == 0:
		return False
	else:
		return True

