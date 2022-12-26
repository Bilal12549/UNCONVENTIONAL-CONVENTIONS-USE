import time

def fight(player, enemy, w_msg):
  while player.hp > 0
    player.update(enemy)
    time.sleep(2.5)
    enemy.update(player)
    if enemy.hp <= 0:
      break
  
  print(w_msg)
    