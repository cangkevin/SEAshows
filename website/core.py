import functools

from .rss_client import RSSClient
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

client = RSSClient()
bp = Blueprint('listing', __name__)


@bp.route('/')
def index():
    return redirect(url_for('.shows',
                            category='recently-added-can-dub',
                            page=1))


@bp.route('/movies/<category>/<page>')
def movies(category, page):
    response = client.get_movies(category, page)

    return render_template('listing/movies.html',
                           domains={'shows': client.show_categories,
                                    'movies': client.movie_categories},
                           current_category=category,
                           response=response)


@bp.route('/shows/<category>/<page>')
def shows(category, page):
    response = client.get_shows(category, page)

    return render_template('listing/shows.html',
                           domains={'shows': client.show_categories,
                                    'movies': client.movie_categories},
                           current_category=category,
                           response=response)


@bp.route('/episodes/<show_id>/<page>')
def episodes(show_id, page):
    response = client.get_episodes(show_id, page)

    return render_template('listing/episodes.html',
                           domains={'shows': client.show_categories,
                                    'movies': client.movie_categories},
                           current_show=show_id,
                           response=response)


@bp.route('/sources/<episode_id>')
def sources(episode_id):
    response = client.get_sources(episode_id)

    return render_template('listing/sources.html',
                           domains={'shows': client.show_categories,
                                    'movies': client.movie_categories},
                           response=response)