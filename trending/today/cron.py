from django_cron import CronJobBase, Schedule
import time
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Test,count
from .models import manunews, counter
from bs4 import BeautifulSoup
import requests



class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

###################SPORTS#######################
    def do(self):
        manunews.objects.all().delete()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pEUVNnQVAB?hl=en-CA&gl=CA&ceid=CA%3Aen"
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        for a in soup.findAll('div', attrs={'class': 'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
            try:
                #time.sleep(1)
                link = a.findNext('a', attrs={'class': 'VDXfz'})
                l = 'https://news.google.com/' + link['href']
                headline = a.findNext('a', attrs={'class': 'DY5T1d'}).text
                image = a.findNext('img', attrs={'class': 'tvs3Id QwxBBf'})
                i = image['src']
                content = a.findNext('span', attrs={'class': 'xBbh9'}).text
                channel = a.findNext('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
                times = a.findNext('time', attrs={'class': 'WW6dff uQIVzc Sksgp'}).text
                # print("headline ===============",headline,"image ========",image,"channel===========",channel,"content==========",content,"times====================",times,l)
                final = manunews(headline=headline, content=content, channel=channel, time=times, link=l, image=i,
                                 type='sports')
                print('control')
                final.save()
            except:
                continue



###################HOME#######################
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pEUVNnQVAB?hl=en-CA&gl=CA&ceid=CA%3Aen"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        for a in soup.findAll('div', attrs={'class': 'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
            try:
                #time.sleep(1)
                link = a.findNext('a', attrs={'class': 'VDXfz'})
                l = 'https://news.google.com/' + link['href']
                headline = a.findNext('a', attrs={'class': 'DY5T1d'}).text
                image = a.findNext('img', attrs={'class': 'tvs3Id QwxBBf'})
                i = image['src']
                content = a.findNext('span', attrs={'class': 'xBbh9'}).text
                channel = a.findNext('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
                times = a.findNext('time', attrs={'class': 'WW6dff uQIVzc Sksgp'}).text
                ##print("headline ===============",headline,"image ========",image,"channel===========",channel,"content==========",content,"times====================",times,l)
                final = manunews(headline=headline, content=content, channel=channel, time=times, link=l, image=i,
                                 type='home')
                print("second")
                final.save()
            except:
                continue



###################ENTERTAINMENT#######################
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pEUVNnQVAB?hl=en-CA&gl=CA&ceid=CA%3Aen"
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        for a in soup.findAll('div', attrs={'class': 'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}):
            try:
                #time.sleep(1)
                link = a.findNext('a', attrs={'class': 'VDXfz'})
                l = 'https://news.google.com/' + link['href']
                headline = a.findNext('a', attrs={'class': 'DY5T1d'}).text
                image = a.findNext('img', attrs={'class': 'tvs3Id QwxBBf'})
                i = image['src']
                content = a.findNext('span', attrs={'class': 'xBbh9'}).text
                channel = a.findNext('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
                times = a.findNext('time', attrs={'class': 'WW6dff uQIVzc Sksgp'}).text
                # print("headline ===============",headline,"image ========",image,"channel===========",channel,"content==========",content,"times====================",times,l)
                final = manunews(headline=headline, content=content, channel=channel, time=times, link=l, image=i,
                                 type='entertainment')
                print("third")
                final.save()
            except:
                continue
        ##########################COUNTER#############################
        count = counter.objects.all().delete()
        url = "https://www.worldometers.info/coronavirus/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        i = 0
        for a in soup.findAll('div', attrs={'class': 'maincounter-number'}):
            s = a.text
            if i == 0:
                t = s
            if i == 1:
                d = s
            if i == 2:
                r = s
                c = counter(Total_cases=t, Deaths=d, Recovered=r)
                c.save()

            i = i + 1
        return HttpResponse('yes!!!!!!')


