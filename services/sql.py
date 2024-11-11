import os
from typing import List, Optional

import sqlalchemy
from sqlalchemy.orm import (
  DeclarativeBase, Mapped, mapped_column, relationship, scoped_session, sessionmaker
)

from lib.recipe import Category, Tag
from models.recipe import Recipe, TagTable


engine = sqlalchemy.create_engine(os.environ.get('DATABASE_URL'))
Session = scoped_session(sessionmaker(bind=engine))


def fetch_all():
  return Session.query(Recipe).all()

def query_recipe(recipe_slug):
  try:
    return Session.query(Recipe).where(Recipe.slug==recipe_slug).one()
  except sqlalchemy.exc.NoResultFound:
    return None

def query_by_tag(t):
  return sorted([(r.name, r.slug) for r in Session.query(Recipe).filter(
                 Recipe.tags.any(TagTable.name==t)).all()])

def recipes_by_display_category():
  display_dict = {}

  cuisines = [c.name for c in Session.query(TagTable).where(
              TagTable.category == Category.CUISINE).all()]
  vegetables = [Tag.get(Tag.CHICKPEA), Tag.get(Tag.EGGPLANT), Tag.get(Tag.POTATO),
                Tag.get(Tag.SQUASH), Tag.get(Tag.SWEET_POTATO), Tag.get(Tag.EGG)]
  dishes = [Tag.get(Tag.STIR_FRY), Tag.get(Tag.FRIED_RICE), Tag.get(Tag.NOODLES)]
  food_types = [Tag.PASTA, Tag.SALAD, Tag.SANDWICH, Tag.SOUP, Tag.BREAD, Tag.BREAKFAST,
                Tag.DESSERT, Tag.DRINK]
  sffrn = 'Stir-Fry, Fried Rice, Noodles'
  other = 'Other Vegetables'

  tag_map = {tag.name: tag.display_name.title() for tag in Session.query(TagTable).all()}

  for t in cuisines:
    display_dict[tag_map[t]] = query_by_tag(t)

  display_dict[tag_map[Tag.CURRY]] = query_by_tag(Tag.CURRY)

  display_dict[sffrn] = []
  for t in dishes:
    display_dict[sffrn].extend(query_by_tag(t))

  for t in vegetables:
    display_dict[tag_map[t]] = query_by_tag(t)

  display_dict[other] = sorted([
    (r.name, r.slug) for r in Session.query(Recipe).filter(~Recipe.tags.any(
    TagTable.name.in_(cuisines + vegetables + food_types + dishes + [Tag.CURRY])))
  ])

  for t in food_types:
    display_dict[tag_map[t]] = query_by_tag(t)

  return display_dict
