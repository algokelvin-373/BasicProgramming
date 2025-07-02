enemies = 1

def increase_enemy():
    global enemies
    enemies += 1
    print(f"Increasing enemy...")
    
print(f"Total enemy: {enemies}")
increase_enemy()
print(f"Total enemy: {enemies}")