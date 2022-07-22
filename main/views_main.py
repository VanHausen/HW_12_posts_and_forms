import logging

from flask import Blueprint, render_template, request

from json import JSONDecodeError

from functions import get_posts_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates_name')

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', query=search_query, posts=posts)
