#matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
import time
G           = 6.67e-11
Ms          = 2.0e30
Me          = 5.972e29
AU          = 1.5e11
daysec      = 24.0*60*60
e_ap_v      = 29290
gravconst_e = G*Me*Ms
xe,ye,ze    = 1.0167*AU,0,0
xve,yve,zve = 0,e_ap_v,0
xs,ys,zs    = 0,0,0
xvs,yvs,zvs = 0,0,0
t           = 0.0
dt          = 1*daysec
xelist,yelist,zelist = [],[],[]
xslist,yslist,zslist = [],[],[]
while(t<5*365*daysec):
    rx,ry,rz = xe - xs, ye - ys, ze - zs
    modr3_e = (rx**2+ry**2+rz**2)**1.5
    if(modr3_e > 0):
        fx_e = -gravconst_e*rx/modr3_e
        fy_e = -gravconst_e*ry/modr3_e
        fz_e = -gravconst_e*rz/modr3_e
        if(Me > 0):
            xve += fx_e*dt/Me
            xe += xve*dt
            xelist.append(xe)
            yve += fy_e*dt/Me
            ye += yve*dt
            yelist.append(ye)
            zve += fz_e*dt/Me
            ze += zve*dt
            zelist.append(ze)
        if(Ms > 0):
            xvs += -fx_e*dt/Ms
            xs += xvs*dt
            xslist.append(xs)
            yvs += -fy_e*dt/Ms
            ys += yvs*dt
            yslist.append(ys)
            zvs += -fz_e*dt/Ms
            zs += zvs*dt
            zslist.append(zs)
    t +=dt
print('data ready')
fig, ax = plt.subplots(figsize=(6,6))
if(ax):
    ax.set_aspect('equal')
    ax.grid()
    line_e,     = ax.plot([],[],'-g',lw=1,c='blue')
    point_e,    = ax.plot([AU], [0], marker='o', markersize=4, markeredgecolor='blue', markerfacecolor='blue')
    text_e      = ax.text(AU,0,'Earth')
    point_s,    = ax.plot([0], [0], marker='o', markersize=7, markeredgecolor='yellow', markerfacecolor='yellow')
    text_s      = ax.text(0,0,'Sun')
    exdata,eydata = [],[]
    sxdata,sydata = [],[]
    print(len(xelist))
    pause=False
    def update(i):
        global pause
        if(i<1000 and pause is False):
            time.sleep(0.1)
            if(xelist):
                exdata.append(xelist[i])
                if(yelist):
                    eydata.append(yelist[i])
                    line_e.set_data(exdata,eydata)
                    point_e.set_data(xelist[i],yelist[i])
                    text_e.set_position((xelist[i],yelist[i]))
                    point_s.set_data(xslist[i],yslist[i])
                    text_s.set_position((xslist[i],yslist[i]))
                    ax.axis('equal')
                    ax.set_xlim(-2*AU,6*AU)
                    ax.set_ylim(-2*AU,6*AU)
        else:
            pause=True
        return line_e,point_s,point_e,text_e,text_s
    anim = animation.FuncAnimation(fig,func=update,frames=len(xelist),interval=1,blit=True)
    plt.show()
