enemies = 1


'''def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")'''

#Local Scope
'''def drink_portion():
    portion_strength = 2
    print(portion_strength)
    
drink_portion()
print(portion_strength)'''

#Global Scope
player_health = 10

def game():
    def drink_portion():
        portion_strength = 2
        print(portion_strength)

    drink_portion()

print(player_health)
