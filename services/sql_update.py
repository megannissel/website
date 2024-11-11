import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from lib.recipe import Tag
from models.recipe import Recipe, Ingredient, Direction, TagCategory, TagTable, recipes_tags


def get_conn():
  return sqlalchemy.create_engine(os.environ.get('DATABASE_URL'))

def add_recipe(recipes):
  engine = get_conn()
  with engine.connect():
    session = sessionmaker(bind=engine)()

    rows = []
    for recipe in recipes:
      if recipe.get('related_recipes'):
        related_recipe = recipe['related_recipes'][0]
      else:
        related_recipe = None
      row = Recipe(
        slug=recipe['slug'],
        name=recipe['name'],
        link=recipe['link'],
        mid_note=recipe.get('ingredients_note'),
        footnote=recipe.get('footnote'),
        related_recipe=related_recipe,
      )
      rows.append(row)
    
    session.add_all(rows)
    session.commit()

  return "OK"

def add_ingredients_directions(recipes):
  engine = get_conn()
  with engine.connect():
    session = sessionmaker(bind=engine)()

    rows = []

    for recipe in recipes:
      ingredients = recipe['ingredients']
      directions = recipe['directions']

      if isinstance(ingredients, dict):
        for category, ingredients_list in ingredients.items():
          for i, ing in enumerate(ingredients_list):
            row = Ingredient(
              priority_number = i,
              ingredient = ing,
              label = category,
              recipe = recipe['slug']
            )
            rows.append(row)
      else:
        for i, ing in enumerate(ingredients):
          row = Ingredient(
            priority_number = i,
            ingredient = ing,
            recipe = recipe['slug']
          )
          rows.append(row)
    
      if isinstance(directions, dict):
        for category, directions_list in directions.items():
          for i, dir in enumerate(directions_list):
            row = Direction(
              step_number = i+1,
              step = dir,
              label = category,
              recipe = recipe['slug']
            )
            rows.append(row)
      else:
        for i, dir in enumerate(directions):
          row = Direction(
            step_number = i+1,
            step = dir,
            recipe = recipe['slug']
          )
          rows.append(row)

    session.add_all(rows)
    session.commit()

  return "OK"

def add_tags(tag_tuples):
  engine = get_conn()
  with engine.connect():
    session = sessionmaker(bind=engine)()

    rows = []
    for tag_tuple in tag_tuples:
      row = Tag(
        name = tag_tuple[0],
        display_name = tag_tuple[1],
      )
      rows.append(row)

    session.add_all(rows)
    session.commit()

  return "OK"

def add_tag_recipe(recipes):
  engine = get_conn()
  with engine.connect():
    session = sessionmaker(bind=engine)()

  recipe_tag_pairs = []

  for recipe in recipes:
    for tag in recipe['tags']:
      recipe_tag_pairs.append((recipe['slug'], Tag.TAG_KEYS[tag]))

  for recipe_slug, tag_name in recipe_tag_pairs:
    session.execute(recipes_tags.insert().values(recipe_id=recipe_slug, tag_id=tag_name))

  session.commit()
  return "OK"
