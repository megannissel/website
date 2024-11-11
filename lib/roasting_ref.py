from collections import namedtuple


RoastRef = namedtuple('RoastRef', ['food', 'temp', 'time'])
ROASTING_REF = [
  RoastRef("Spaghetti Squash", "400", "30-40 min"),
  RoastRef("Cauliflower", "450", "25-35 min"),
  RoastRef("Butternut Squash", "400", "45-60 min"),
  RoastRef("Beets", "375", "60-90 min"),
  RoastRef("Sweet Potatoes", "425", "30-40 min"),
  RoastRef("Potatoes", "400", "30-40 min"),
  RoastRef("Asparagus", "425", "10-15 min"),
  RoastRef("Brussles Sprouts", "400", "10-15 min + broil"),
  RoastRef("Eggplant Slices", "400", "15 min / side"),
]
