from turtle import exitonclick, forward, right, left, textinput, numinput, title, speed, color, goto, penup, pendown, pensize, circle

VELIKOST_POLE = 25   #Konstanta určující velikost pole mřížky.


# Název okna :
title("Pišqworky od Pepy verze 1.1")

# Nastavení hráčů:
hrac1 = textinput("Začátek hry!","Zadej jméno prvního hráče:")

# Kontrola vstupu. Pokud uživatel potvrdí jméno bez zadání znaku, bude vyzván k opětovnému zadání:

while hrac1 == "":        
    hrac1 = textinput("Chyba","Chyba, zadej platné jméno prvního hráče:")


hrac2 = textinput("Začátek hry!","Zadej jméno druhého hráče:")

# Kontrola vstupu. Pokud uživatel potvrdí jméno bez zadání znaku, či se bude jméno shodovat s prvním, bude vyzván k opětovnému zadání:

while hrac2 == "" or hrac1 == hrac2 :        
    hrac2 = textinput("Chyba","Chyba, zadej platné jméno druhého hráče:")

# Nastavení mřížky:

mrizka_x = numinput("Začátek hry!","Zadejte rozměr x hrací mřížky:")
mrizka_x_kontrola  = mrizka_x % 1 

while mrizka_x < 3 or mrizka_x_kontrola != 0: #Zbytek z celočíselného dělení, kontoluji, jestli je zbytkem nula, jinak bylo zadáno desetinné číslo = neplatný rozměr mřížky.

    mrizka_x = numinput("Chyba","Chyba, zadejte celočíselný rozměr x hrací mřížky, větší než 2:")
    mrizka_x_kontrola  = mrizka_x % 1 

mrizka_x = int(mrizka_x)


mrizka_y = numinput("Začátek hry!","Zadejte rozměr y hrací mřížky:")

mrizka_y_kontrola  = mrizka_y % 1 

while mrizka_y < 3 or mrizka_y_kontrola != 0: #Zbytek z celočíselného dělení, kontoluji, jestli je zbytkem nula, jinak bylo zadáno desetinné číslo = neplatný rozměr mřížky.

    mrizka_y = numinput("Chyba","Chyba, zadejte celočíselný rozměr y hrací mřížky, větší než 2:")
    mrizka_y_kontrola  = mrizka_y % 1 

mrizka_y = int(mrizka_y)


# Vykreslení mřížky

speed(0)
for _ in range(mrizka_y):
    for _ in range(mrizka_x):
        for _ in range(4):
            forward(VELIKOST_POLE)
            left(90)
        forward(VELIKOST_POLE)

    penup()
    left(180)
    forward(VELIKOST_POLE * mrizka_x)
    right(90)
    forward(VELIKOST_POLE)
    right(90)
    pendown()

# Podmínka, která ošetřuje různost dalšího cyklu v závislosti na počtu polí mřížky. Je-li počet polí lichý, int zaokrouhlí dolů a tak musím přičíst 1. 
# Zároveň ale přičítám k oběma variantám 1, aby vhodně fungovala fce range. Tzn. dohromady k sudým +1, k lichým +2.

if      (mrizka_x * mrizka_y) % 2 == 0:
    pocet_tahu = int((mrizka_x * mrizka_y)/2+1)
elif    (mrizka_x * mrizka_y) % 2 != 0:
    m = int((mrizka_x * mrizka_y)/2)
    pocet_tahu = int(m+2)

for i in range(1, pocet_tahu):         # Cyklus zajišťující konec hry po zaplnění hracího pole

    # Sběr souřadnic:

    sour_x = numinput(f"Tah {i} hráče {hrac1}", f"{hrac1}, zvol souřadnici x svého tahu:")

    #Kontrola vstupu, prázdný vstup None je ošetřen defaultně
    while sour_x < 1 or sour_x > mrizka_x or sour_x % 1 != 0 :
            
        sour_x = numinput(f"Tah {i} hráče {hrac1}","Chybná souřadnice x, zadej platnou:")


    sour_y = numinput(f"Tah {i} hráče {hrac1}", f"{hrac1}, zvol souřadnici y svého tahu:")

    while sour_y < 1 or sour_y > mrizka_x or sour_y % 1 != 0 :
            
        
        sour_y = numinput(f"Tah {i} hráče {hrac1}","Chybná souřadnice y, zadej platnou:")
            

    x = sour_x * VELIKOST_POLE - VELIKOST_POLE        # Jedno políčko má k pixelů, proto násobím. Odčítám pro to, aby kreslení začínalo v levém dolním rohu (pro 1,1 pixel 0,0)
    y = sour_y * VELIKOST_POLE - VELIKOST_POLE


    # kreslení křížku na zadaných souřadnicích:
    penup()
    goto([x,y])
    pendown()
    pensize(2)
    color("blue")
    goto([x+VELIKOST_POLE,y+VELIKOST_POLE])
    penup()
    goto([x+VELIKOST_POLE,y])
    pendown()
    goto([x,y+VELIKOST_POLE])

    if i+1 == pocet_tahu and mrizka_x*mrizka_y%2 != 0:   # Hraje-li se na lichý počet polí, program zde v posledním kole zajistí, aby nemohl hrát hráč 2, který už by neměl volné pole.
        break



    sour2_x = numinput(f"Tah {i} hráče {hrac2}", f"{hrac2}, zvol souřadnici x svého tahu:")

    #Kontrola vstupu, prázdný vstup None je ošetřen samotnou fcí numinput
    while sour2_x < 1 or sour2_x > mrizka_x or sour2_x % 1 != 0 :

        sour2_x = numinput(f"Tah {i} hráče {hrac2}","Chybná souřadnice x, zadej platnou:")
            

    sour2_y = numinput(f"Tah {i} hráče {hrac2}", f"{hrac2}, zvol souřadnici y svého tahu:")

    #Kontrola vstupu, prázdný vstup None je ošetřen samotnou fcí numinput
    while sour2_y < 1 or sour2_y > mrizka_y or sour2_y % 1 != 0 :
        
        sour2_y = numinput(f"Tah {i} hráče {hrac2}","Chybná souřadnice y, zadej platnou:")   

# Úprava souřadnic tak, aby kolečko bylo vykresleno uvnitř zvoleného pole mřížky:
    x2 = sour2_x * VELIKOST_POLE - (VELIKOST_POLE / 2)    # Násobení k <- jedno pole má k pixelů. Minus (k/2) -> Dostane se doprostřed pole na x-ové ose
    y2 = sour2_y * VELIKOST_POLE - (0.9 * VELIKOST_POLE)  # Násobení k <- jedno pole má k pixelů. Minus (0,9k) -> Dostane se do spodní části pole na y-ové ose


    # kreslení kolečka na zadaných souřadnicích:
    penup()
    goto([x2,y2])
    pendown()
    pensize(2)
    color("red")
    circle(0.4*VELIKOST_POLE,360)

exitonclick()
print(f"Děkuji, že jste hráli Pišqworky od Pepy, {hrac1} a {hrac2}! Gratuluji vítězi.")