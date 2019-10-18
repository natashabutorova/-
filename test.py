import math as m
class geo():
    def __init__(self,*coord):
        if (len(coord)==0):
            coord=(0,0)
            self.fi=coord[0]
            self.lyambda=coord[1]
        elif(len(coord)==1):
            if (isinstance (coord[0], (int,float))):
                self.fi=coord[0]
                self.lyambda=0
            else:
                self.fi=coord[0][0]
                self.lyambda=coord[0][1]
        else:
                self.fi=coord[0]
                self.lyambda=coord[1]
    def tuda (self):
        a=6378137
        b=6356752.3142
        f=(a-b)/a
        e=m.sqrt(2*f-f**2)
        fi=self.fi*m.pi/180
        lyambda=self.lyambda*m.pi/180
        x=a*lyambda
        y=a*m.log(m.tan(m.pi/4+fi/2)*((1-e*m.sin(fi))/(1+e*m.sin(fi)))**(e/2))
        return x, y
    def obratno(self, x, y):
        a=6378137
        b=6356752.3142
        f=(a-b)/a
        e=m.sqrt(2*f-f**2)
        eh=e/2
        pih=m.pi/2
        ts=m.exp(-y/a)
        phi=pih-2*m.atan(ts)
        i=0
        dphi=1
        while True:
             con=e*m.sin(phi)
             dphi=pih-2*m.atan(ts*((1-con)/(1+con))**e)-phi
             phi=phi+dphi
             break
        lyambda=x/a
        fi=phi
        lyambda=lyambda*180/m.pi
        fi=fi*180/m.pi
        return fi, lyambda
        
g=geo(79, 180)
r=g.tuda()
p=g.obratno(20037508.342789244, 14885392.582663137)
print (r)
print (p)
