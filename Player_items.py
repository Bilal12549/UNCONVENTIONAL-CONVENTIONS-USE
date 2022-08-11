class item:

  def __init__(self, name, damage, damage_message, heal, heal_message, description):
    self.name = name
    self.damage = damage
    self.heal = heal
    self.description = description


#-------------------------------------------------------#


class wooden_spork(item):
  def __init__(self):
    item.__init__(self, "wooden spork", 12, f"You poke your enemy with courageousness. You deal {self.damage} damage.", 1, f"mm woody. . . You heal {self.heal} health.", "Not the best, but at least it's not nothing.")



#----------#


class nothing(item):
  def __init__(self):
    item.__init__(self, "", 0, "Nothing happens", 0, "Does not and has not quenched anything", "Nothing, to see here. . .")

#----------#