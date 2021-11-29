import microbit
import os

arr = [[False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]]

def quit():
    exit()

def on(x, y):
    if((x < 0 or x > 4) or (y < 0 or y > 4)):
        print('Invalid LED.')
    else:
        microbit.display.set_pixel(x, y, 9)

def off(x, y):
    if((x < 0 or x > 4) or (y < 0 or y > 4)):
        print('Invalid LED.')
    else:    
        microbit.display.set_pixel(x, y, 0)
    
def blink(q, z, x, y):
    if((x < 0 or x > 4) or (y < 0 or y > 4)):
        print('Invalid LED.')
    elif(z < 0 or z > 20):
        print('Invalid count value.')
    else:
        for i in range (z):
            on(x,y)
            microbit.sleep(q)
            off(x,y)
            microbit.sleep(q)

def toggle(x, y):
    if((x < 0 or x > 4) or (y < 0 or y > 4)):
        print('Invalid LED.')
    else:
        if(arr[x][y] == True):
            arr[x][y] = False
            off(x, y)
        else:
            arr[x][y] = True
            on(x, y)
        
def button(but):
    if (but == 'a'):
        print('True')
    elif(but == 'b'):
        print('False')
    else:
        print('Invalid button.')
        
def set_brightness(a, x, y):
    if((x < 0 or x > 4 ) or (y < 0  or y > 4)):
        print('Invalid LED.')
    elif(a < 0 or a > 9):
        print('Invalid brightness.')
    else:
        microbit.display.set_pixel(x, y, a)
        print(a)
    
def brightness(x, y):
    if((x < 0 or x > 4 ) or (y < 0  or y > 4)):
        print('Invalid LED.')
    else:
        print(microbit.display.get_pixel(x, y))

        
def light():
    a = microbit.display.read_light_level()
    print(a)
        
while True:
    line = input('cmd: ')
    parsed = line.split()
    if(parsed[0] == 'led'):
        if(parsed[1] == 'on'):
            on(int(parsed[2]), int(parsed[3]))
            
        elif(parsed[1] == 'off'):
            off(int(parsed[2]), int(parsed[3]))
            
        elif(parsed[1] == 'blink'):
            blink(int(parsed[2]), int(parsed[3]), int(parsed[4]), int(parsed[5]))
        
        elif(parsed[1] == 'toggle'):
            toggle(int(parsed[2]), int(parsed[3]))
            
        elif(parsed[1] == 'brightness'):
            if(len(parsed) >= 3):
                if(parsed[2] == 'set'):
                    set_brightness(int(parsed[3]), int(parsed[4]), int(parsed[5]))
                else:    
                    brightness(int(parsed[2]), int(parsed[3]))
            else:
                print('Invalid command.')
                
    elif(parsed[0] == 'button'):
        button(parsed[1])
    
    elif(parsed[0] == 'light'):
        light()

    elif(parsed[0] == 'temperature'):
        if(parsed[1] == 'c'):
            cels = microbit.temperature()
            print(cels)
        elif(parsed[1] == 'f'):
            fahr = microbit.temperature()
            print(fahr * 1.8 + 32)
        elif(parsed[1] == 'k'):
            kelv = microbit.temperature()
            print(kelv + 273.15)
            
    elif(parsed[0] == 'exit' or parsed[0] == 'quit'):
        quit()

    elif(parsed[0] == 'mv'):
        try:
            if(os.path.isfile(parsed[1]) == True):
                os.rename(parsed[1],parsed[2])
        except Exception as e:
            print('Cannot move file.')

    elif(parsed[0] == 'rm'):
        try:
            if(parsed[1] == '-r' or parsed[1] == '-R' or parsed[1] == '--recursive'):
                if(os.path.isfile(parsed[2]) == True):
                    os.remove(parsed[2])
            elif(os.path.isfile(parsed[1]) == True):
                filesize = os.path.getsize(parsed[1])
                if(filesize == 0):
                    os.remove(parsed[1])
                else:
                    print('Cannot remove file. File not empty.')
        except Exception as e:
            print('Cannot remove file.')

    elif(parsed[0] == 'echo'):
        if(parsed[1] == '-n'):
            text = parsed[2]
            for i in range(3, len(parsed)):
                text = text + ' ' + parsed[i]
            print(text, end = '')
        else:
            text = parsed[1]
            for i in range(2, len(parsed)):
                text = text + ' ' + parsed[i]
            print(text)

    elif(parsed[0] == 'cat'):
        try:
            for i in range(1, len(parsed)):
                fd = os.open(parsed[i], os.O_RDONLY)
                catfile = os.read(fd, 10000)
                catfile1 = catfile.decode('utf-8')
                print(catfile1)
                os.close(fd)
        except Exception as e:
            print('Cannot remove file. File not empty.')

    elif(parsed[0] == 'cp'):
        try:
            if(os.path.isfile(parsed[1]) == True):
                fd = os.open(parsed[1], os.O_RDONLY)
                fd1 = os.open(parsed[2], os.O_RDWR | os.O_CREAT)
                cpfile = os.read(fd, 10000)
                os.write(fd1, cpfile)
                os.close(fd)
                os.close(fd1)
        except Exception as e:
            print('Cannot copy file.')

    elif(parsed[0] == 'ls'):
        if(len(parsed) == 1):
            pathls = os.getcwd()
            cmd = os.listdir(pathls)
            for i in cmd:
                if not i.startswith('.'):
                    print(i)
        elif(len(parsed) <= 2):
            if(parsed[1] == '-a' or parsed[1] == '--all'):
                pathls = os.getcwd()
                cmd = os.listdir(pathls)
                for i in cmd:
                    print(i)
            elif(parsed[1] == '-l' or parsed[1] == '--long'):
                pathls = os.getcwd()
                cmd = os.listdir(pathls)
                for i in cmd:
                    if not i.startswith('.'):
                        statinfo = os.stat(i)
                        print(str(statinfo.st_size) + ' ' + i)
        elif(len(parsed) >= 3):
            if(((parsed[1] == 'l'or parsed[1] == '--long') and (parsed[2] == '-a' or parsed[2] == '--all')) or ((parsed[1] == '-a' or parsed [1] == '--all')and (parsed[2] == '-l' or parsed[2] == '--long'))):
                pathls = os.getcwd()
                cmd = os.listdir(pathls)
                for i in cmd:
                    statinfo = os.stat(i)
                    print(str(statinfo.st_size) + ' ' + i)

    else:
        print('Invalid command.')