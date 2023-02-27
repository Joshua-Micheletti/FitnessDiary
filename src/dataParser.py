import re

backupCounter = 3


def readTXT(filepath):
    data = open(filepath, "r")
    text = data.read()
    data.close()
    
    lines = text.split("\n")
    
    elements = []
    elements.append([])
    
    current = 0
    
    for line in lines:
        if line == "":
            elements.append([])
            current += 1
        else:
            elements[current].append(line)
            
    elements = [value for value in elements if value != []]
        
            
    parsedElements = []
    
    for element in elements:
        parsedElements.append({})
        
        for data in element:
            if "/" in data:
                formattedDate = ""
                
                numbers = data.split("/")
                
                if len(numbers[0]) == 1:
                    numbers[0] = "0" + numbers[0]
                if len(numbers[1]) == 1:
                    numbers[1] = "0" + numbers[1]
                
                formattedDate += numbers[0] + "/" + numbers[1] + "/" + numbers[2]
                
                parsedElements[len(parsedElements) - 1]["date"] = formattedDate.replace(':', '')
                
            if "Weight" in data or "weight" in data:            
                value = ""
                
                for character in data:
                    if character.isdigit():
                        value += character
                    if character == "." or character == ",":
                        value += "."

                parsedElements[len(parsedElements) - 1]["weight"] = value
                
            if "Time" in data or "time" in data:
                value = ""
                
                index = 0
                
                for character in data:
                    if character.isdigit():
                        value += character
                    if (character == ":" or character == "." or character == "," or character == ";") and (data[index - 1].isdigit() and data[index + 1].isdigit()):
                        value += ":"
                        
                    index += 1
                        
                parsedElements[len(parsedElements) - 1]["time"] = value
                
            if "Distance" in data or "distance" in data:
                value = ""
                
                for character in data:
                    if character.isdigit():
                        value += character
                    if character == "." or character == ",":
                        value += "."
                        
                    parsedElements[len(parsedElements) - 1]["distance"] = value

        if not (parsedElements[len(parsedElements) - 1]["distance"] is None) and not(parsedElements[len(parsedElements) - 1]["time"] is None):
            timeComponents = parsedElements[len(parsedElements) - 1]["time"].split(":")
            parsedElements[len(parsedElements) - 1]["speed"] = str(((float(parsedElements[len(parsedElements) - 1]["distance"]) * 1000) / (float(timeComponents[0]) * 60 + float(timeComponents[1]))) * 3.6)   
        
    return(parsedElements)


def writeTXT(filepath, elements):
    global backupCounter
    
    data = open(filepath, "w")
    
    text = ""
    
    for element in elements:
        if "date" in element and len(element["date"]) != 0:
            text += element["date"] + ":\n"
        if "time" in element and len(element["time"]) != 0:
            text += "Time: " + element["time"] + "\n"
        if "distance" in element and len(element["distance"]) != 0:
            text += "Distance: " + element["distance"] + " Km\n"
        if "weight" in element and len(str(element["weight"])) != 0:
            text += "Weight: " + str(element["weight"]) + " Kg\n"
            
        text += "\n"
    
    data.write(text)
    
    data.close()
    
    backupCounter -= 1
    
    
    if backupCounter == 0:
        backupCounter = 5
        
        data = open(filepath + ".bak", "w")
    
        text = ""
        
        for element in elements:
            if "date" in element and len(element["date"]) != 0:
                text += element["date"] + ":\n"
            if "time" in element and len(element["time"]) != 0:
                text += "Time: " + element["time"] + "\n"
            if "distance" in element and len(element["distance"]) != 0:
                text += "Distance: " + element["distance"] + " Km\n"
            if "weight" in element and len(element["weight"]) != 0:
                text += "Weight: " + element["weight"] + " Kg\n"
                
            text += "\n"
        
        data.write(text)
        
        data.close()
    
    
    