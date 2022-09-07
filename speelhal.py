ticket = input ("Hoeveel tickts?:")
vrticket = input ("Hoeveel 5 minuten?:")  #per 5 min
kosten=  ((int (ticket)*7.45)+ ((int (vrticket) * 9)))
print ("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {} euro". format (kosten))