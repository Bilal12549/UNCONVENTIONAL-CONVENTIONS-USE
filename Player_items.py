class Item:

  def __init__(self, name, damage, damage_message, heal, heal_message, description):
    self.name = name
    self.damage = damage
    self.heal = heal
    self.description = description


#-------------------------------------------------------#


class wooden_spork(Item):
  def __init__(self):
    Item.__init__(self, "wooden spork", 12, f"You poke your enemy with courageousness. You deal 12 damage.", 0.000001, f"mm woody. . . You heal 0.000001 health.", "Not the best, but at least it's not nothing.")



#----------#


class nothing(Item):
  def __init__(self):
    Item.__init__(self, "", 0, "Nothing happens", 0, "Does not and has not quenched anything", "Nothing, to see here. . .")

#----------#