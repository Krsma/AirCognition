
# tuples = (key, nubmer of pages, link) => generates a json with links 
# krnji linkovi da ne bih morao da se cimam sa skidanjem brojeva

# F35, F16, F15, F14, A10
# Su27, MiG31, Su25, Su35, Mig29
# Rafale, Typhon, Saab Gripen , Super Tucano
# Panavia Tornado, J10, Harier

inputSceletons = [("Dassault Rafale", "https://www.airfighters.com/photosearch.php?cra=823&lim=5&dis=tiles&pag=", 17),
                ("Saab JS-39 Grippen", "https://www.airfighters.com/photosearch.php?cra=2022&lim=5&dis=tiles&pag=", 19),
                ("Lockheed Martin F35 Lightning II", "https://www.airfighters.com/photosearch.php?cra=2992&lim=5&dis=tiles&pag=", 14),
                ("Embraer  EMB314 Super Tucano", "https://www.airfighters.com/photosearch.php?cra=6980&lim=5&dis=tiles&pag=", 2),
                ("Eurofighter EF2000 Typhon", "https://www.airfighters.com/photosearch.php?cra=2167&lim=5&dis=tiles&pag=", 77),
                ("Sukhoi Su25", "https://www.airfighters.com/photosearch.php?cra=1344&lim=5&dis=tiles&pag=", 2)
                ]


outputPath = "imagePaths.json"

def generateLinks(sceleton, numberofLinks):
    return [sceleton+str(n) for n in range(1,numberofLinks+1)]

def generateAllLinks(sceletons):
    return {key: generateLinks(sceleton, numberOfLinks) for key, sceleton, numberOfLinks in sceletons}

if __name__ == "__main__":
    print(generateAllLinks(inputSceletons))