import os

from flask import Flask

from api.api import api_bp
from views.view import view_bp

app = Flask(__name__)

app.json_provider_class.ensure_ascii = False
app.register_blueprint(api_bp)
app.register_blueprint(view_bp)


# Вьюшка, отображающая ошибку - отсутствие страницы
@app.errorhandler(404)
def error_404(e):
    return f"Такой страницы не существует, пожалуйста вернитесь <a href='/' class='item__head'>назад</a>"


# Вьюшка, отображающая ошибку - отсутствие отклика сервера
@app.errorhandler(500)
def error_500(e):
    return "Сервер перегружен, пожалуйста, попробуйте зайти еще раз через пару минут"


if __name__ == '__main__':
    app.config['ROOT_PATH_DIR'] = os.path.realpath(__file__)
    app.run(debug=True)
