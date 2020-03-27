import time
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Test,count
from .models import manunews, counter
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    number=manunews.objects.filter(type='home')
    count=counter.objects.all()
    params={
        'home':number,
        'count':count

    }
    return render(request, 'main/home.html', params)

def corona(request):
    n=manunews.objects.filter(headline__icontains="corona")
    count = counter.objects.all()

    params = {
        'corona': n,
        'count': count

    }
    return render(request,'main/corona.html',params)


def entertainment(request):
    entertainment = manunews.objects.filter(type='entertainment')
    return  render(request,'main/entertainment.html',{'entertainment': entertainment})
def shopping(request):
    return  render(request,'main/shopping.html')
def sports(request):
    sports = manunews.objects.filter(type='sports')
    return  render(request,'main/sports.html',{'sports':sports})
def news2(request):
    return  render(request,'main/news.html')
def test(request):
    if request.method == "POST":
        form = Test(request.POST)
        form.save()
        return HttpResponse('Saved')
    else:
        params={
            'form':Test
        }
        return render(request,'main/test.html',params)

def scrape(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = "https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all"
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    for a in soup.findAll('span',attrs={'class':''}):
        try:

            # time.sleep(1)
            link = a.findNext('span').text
            print(link)
        except:
            continue




    return HttpResponse('yes!!!!!!')


def googlenews(request):
    url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pEUVNnQVAB/sections/CAQiU0NCQVNPQW9JTDIwdk1EVnFhR2NTQldWdUxVZENHZ0pEUVNJT0NBUWFDZ29JTDIwdk1ESnFhblFxRVFvUEVnMUZiblJsY25SaGFXNXRaVzUwS0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EVnFhR2NTQldWdUxVZENHZ0pEUVNnQVABUAE?hl=en-CA&gl=CA&ceid=CA%3Aen"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    for a in soup.findAll('h3', attrs={'class': 'ipQwMb ekueJc gEATFF RD0gLb'}):
        try:
            time.sleep(1)
            link = a.findNext('a', attrs={'class': 'VDXfz'})
            l = 'https://news.google.com/' + link['href']
            headline = a.findNext('a', attrs={'class': 'DY5T1d'}).text
            image = a.findNext('img', attrs={'class': 'tvs3Id QwxBBf'})
            i = image['src']
            content = a.findNext('span', attrs={'class': 'xBbh9'}).text
            channel = a.findNext('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
            times = a.findNext('time', attrs={'class': 'WW6dff uQIVzc Sksgp'}).text
            ##print("headline ===============",headline,"image ========",image,"channel===========",channel,"content==========",content,"times====================",times,l)
            final = manunews(headline=headline, content=content, channel=channel, time=times, link=l, image=i, type='home')
            final.save()
        except:
            continue


    return HttpResponse('yes!!!!!!')

def googlenewsentertainment(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pEUVNnQVAB/sections/CAQiU0NCQVNPQW9JTDIwdk1EVnFhR2NTQldWdUxVZENHZ0pEUVNJT0NBUWFDZ29JTDIwdk1ESnFhblFxRVFvUEVnMUZiblJsY25SaGFXNXRaVzUwS0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EVnFhR2NTQldWdUxVZENHZ0pEUVNnQVABUAE?hl=en-CA&gl=CA&ceid=CA%3Aen"
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    for a in soup.findAll('h3', attrs={'class': 'ipQwMb ekueJc gEATFF RD0gLb'}):
        try:
            time.sleep(1)
            link = a.findNext('a', attrs={'class': 'VDXfz'})
            l = 'https://news.google.com/' + link['href']
            headline = a.findNext('a', attrs={'class': 'DY5T1d'}).text
            image = a.findNext('img', attrs={'class': 'tvs3Id QwxBBf'})
            i = image['src']
            content = a.findNext('span', attrs={'class': 'xBbh9'}).text
            channel = a.findNext('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
            times = a.findNext('time', attrs={'class': 'WW6dff uQIVzc Sksgp'}).text
            #print("headline ===============",headline,"image ========",image,"channel===========",channel,"content==========",content,"times====================",times,l)
            final = manunews(headline=headline, content=content, channel=channel, time=times, link=l, image=i,
                             type='entertainment')
            final.save()
        except:
            continue

    return HttpResponse('yes!!!!!!')


def googlenewssports(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pEUVNnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EVnFhR2NTQldWdUxVZENHZ0pEUVNJT0NBUWFDZ29JTDIwdk1EWnVkR29xQ2dvSUVnWlRjRzl5ZEhNb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EVnFhR2NTQldWdUxVZENHZ0pEUVNnQVABUAE?hl=en-CA&gl=CA&ceid=CA%3Aen"
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    for a in soup.findAll('h3', attrs={'class': 'ipQwMb ekueJc gEATFF RD0gLb'}):
        try:
            time.sleep(1)
            link = a.findNext('a', attrs={'class': 'VDXfz'})
            l = 'https://news.google.com/' + link['href']
            headline = a.findNext('a', attrs={'class': 'DY5T1d'}).text
            image = a.findNext('img', attrs={'class': 'tvs3Id QwxBBf'})
            i = image['src']
            content = a.findNext('span', attrs={'class': 'xBbh9'}).text
            channel = a.findNext('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
            times = a.findNext('time', attrs={'class': 'WW6dff uQIVzc Sksgp'}).text
            #print("headline ===============",headline,"image ========",image,"channel===========",channel,"content==========",content,"times====================",times,l)
            final = manunews(headline=headline, content=content, channel=channel, time=times, link=l, image=i,
                             type='sports')
            final.save()
        except:
            continue

    return HttpResponse('yes!!!!!!')



