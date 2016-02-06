import urllib2
#import database_statistics

def getRouterUrl():
    return 'http://192.168.0.1' #Ip to TP-Link router

def SetupRouterConnection():

   #TP-Link router username and password
   username = 'admin'
   password = 'admin'

   p = urllib2.HTTPPasswordMgrWithDefaultRealm()

   p.add_password(None, getRouterUrl(), username, password)

   handler = urllib2.HTTPBasicAuthHandler(p)
   opener = urllib2.build_opener(handler)
   urllib2.install_opener(opener)
   return True

def addMacToWiFiBlock( mac,  desc):
   url = getRouterUrl()+'/userRpm/WlanMacFilterRpm.htm?Mac='+mac+'&Desc='+desc+'&Type=1&entryEnabled=1&Changed=0&selIndex=0&Page=1&vapIdx=1&Save=Save'
   page = urllib2.urlopen(url).read()
   return True

def getClientList():
    url = getRouterUrl()+'/userRpm/AssignedIpAddrListRpm.htm?Refresh=Refresh' #Clients
    page = urllib2.urlopen(url).read()
    devices = []

    #Parse out device list
    page = page.split("new Array(", 1)
    page = page[1].split('0,0 );', 1)
    page = page[0].replace('"',"").replace(' ',"")
    data = page.split("\n")

    for index in range(len(data)):
        if(index != 0):
            devices.append( data[index].split(",") )

    return devices

def getStatistics():
    url = getRouterUrl()+'/userRpm/SystemStatisticRpm.htm?itnerval=10&Num_per_page=100' #stats
    page = urllib2.urlopen(url).read()
    stats = []

    #Parse out statistic data
    page =  page.split("new Array(", 1)
    page = page[1].split('0,0 );', 1)
    page = page[0].replace('"',"").replace(' ',"")
    data = page.split("\n")

    for index in range(len(data)):
        if(index != 0):
            stats.append(  data[index].split(",") )
        #    if (len(sd) > 5):
        #        database_statistics.addStatisticData(sd[1],sd[2],sd[3],sd[4],sd[5],sd[6],sd[7],sd[8],sd[9])

    return stats

#SetupRouterConnection()
#addMacToWiFiBlock('00-00-00-00-00-11', 'test')
#getClientList()
#getStatistics()
