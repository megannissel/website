from typing import List, Optional

from sqlalchemy import Column, Table, ForeignKey, Integer, String
from sqlalchemy.orm import (
  Mapped, mapped_column, relationship, scoped_session, sessionmaker
)

from models.base import Base


recipes_tags = Table(
  "recipe_tag",
  Base.metadata,
  Column("recipe_id", ForeignKey("recipe.slug"), primary_key=True),
  Column("tag_id", ForeignKey("tag.name"), primary_key=True),
)


class Recipe(Base):
  __tablename__ = "recipe"

  slug: Mapped[str] = mapped_column(primary_key=True)
  name: Mapped[str]
  link: Mapped[str]
  mid_note: Mapped[Optional[str]]
  footnote: Mapped[Optional[str]]
  related_recipe: Mapped[Optional[str]]

  ingredients: Mapped[List["Ingredient"]] = relationship(back_populates="recipe_c")
  directions: Mapped[List["Direction"]] = relationship(back_populates="recipe_c")

  tags: Mapped[List["TagTable"]] = relationship(secondary=recipes_tags, back_populates="recipes")


class Ingredient(Base):
  __tablename__ = "ingredient"

  i_id: Mapped[int] = mapped_column(primary_key=True)
  priority_number: Mapped[int]
  ingredient: Mapped[str]
  label: Mapped[Optional[str]]
  recipe: Mapped[str] = mapped_column(ForeignKey("recipe.slug"))
  recipe_c: Mapped["Recipe"] = relationship(back_populates="ingredients")


class Direction(Base):
  __tablename__ = "direction"

  d_id: Mapped[int] = mapped_column(primary_key=True)
  step_number: Mapped[int]
  step: Mapped[str]
  label: Mapped[Optional[str]]
  recipe: Mapped[str] = mapped_column(ForeignKey("recipe.slug"))
  recipe_c: Mapped["Recipe"] = relationship(back_populates="directions")


class TagCategory(Base):
  __tablename__ = "tag_category"

  name: Mapped[str] = mapped_column(primary_key=True)

  tags: Mapped[List["TagTable"]] = relationship()


class TagTable(Base):
  __tablename__ = "tag"

  name: Mapped[str] = mapped_column(primary_key=True)
  display_name: Mapped[str]
  category: Mapped["TagCategory"] = mapped_column(ForeignKey("tag_category.name"))

  recipes: Mapped[List["Recipe"]] = relationship(secondary=recipes_tags, back_populates="tags")
