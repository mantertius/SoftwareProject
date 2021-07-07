import keyboard
import os
class Player:
    def __init__(self,hp,mp,att,_def,race) -> None:
        self.Health = hp
        self.Mana = mp
        self.Attack = att
        self.Defense = _def
        self.Race = race
    def attack(self,enemy):
        enemy.Hit(self.Attack)
        print("Atacando o "+ enemy.Race +" ...")
    def Buff(self):
        self.Attack += 1
        print("Buffado. Seu ataque é: " + str(self.Attack))

class Enemy:
    def __init__(self,hp,mp,att,_def,race) -> None:
        self.Health = hp
        self.Mana = mp
        self.Attack = att
        self.Defense = _def
        self.Race = race
    def Hit(self,att):
        a = max(0,att-self.Defense)
        self.Health -= a
        print(self.Race +" sofreu " + str(a) +" de dano.")
        if(self.Health <= 0):
            print(self.Race +" morreu.")
            print("Fim de jogo")
            quit()
        
        
        # if (att-self.Defense > 0):
        #     self.Health -= att - self
        # else:
        #     self.Health = 0 
        
Player1 = Player(100,100,5,3,"Human")
print(Player1.Health)
Enemy1 = Enemy(20,0,5,3,"Rat")

while True:
    print("Sua vida é "+ str(Player1.Health)+" e a vida do " + Enemy1.Race + " é "+ str(Enemy1.Health))
    a = input()
    if (keyboard.is_pressed('a')):
        Player1.attack(Enemy1)
    elif (keyboard.is_pressed('b')):
        Player1.Buff()
    elif (keyboard.is_pressed('q')):
        print("Saindo do jogo...")
        quit()