from PIL import Image,ImageDraw
max_iter = 50


def mandelbrot(c):
    z=0
    i=0
    while abs(z) <= 2 and i<max_iter:
        z = z*z  + c
        i+=1
    return i

width,heigh = (600,400)
cx,cy,zoom = (-0.74384935657398,-0.1317013084796293,15)
minx,maxx,miny,maxy = (cx-1,cx+0.25,cy-0.25,cy+0.25)

for i in range(zoom):
    im = Image.new('HSV',(width,heigh),(0,0,0))
    draw = ImageDraw.Draw(im)

    x_pix=((maxx-minx)/width)
    y_pix = ((maxy-miny)/heigh)

    for x in range (width):
        for y in range (heigh):
            nx = minx + x_pix * x
            ny = miny + y_pix * y
            c= complex (nx,ny)
            iter = mandelbrot(c)
            heu = int(360 * (iter/max_iter))
            sat=200
            if iter < max_iter:
                value = 100
            else:
                value = 0
            draw.point([x,y],(heu,sat,value))
        im.convert('RGB').save(f'output{i}.png','PNG')


    spanx=maxx - minx
    spany = maxy - miny

    minx = minx + spanx/4
    maxx = maxx + spanx/4

    miny = miny + spany/32
    maxy = maxy + spany/32

