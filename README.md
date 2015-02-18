# WSBK2ICS
World Superbike iCalendar(ics) exporter
This script scraps current year's calendar events from worldsbk website to ics calendar format which can be imported iOS, Android, Outlook etc.

You can specify the race tracks you want to export, default all. Eg:
Çıktı almak istediğiniz yarış pistlerini belirtebilirsiniz. Varsayılan hepsi. Örnek:

**--tracks "Aragon,Assen,Imola"**

You can filter race classes, event types. Default all. Eg:
Yarış sınıflarını ve etkinlik türlerini belirtebilirsiniz. Varsayılan hepsi. Örnek:

**--filters "sbk - Race 1,ssp - Race,ssp - Qualifying"**

Bu script worldsbk sitesinden yarış takvimini alıp ics takvim formatına çevirir, bu format iOS, Android, Outlook'a import edilebilir.
