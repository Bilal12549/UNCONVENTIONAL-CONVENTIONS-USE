class item:

  def __init__(self, name, damage, heal, description):
    self.name = name
    self.damage = damage
    self.heal = heal
    self.description = description


#-------------------------------------------------------#


class wooden_spork(item):
  def __init__(self):
    item.__init__(self, "wooden spork", 12, 1, "Not the best, but at least it's not nothing.")

#----------#


class nothing(item):
  def __init__(self):
    item.__init__(self, ".", 0, 0, "Nothing, to see here. . .")

#----------#