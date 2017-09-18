from django.shortcuts import render, HttpResponse, redirect
def index(request):
  return render(request, "survey/surveyform.html")

def submit(request):
  request.session['name'] = request.POST['name']
  request.session['location'] = request.POST['location']
  request.session['language'] = request.POST['language']
  request.session['comment'] = request.POST['comment']
  return render(request, "survey/result.html")

def goback(request):
  del request.session['name']
  del request.session['location']
  del request.session['language']
  del request.session['comment']
  return redirect('/')
