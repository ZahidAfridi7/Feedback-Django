from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import ReviewForm
from .models import Review

# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
          review = Review(user_name=form.cleaned_data['user_name'],
                          review_text=form.cleaned_data['review_text'],
                          ratting=form.cleaned_data['ratting'])
          review.save() 
          return HttpResponseRedirect('/thank-you')
    form = ReviewForm()
    
    return render(request,"reviews/review.html",{
            "form": form
        })
def thank_you(request):
    return render(request,"reviews/thankyou.html")    