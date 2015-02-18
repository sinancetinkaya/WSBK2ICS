# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2 
import urllib
from icalendar import Calendar, Event
from datetime import datetime, date
from dateutil.parser import parse
import argparse
import iso8601


print u"\nWSBK iCalendar exporter by Sinan Çetinkaya (sinancetinkaya35@gmail.com)\n"
parser = argparse.ArgumentParser(description=u'WSBK iCalendar exporter by Sinan Çetinkaya (sinancetinkaya35@gmail.com)')
parser.add_argument('--tracks', help=u'You can specify the race tracks you want to export, default all / Çıktı almak istediğiniz yarış pistlerini belirtebilirsiniz. Varsayılan hepsi. Eg/örnek: --tracks "Aragon,Assen,Imola"')
parser.add_argument('--filters', help=u'You can filter race classes, event types. Default all / Yarış sınıflarını ve etkinlik türlerini belirtebilirsiniz. Varsayılan hepsi. Eg/örnek: --filters "sbk - Race 1,ssp - Race,ssp - Qualifying"')
args = vars(parser.parse_args())

if args['tracks'] != None:
    tracks = args['tracks'].split(',')
else:
    tracks = "*"

if args['filters'] != None:
    filters = args['filters'].split(',')
else:
    filters = '*'
site = "http://www.worldsbk.com"

cal = Calendar()
cal.add('PRODID', '-//Sinan Cetinkaya//iCalendar//TR')
cal.add('VERSION', '2.0')
cal.add('METHOD','PUBLISH')
cal.add('CALSCALE','GREGORIAN')
cal.add('X-WR-CALNAME', 'WSBK - FIM World Superbike')
cal.add('X-WR-TIMEZONE', 'UTC')
cal.add('X-WR-CALDESC', 'FIM World Superbike World Championship')

if tracks=='*':
    tracks=[]
    soup = BeautifulSoup(urllib2.urlopen(site+'/en/calendar').read())
    tracksArray = soup.find('ol',attrs={'class':'circuit_calendar'})
    tracksArray = tracksArray.findAll('div', attrs={'class':'content'})
    for trackEach in tracksArray:
        tracks.append(trackEach.a['href'].split('/')[3]) #her bir yarışın href'ini '/' ile böl ve 3. öğeyi al = pist adı
                            

f = open('WSBK.ics', 'wb')
year = date.today().year.__str__()
for track in tracks:
    url = site +urllib.quote('/en/event/'+ track + '/' + year)
    print url
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    section = soup.find('section', attrs={'class':'content clearfix'})
    circutName = section.find('h1').contents[0]
    Circuit_Information = section.find('div', attrs={'class':'col-xs-4 col_center'})
    DESCRIPTION = Circuit_Information.find('dd', attrs={'style':True}).getText('\n')
    LOCATION =''
    for LOCATIONLine in DESCRIPTION.split('\n'):
        if ':' in LOCATIONLine:
            break;
        else:
            LOCATION += LOCATIONLine
    
    allRaces = section.find('div', attrs={'class':'tab_widget'})
    timeTable = allRaces.findAll('tr', attrs={'class':'timeIso'})
    for eachTime in timeTable:
        
        try:
            eName = eachTime.find('td').getText()
            DTSTART = iso8601.parse_date(eachTime.find('td', attrs={'data_ini':True})['data_ini'])
            eName.strip()
        except TypeError:
            eName = ''
            
        if eName in filters or filters == '*':
            SUMMARY = 'WSBK: '+ eName +" - "+ track 
            UID = (year + "_" + track + "_" + eName).replace(" ", "")
            event = Event()
            event.add('DTSTART', DTSTART)
            event.add('SUMMARY', SUMMARY)
            event['UID'] = UID
            event.add('LOCATION', LOCATION)
            event.add('DESCRIPTION', DESCRIPTION)
            event.add('PRIORITY', 5)
            cal.add_component(event)
            print "%s, %s, %s" %(DTSTART.strftime('%Y-%m-%d %H:%M') , track, eName)


f.write(cal.to_ical())
f.close()
