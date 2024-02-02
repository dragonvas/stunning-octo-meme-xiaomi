anime=0
o=0
oo=0
x=0
xx=0
c=0
z=0
v=1
po=1
aa=45
dirx=100
def setup():
    size(1000,1000)
def draw():
    global anime,o,oo,x,xx,c,z,t,q,r,u,s,J,p,m,v,po,aa,dirx
    background (0 ,150 ,0)
    if anime == 0:
        background (0 ,150 ,0)
        fill (oo,0,0)
        ellipse (700 ,700 ,50 ,50)
        fill (0,x,0)
        ellipse (100 ,100 ,50 ,50)
        fill (0,0,o)
        ellipse (900 ,700 ,30 ,30)
        fill (xx,xx,0)
        ellipse (200 ,700 ,50 ,50)
        fill (0,c,c)
        ellipse (10 ,600 ,50 ,50)
        fill (z,0,z)
        ellipse (700 ,800 ,50 ,50)
        o=o+1
        oo=oo+2
        x=x+3
        xx=xx+4
        c=c+5
        z=z+6
        if oo >= 255:
            oo=0
        if o >= 255:
            o=0
        if x >= 255:
            x=0
        if xx >= 255:
            xx=0
        if c >= 255:
            c=0
        if z >= 255:
            z=0
    if anime == 1:
        background (0 ,150 ,0)
        fill(255)
        r=random(255)
        u=random(255)
        t=random(255)
        q=random(50)
        J=random(1000)
        s=random(1000)
        m=random(1000)
        p=random(1000)
        stroke (t ,r ,u)
        strokeWeight (q)
        line (500,500,s,J)
        line (500,500,m,p)
    if anime == 2:
        background (0 ,150 ,0)
        fill(255)
        ellipse  (500 ,v ,50 ,50)
        v=v+dirx
        if v > 990:
            ellipse (500 ,v ,50 ,50)
            dirx=-100
            v=v+dirx
        if v < 10:
            ellipse (500 ,v ,50 ,50)
            dirx=100
            v=v+dirx
    if anime > 2:
        background (0 ,150 ,0)
        anime=anime-anime
def mouseClicked():
    global anime
    anime=anime+1
