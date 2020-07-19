from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CarbonFootprintForm
from .models import Survey
import sqlite3
# Create your views here.

#home page
def home(request):
    return render(request, 'survey/home.html')
#survey
'''
def survey(request):
    return render(request, 'survey/survey.html')
'''

#signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log user in
            login(request, user)
            return redirect('survey/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'survey/signup.html', {'form': form})

#login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log user in
            user = form.get_user()
            login(request, user)
            return redirect('survey/home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'survey/login.html', {'form': form})
'''
#logout
def logout_view(request):
    if request.method == 'POST':
        logout(request) # no need to pass in user because Django knows which user is logged in
        return redirect('survey/login.html')
'''

#Survey
def survey(request):
    form = CarbonFootprintForm()
    note = ''
    if request.method == 'POST':
        filled_form = CarbonFootprintForm(request.POST)
        if filled_form.is_valid():
            print(filled_form)
            created_carbonfp = filled_form.save()
            created_carbonfp_pk = created_carbonfp.id #retrieves primary key
            note = 'Thanks for submitting the form!'
            filled_form = CarbonFootprintForm()
        else:
            created_carbonfp = None
            note = 'Something did not go right, please try again.'
        return render(request, 'survey/survey.html', {'carbonfpform': filled_form, 'created_carbonfp_pk': created_carbonfp_pk, 'note': note})
    else:
        form = CarbonFootprintForm()
        return render(request, 'survey/survey.html', {'carbonfpform': form, 'note': note})

#Info page
def info(request, pk):
    survey = Survey.objects.get(pk = pk)
    form = CarbonFootprintForm(instance = survey)

    if (survey.total > 75):
        header = "You have a very large carbon footprint! Consider lightening your step through the following ways:"
        steps = ["Reduce your waste by recycling more",
                "Take shorter showers",
                "Switch to more energy efficient lights",
                "Cut down on some animal based products from your diet",
                "Rely less on automobiles for transportation when you could travel by foot or bicycle instead. Clean-air vehicles and public transportation are also friendlier options for travel than gasoline-run cars"
                ]
        return render(request, 'survey/info.html', {'header': header, 'steps': steps})

    elif (survey.total < 75 and survey.total >= 50):
        header = "Your carbon footprint is larger than the average person’s—but not by very much! With a few simple steps, you can lighten your step on the planet. Consider reducing your CO2 emission through the following ways:"
        steps = ["Reduce your waste by recycling more",
                "Take shorter showers",
                "Switch to more energy efficient lights",
                "Cut down on some animal based products from your diet",
                "Rely less on automobiles for transportation when you could travel by foot or bicycle instead. Clean-air vehicles and public transportation are also friendlier options for travel than gasoline-run cars"
                ]
        return render(request, 'survey/info.html', {'header': header, 'steps': steps})

    elif (survey.total < 50 and survey.total > 40):
        header = "Congratulations! You are below the global average in terms of CO2 emissions. If not already, check out how you could further lighten your step: "
        steps = ["Reduce your waste by recycling more",
                "Take shorter showers",
                "Switch to more energy efficient lights",
                "Cut down on some animal based products from your diet",
                "Rely less on automobiles for transportation when you could travel by foot or bicycle instead. Clean-air vehicles and public transportation are also friendlier options for travel than gasoline-run cars"
                ]
        return render(request, 'survey/info.html', {'header': header, 'steps': steps})

    else:
        header = "Amazing! You are one of the very few individuals who have a small carbon footprint on this planet. If everyone has the same impact on Earth as you do, our planet would be able to sustain everyone perfectly fine. If you’re not already, consider planting trees to absorb the already emitted CO2."
        return render(request, 'survey/info.html', {'header': header})

    '''
    print(form)

    results = cc.execute("select total from survey_survey where id = (?)", (pk))
    fetched_results = results.fetchall()
    print(fetched_results)
    '''
