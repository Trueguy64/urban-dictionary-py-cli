import webbrowser #imports the webbrowser module

while True:
    userWord=input("Enter your word: ") #Records the inputted word of the user
    urbanUrl=("https://www.urbandictionary.com/define.php?term=" + userWord) #Places the user's word into the URL term
    urbanUrl = urbanUrl.replace(' ', '%20') #Replaces spaces with correct formatting to prevent the program breaking due to the usage of traditional space
    webbrowser.open_new(urbanUrl) #Opens a new tab with the link combimed with the user's word
    yesList=["Yes", "yes", "Y", "y"] #A list of valid "yes", which allows the program to repeat itself
    noList=["No","no","N","n"]
    if input("Do you want to repeat (y/n): ") in noList: #If the user does not want to repeat the program, then by entering any phrase within the noList, they are able to exit out of it.
        break
