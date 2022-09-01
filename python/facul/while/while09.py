h = 0 #horas 
while h < 24:
    m = 0 #minutos
    while m < 60:
        s = 0 #segundos
        while s < 60:
            print(f'{h:02}:{m:02}:{s:02}')
            s+=1
        m+=1
    h+=1
    
    