from platform import java_ver


geel = input("Is de kaas geel?")
if geel == "ja":
    gaten = input("Zitten er gaten in?")
    if gaten == "ja":
        duur = input("Is de kaas belagelijk duur?")
        if duur == "ja":
            print("Emmenthaler")
        elif "nee":
            print("Leerdammer")
    elif "nee":
        steen = input("Is de kaas hard als steen?")
        if steen == "ja":
            print("Parmigiano Reggiano")
        elif "nee":
            print("Goudse kaas")
    
elif "nee":
    blauwe = input("Heeft de kaas blauwe schimmel?")
    if blauwe == "ja":
        korst = input("Heeft de kaas een korst?")
        if korst == "ja":
            print("Blue de Rochbaron")
        elif "nee":
            print("Foume d'Ambert")
    elif "nee":
        korst2 = input("Heeft de kaas een korst?")
        if korst2 == "ja":
            print("Camembert")
        elif "nee":
            print("Mozzarella")