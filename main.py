# How to incorporate the different scripts? 

# Making sure prompt is not a programmed command
"""
    Example scenario
    prompt: Hvordan er været idag?
    answere: COMMAND weather()
    
"""
from execution_modules import weather, news_norway

answere = "         COMMAND news_norway()"
#remove the two newline commands.
answere = answere.strip()
print(answere)
if answere.startswith("COMMAND"):
    print("Run command")
    if answere.find("weather()") != -1:
        response = weather()
    elif answere.find("news_norway()") != -1:
        news, headlines = news_norway()
        #news og headlines er tuples.
        for i in range(len(news)):
             respone = news[i]
             

else:
    respone = answere



