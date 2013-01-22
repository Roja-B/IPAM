from PARAMETERS import *
#PATH = "/media/data3/roja/IPAM"
#SLIDE = 1 # years
#WINDOW = 2 # years
#START_YEAR = 2000
#END_YEAR = 2013
t = open(PATH+"/myResults/CommunitySizes","w")
#years=[n for n in range(START_YEAR,END_YEAR-WINDOW+1+1)]
years = []
year = START_YEAR
while year <= END_YEAR-WINDOW+1:
        years.append(year)
        year += SLIDE
print years
dirs=[]
for year in years:
    if MODE == "NORMAL":
        dirs.append(str(year)+str(year+WINDOW-1))
    elif MODE == "AGGREGATE":
        dirs.append(str(START_YEAR)+str(year+WINDOW-1))
print dirs
time = 0
for (year,entry) in zip(years,dirs):
    try: f=open(PATH+"/myResults/{0}/communityStats".format(entry),"r")
    except: continue
    f.readline()
    print "========================== C",year
    for line in f:
        line = line.strip()
        density = line.split(' ')[3]
        com = line.split(' ')[0]
        size = line.split(' ')[1]
        if density == "NA": size = "3"
        print com,size,density
        t.write(str(year)+'_'+str(com)+'\t'+entry+'\t'+str(size)+'\n')
    f.close()
    time += 1
t.close()
