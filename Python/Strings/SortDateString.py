dates = ["24 Jul 2017","25 Jul 2017", "11 Jun 1996", "01 Jan 2019", "12 Aug 2005", "01 Jan 1997"]

daysDict={}
monthsDict={}
yearsDict={}

daysArr=[]
monthsArr=[]
yearsArr=[]

monthsMap={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"Jun":6,"Jul":7,"Aug":8}

for i in range(len(dates)):
    date=dates[i].split()
    day=date[0]
    month=monthsMap[date[1]]
    year=date[2]
    days[i]=i
    months[i]=month
    years[year]=i

print(months)
