from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

'''
def january(request):
    return HttpResponse("Code 3 hours Each day")

def feb(request):
    return HttpResponse("Walk for at least 20 minutes every day!")

def march(request):
    return HttpResponse("Practice Django for atl least 20 minitues each day!")
    
'''    
'''
def monthly_challenges(request, month):
    text= None
    if month=="january":
        text= "Code 3 hours Each day"
    elif month=="february":
        text="Walk for at least 20 minutes every day!"
    elif month=="march":
        text="Practice Django for atl least 20 minitues each day!"
    else:
        return HttpResponseNotFound("This month not supported !")
    return HttpResponse(text)
'''
 
monthly_challenges = {
    "january": "Walk for at least 20 minutes each day",
    "february": "Read a book for at least 15 minutes daily",
    "march": "Drink 8 glasses of water every day",
    "april": "Do 10 minutes of stretching exercises each morning",
    "may": "Try a new healthy recipe each week",
    "june": "Practice meditation for 10 minutes daily",
    "july": "Go for a 30-minute walk outdoors every day",
    "august": "Limit screen time to no more than 2 hours after work",
    "september": "Write down three things you are grateful for each day",
    "october": "Try a new hobby or activity this month",
    "november": "Spend 15 minutes decluttering a space in your home each day",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request,"challenges/index.html", {
        "months": months
    })

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month> len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    redirect_month = months [month-1 ] 
    redirect_path= reverse ("month-challenge", args=[redirect_month]) 
    return HttpResponseRedirect(redirect_path)
 
       
    


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month
            })
 
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
