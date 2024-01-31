import random
from flask import render_template
from datetime import datetime

def getWeatherReal():
    z=random.randint(1,5)
    mnk=datetime.now()
    monat=mnk.month
    w=["f065","f001","f004","f006","f002"]
    h=["f009","f001","f008","f000","f003"]
    s=["f00d","f07d","f00c","f009","f072"]
    f=["f001","f009","f07d","f002","f085"]
    #Januar
    if monat==1:
        if z==1:
            imageSRC1=w[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=w[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=w[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=w[3]
            return(imageSRC4)
        else:
            imageSRC5=w[4]
            return(imageSRC5)
    #Februar
    elif monat==2:
        if z==1:
            imageSRC1=w[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=w[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=w[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=w[3]
            return(imageSRC4)
        else:
            imageSRC5=w[4]
            return(imageSRC5)
    #März
    elif monat==3:
        if z==1:
            imageSRC1=f[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=f[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=f[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=f[3]
            return(imageSRC4)
        else:
            imageSRC5=f[4]
            return(imageSRC5)
    #April
    elif monat==4:
        if z==1:
            imageSRC1=f[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=f[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=f[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=f[3]
            return(imageSRC4)
        else:
            imageSRC5=f[4]
            return(imageSRC5)
    #Mai
    elif monat==5:
        if z==1:
            imageSRC1=s[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=s[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=s[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=s[3]
            return(imageSRC4)
        else:
            imageSRC5=s[4]
            return(imageSRC5)
    #Juli
    elif monat==6:
        if z==1:
            imageSRC1=s[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=s[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=s[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=s[3]
            return(imageSRC4)
        else:
            imageSRC5=s[4]
            return(imageSRC5)
    #Juli
    elif monat==7:
        if z==1:
            imageSRC1=s[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=s[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=s[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=s[3]
            return(imageSRC4)
        else:
            imageSRC5=s[4]
            return(imageSRC5)
    #August
    elif monat==8:
        if z==1:
            imageSRC1=s[0]
            return(imageSRC1) 
        elif z==2:
            imageSRC2=s[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=s[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=s[3]
            return(imageSRC4)
        else:
            imageSRC5=s[4]
            return(imageSRC5)
    #Septemper
    elif monat==9:
        if z==1:
            imageSRC1=h[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=h[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=h[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=h[3]
            return(imageSRC4)
        else:
            imageSRC5=h[4]
            return(imageSRC5)
    #Oktober
    elif monat==10:
        if z==1:
            imageSRC1=h[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=h[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=h[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=h[3]
            return(imageSRC4)
        else:
            imageSRC5=h[4]
            return(imageSRC5)
    #November
    elif monat==11:
        if z==1:
            imageSRC1=w[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=w[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=w[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=w[3]
            return(imageSRC4)
        else:
            imageSRC5=w[4]
            return(imageSRC5)
    #Dezember
    else:
        if z==1:
            imageSRC1=w[0]
            return(imageSRC1)
        elif z==2:
            imageSRC2=w[1]
            return(imageSRC2)
        elif z==3:
            imageSRC3=w[2]
            return(imageSRC3)
        elif z==4:
            imageSRC4=w[3]
            return(imageSRC4)
        else:
            imageSRC5=w[4]
            return(imageSRC5)
   
def getContent():
    return render_template("weather(real)/index.html"),200

def createPlugin(plugin):
    plugin.name("weather(real)")
    plugin.describe("prints put current weather")
    plugin.api("weather(real)", getWeatherReal)
    plugin.content(getContent)