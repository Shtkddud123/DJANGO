import requests
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from piano.models import PracticeSession
from piano.forms import PracticeSessionForm

# Create your views here.
def piano_page(request):
    yt_html = requests.get(
     "https://www.youtube.com/channel/UCILeIbhtlv4lmgAaZbPKr8A"
    ).text
    title_start = yt_html.find('<h3 class="yt-lockup-title ">')
    href_start = yt_html[title_start:].find("href=")
    href_end = yt_html[title_start + href_start:].find(">")
    yt_code = yt_html[
     title_start + href_start:title_start + href_start + href_end
    ].split("=")[-1].split('"')[0]

    today = datetime.datetime.now().date()
    sixty_days_ago = today - datetime.timedelta(days=60)
    sixty_sessions = PracticeSession.objects.all().filter(date__gte=sixty_days_ago).order_by("date")
    one_year_ago = datetime.datetime(today.year - 1, today.month, today.day).date()
    year_sessions = PracticeSession.objects.all().filter(date__gte=one_year_ago).order_by("date")
    cumulative_sixty = [[
     sixty_days_ago,
     sum([session.minutes for session in PracticeSession.objects.all().filter(date__lte=sixty_days_ago)])
    ]]
    while cumulative_sixty[-1][0] != today:
        next_day = cumulative_sixty[-1][0] + datetime.timedelta(days=1)
        cumulative_sixty.append([
         next_day,
         sum([session.minutes for session in PracticeSession.objects.all().filter(date__lte=next_day)])
        ])
    cumulative_year = [[
     one_year_ago,
     sum([session.minutes for session in PracticeSession.objects.all().filter(date__lte=one_year_ago)])
    ]]
    while cumulative_year[-1][0] != today:
        next_day = cumulative_year[-1][0] + datetime.timedelta(days=1)
        cumulative_year.append([
         next_day,
         sum([session.minutes for session in PracticeSession.objects.all().filter(date__lte=next_day)])
        ])
    all_minutes = sum([session.minutes for session in PracticeSession.objects.all()])
    hours = all_minutes // 60
    minutes = all_minutes % 60
    return render(request, "piano.html", {
     "recent_code": yt_code,
     "today": today,
     "sixty_sessions": sixty_sessions,
     "sixty_days_ago": sixty_days_ago,
     "year_sessions": year_sessions,
     "one_year_ago": one_year_ago,
     "cumulative_sixty": cumulative_sixty,
     "cumulative_year": cumulative_year,
     "hours": hours,
     "minutes": minutes
    })


def practice_page(request):
    return render(request, "pianopractice.html")


@login_required(login_url="/", redirect_field_name=None)
def update_page(request):
    sessions = PracticeSession.objects.all().order_by("date").reverse()
    today = datetime.datetime.now()
    form = PracticeSessionForm(initial={"date": today})
    if request.method == "POST":
        form = PracticeSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/piano/update/")
        else:
            return render(request, "pianoupdate.html", {"form": form, "sessions": sessions})

    return render(request, "pianoupdate.html", {"form": form, "sessions": sessions})



@login_required(login_url="/", redirect_field_name=None)
def delete_page(request, session_id):
    session = PracticeSession.objects.get(pk=session_id)
    if request.method == "POST":
        session.delete()
        return redirect("/piano/update/")
    return render(request, "pianodelete.html", {"session": session})
