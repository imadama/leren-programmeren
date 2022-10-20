#vraag de gebruiker om een woord
#print het woord 2x naast elkaar: appel appel
#print de letters van het woord in om gekeerde
#         volgorde aan elkaar : leppa

woord = input("Vertel een woord!")
#for i in woord:
#    for x in range(2):
#       print(i, end= "")
newWoord = ""
for letter in woord:
    newWoord += letter+letter
print(newWoord)

print(woord) [::-1]