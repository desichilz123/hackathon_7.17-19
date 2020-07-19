from django import forms
from .models import Survey
#from.models import CarbonFootprint

class CarbonFootprintForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [ 'question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8']
    
    q1choices = [
        ("5", "<5 mins"),
        ("10", "5-10 mins"),
        ("15", "10-15 mins"),
        ("20", "15-20 mins"),
        ("25", "20+ mins")
        ]
    question1 = forms.ChoiceField(label = 'How long do you usually shower for per day? ', choices = q1choices)

    q2choices = [
        ("7", "Car"),
        ("1", "Walking"),
        ("1", "Biking"),
        ("4", "Bus"),
        ("4", "Light rail / BART")
        ]
    question2 = forms.ChoiceField(label = 'What form of transportation do you usually use?', choices = q2choices)

    q3choices = [
        ("10", "I eat meat on a daily basis"),
        ("8", "I eat meat less than a few times per week"),
        ("4", "I am a vegetarian"),
        ("2", "I am a vegan")
        ]
    question3 = forms.ChoiceField(label = 'What kind of diet best describes what you eat?', choices = q3choices)

    q4choices = [
        ("50", "I fill 4 garbage cans each week"),
        ("40", "I fill 3 garbage cans each week"),
        ("30", "I fill 2 garbage cans each week"),
        ("20", "I fill 1 garbage can each week"),
        ("5", "I fill half a garbage can each week")
        ]
    question4 = forms.ChoiceField(label = 'How much waste do you produce?', choices = q4choices)

    q5choices = [
        ("3", "Avocado"),
        ("5", "Steak"),
        ("4", "Chicken"),
        ("1", "Salad"),
        ("2", "Carrots")
        ]
    question5 = forms.ChoiceField(label = 'What is your favorite food out of the items below?', choices = q5choices)

    q6choices = [
        ("4", "Fluorescent"),
        ("2", "LED"),
        ("6", "Incandescent"),
        ("6", "Not sure")
        ]
    question6 = forms.ChoiceField(label = 'What kind of light-bulbs are in your house? ', choices = q6choices)

    q7choices = [
        ("12", "1"),
        ("10", "2"),
        ("8", "3"),
        ("6", "4"),
        ("4", "5"),
        ("2", "6 or more")
        ]
    question7 = forms.ChoiceField(label = 'How large is your household?', choices = q7choices)

    q8choices = [
        ("10", "Large house (>2500 sq ft.)"),
        ("7", "Medium sized (1500 sq. ft - 2500 sq. ft)"),
        ("4", "Small house (<1500 sq ft)"),
        ("2", "Apartment")
        ]
    question8 = forms.ChoiceField(label = 'What is the size of your home?', choices = q8choices)
