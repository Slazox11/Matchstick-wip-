from random import randint
bot = randint(1,3)
Allumettes = 21
Player = 21

def main(Allumettes):
    while(Allumettes>0):
     Player = int(input("Veuillez tirer un nombre d'allumette(s) compris entre 1 et 3\n"))

     while(Player>3 or Player<1):
      if (Allumettes>3 or Allumettes<1):
        print("Impossible de réaliser cela, réesayez ultérieurement")
      break
     while(Allumettes>0):
      if(Player == 1):
          Allumettes-1
          Allumettes-Player-bot
          print("vous avez choisis de retirer 1 allumette, il reste",Allumettes-Player,"allumettes")
          print("votre ennemi vient tout juste d'enlever 1 allumette. il reste ",Allumettes-Player-bot,"allumettes\n")
          break
      elif(Player == 2):
          Allumettes-2
          Allumettes-Player-bot
          print("vous avez choisis de retirer deux allumettes, il reste",Allumettes-Player,"allumettes")
          print("votre ennemi vient tout juste d'enlever deux allumettes. il reste",Allumettes-Player-bot,"allumettes\n")
          break
      elif(Player == 3):
          Allumettes-3
          Allumettes-Player-bot
          print("vous avez choisis de retirer 3 allumettes, il reste",Allumettes-Player,"allumettes")
          print("votre ennemi vient tout juste d'enlever trois allumettes. il reste",Allumettes-Player-bot,"allumettes\n")
          break
main(Allumettes)

def game():
    while(Allumettes != 0):
        if Allumettes-Player == 0:
            print("Vous avez perdu, vous ferez mieux que la prochaine fois")
        elif Allumettes-bot == 0:
            print("Votre ennemi a perdu la partie, Félicitations à toi d'avoir gagné! ")
game()

