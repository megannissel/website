from itertools import groupby
from operator import attrgetter

from flask import redirect, render_template, url_for
from flask_login import login_required, current_user

from lib.roasting_ref import ROASTING_REF
from services.sql import recipes_by_display_category, query_recipe


def register_recipe_endpoints(app):

  @app.route('/recipes')
  @login_required
  def recipe_index():
    recipe_dict = recipes_by_display_category()
    return render_template('recipe_book/recipe_index.html',
      recipe_dict=recipe_dict,
      roasting_ref=sorted(ROASTING_REF, key=lambda item: item.food),
    )

  @app.route('/recipe/<recipe_name>')
  @login_required
  def recipe(recipe_name):
    recipe = query_recipe(recipe_name)

    if not recipe:
      return redirect(url_for('recipe_index'))

    ingredients = {k: sorted(g, key=lambda ingredient: ingredient.priority_number)
                   for k, g in groupby(recipe.ingredients, attrgetter('label'))}
    directions = {k: sorted(g, key=lambda direction: direction.step_number)
                   for k, g in groupby(recipe.directions, attrgetter('label'))}

    related_recipe = None
    if recipe.related_recipe:
      related_recipe = query_recipe(recipe.related_recipe)

    return render_template('recipe_book/recipe.html',
      recipe=recipe,
      ingredients=ingredients,
      directions=directions,
      related_recipe=query_recipe(recipe.related_recipe),
    )
