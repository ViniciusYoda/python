from time import sleep

ha = int(input('Hora: '))
ma = int(input('Minutos: '))
sa = int(input('Segundos'))

h = 0
while h < 24:
    m = 0 
    while m < 60:
        s = 0
        while s < 60:
            print(f'{h:02}:{m:02}:{s:02}')
            if h==ha and m==ma and s==sa:
                sleep(1)
                print('Alarme')
                break
            s+=1
        if h==ha and m==ma:
            break
        m+=1
    if h==ha:
        break
    h+=1
    
    print("Alarme")
    
   # ☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !"#"#$%&'())*)+♦♦-./0012348;<=>6♥?@ABEKPUWQXY[][]\]\_``abdc☺efinsvwxyxyz{}|}~⌂Çüéâäàåççêëèï◙ìÄÅÉæÆ