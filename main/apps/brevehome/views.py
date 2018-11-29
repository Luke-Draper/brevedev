from django.shortcuts import render, HttpResponse, redirect
def index(request):
	context = {
		"dummy": "dummy"
	}
	request.session["dummy"] = "dummy"
	return render(request,"brevehome/index.html",context)

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


