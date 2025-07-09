from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.template import loader


@login_required(login_url='login')
def profile_view(request):
    user = request.user
    # profile = UserProfile.objects.get(user=user)
    # predictions = Prediction.objects.filter(user=user).order_by('-timestamp')
    return render(request, 'Myprofile.html',
                  #  {
                  #     'profile': profile,
                  #     'predictions': predictions
                  # }
                  )


def Report(request):
    template = loader.get_template('Report.html')
    return HttpResponse(template.render())
