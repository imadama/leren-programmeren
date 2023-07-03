from random import shuffle

schoenen_lijst = []
for schoen in [{
        "merk"  :  "Nike",
        "model" :  "Drunk Low Retro",
        "kleur" :  "wit/ zwart",
        "prijs" :  129.00,
        "maten" : [35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
    },{
        "merk"  :  "Adidas",
        "model" :  "Superstar",
        "kleur" :  "rood",
        "prijs" :  99.95,
        "maten" : [37, 38, 39, 40, 41, 42, 43, 44, 45]
    },
    {
        "merk"  :  "Adidas",
        "model" :  "Superstar",
        "kleur" :  "blauw",
        "prijs" :  109.95,
        "maten" : [37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
    },
    {
        "merk"  :  "Nike",
        "model" :  "Waffle Debut",
        "kleur" :  "zwart",
        "prijs" :  41.97,
        "maten" : [37, 40, 41, 46, 49]
    },
    {
        "merk"  :  "Timberland",
        "model" :  "Field Trekker",
        "kleur" :  "bruin",
        "prijs" :  49.47,
        "maten" : [43, 44, 45, 46, 47, 48]
    },
    {
        "merk"  :  "Adidas",
        "model" :  "Superstar",
        "kleur" :  "groen",
        "prijs" :  84.95,
        "maten" : [37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
    },
    {
        "merk"  :  "Nike",
        "model" :  "Air Max 270 kids",
        "kleur" :  "wit/ blauw",
        "prijs" :  69.95,
        "maten" : [33, 34, 35, 36, 37, 38, 39]
    },
    {
        "merk"  :  "Nike",
        "model" :  "Air 340 male",
        "kleur" :  "wit/ groen",
        "prijs" :  149.95,
        "maten" : [39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
    },
    {
        "merk"  :  "Nike",
        "model" :  "Air force 1",
        "kleur" :  "zwart",
        "prijs" :  119.99,
        "maten" : [41, 42, 43, 44, 45, 46, 47, 48]
    },
    {
        "merk"  :  "Puma",
        "model" :  "Monarch field",
        "kleur" :  "zwart",
        "prijs" :  49.95,
        "maten" : [33, 34, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
    },
    {
        "merk"  :  "Gaastra",
        "model" :  "Veelstedura",
        "kleur" :  "wit",
        "prijs" :  299.95,
        "maten" : [39, 40, 41, 42, 43, 44, 45, 46]
    },
    {
        "merk"  :  "Timberland",
        "model" :  "Adventure 2.0",
        "kleur" :  "bruin",
        "prijs" :  69.98,
        "maten" : [39, 41, 42, 43, 46]
    },
    {
        "merk"  :  "Timberland",
        "model" :  "Originals",
        "kleur" :  "bruin",
        "prijs" :  89.98,
        "maten" : [38, 39, 41, 42, 43, 44]
    },
    {
        "merk"  :  "Gaastra",
        "model" :  "Veelstedura kids",
        "kleur" :  "wit",
        "prijs" :  309.95,
        "maten" : [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
    },
    {
        "merk"  :  "Timberland",
        "model" :  "Tree vault",
        "kleur" :  "zwart",
        "prijs" :  109.98,
        "maten" : [33, 34, 35, 36, 37, 38, 39]
}]:
    shuffle(schoen['maten'])
    schoenen_lijst.append(schoen)

shuffle(schoenen_lijst)

fonetische_kleuren = {
    "rood"  : "rode",
    "wit"   : "witte",
    "blauw" : "blauwe",
    "bruin" : "bruine",
    "zwart" : "zwarte",
    "groen" : "groene",
    "wit/ blauw" : "combi wit/ blauwe",
    "wit/ groen" : "combi wit/ groen",
    "wit/ zwart" : "combi wit/ zwarte"
}