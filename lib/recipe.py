class Tag():
  INDIAN = "Indian"
  THAI = "Thai"
  CHINESE = "Chinese"
  JAPANESE = "Japanese"
  TEX_MEX = "Tex-Mex"
  MEDITERRANEAN = "Mediterranean"
  MIDDLE_EASTERN = "Middle Eastern"
  WEST_AFRICAN = "West African"
  ETHIOPIAN = "Ethiopian"

  CURRY = "curry"
  STIR_FRY = "stir-fry"
  FRIED_RICE = "fried-rice"
  NOODLES = "noodles"
  PASTA = "pasta"
  SALAD = "salad"
  SANDWICH = "sandwich"
  SOUP = "soup"
  BREAD = "bread"
  SAUCE = "sauce"

  EGG = "eggs"
  TOFU = "tofu"
  
  RICE = "rice"
  LENTIL = "lentils"
  CHICKPEA = "chickpeas"
  BLACK_BEAN = "black beans"
  WHITE_BEAN = "white beans"

  GREEN_BEAN = "green beans"
  EGGPLANT = "eggplant"
  BELL_PEPPER = "bell peppers"
  POBLANO = "poblano peppers"
  POTATO = "potatoes"
  SWEET_POTATO = "sweet potatoes"
  CAULIFLOWER = "cauliflower"
  BROCCOLI = "broccoli"
  TOMATO = "tomatoes"
  CORN = "corn"
  CARROT = "carrots"
  SQUASH = "squash"
  BEET = "beets"
  MUSHROOM = "mushrooms"

  SPINACH = "spinach"
  KALE = "kale"

  SNACK = "snack"
  BREAKFAST = "breakfast"
  DESSERT = "dessert"
  DRINK = "drinks"

  SPRING = "Spring"
  SUMMER = "Summer"
  AUTUMN = "Autumn"
  WINTER = "Winter"

  TAGS = [
    INDIAN, THAI, CHINESE, JAPANESE, TEX_MEX, MEDITERRANEAN, MIDDLE_EASTERN, WEST_AFRICAN, ETHIOPIAN,
    CURRY, STIR_FRY, FRIED_RICE, NOODLES, PASTA, SALAD, SANDWICH, SOUP, BREAD, SAUCE,
    EGG, TOFU,
    RICE, LENTIL, CHICKPEA, BLACK_BEAN, WHITE_BEAN, GREEN_BEAN,
    EGGPLANT, BELL_PEPPER, POBLANO, POTATO, SWEET_POTATO, CAULIFLOWER, BROCCOLI, TOMATO,
    CORN, CARROT, SQUASH, BEET, MUSHROOM,
    SPINACH, KALE,
    SNACK, BREAKFAST, DESSERT, DRINK,
    SPRING, SUMMER, AUTUMN, WINTER,
  ]

  TAG_KEYS = {tag: tag.lower().replace(" ", "-") for tag in TAGS}

  def get(t):
    return Tag.TAG_KEYS.get(t)

class Category():
  CUISINE = "cuisine"
  DISH_TYPE = "dish_type"
  MEAL = "meal"
  INGREDIENT = "ingredient"
  SEASON = "season"
