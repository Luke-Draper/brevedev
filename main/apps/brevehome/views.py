from django.shortcuts import render, HttpResponse, redirect
def index(request):
	context = {
		"dummy": "dummy"
	}
	request.session["dummy"] = "dummy"
	return render(request,"brevehome/index.html")

def redirect(request):
	del request.session["dummy"]
	return redirect("/")

def post(request):
	if request.method == "POST":
		request.session["name"] = request.POST["name"]
		print("")
		print(request.POST)
		print(request.POST["name"])
		print(request.POST["desc"])
		print("")
		return redirect("/")
	else:
		return redirect("/")


def test_index(request):
	check_session_login(request)
	return render(request,"brevehome/index.html")

def test_login(request):
	check_session_login(request)
	return render(request,"brevehome/login.html")

def test_signup(request):
	check_session_login(request)
	return render(request,"brevehome/signup.html")

def test_dashboard(request):
	check_session_login(request)
	return render(request,"brevehome/dashboard.html")


def check_session_login(request):
	if "test_logged_in" not in request.session:
		request.session["test_logged_in"] = False



