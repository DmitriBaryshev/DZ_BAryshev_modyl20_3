from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Главная'


@app.route('/writers')
def writers():
    return 'Писатели'


@app.route('/books')
def books():
    return 'Топ лучших книг'


@app.route('/writers/<writer>')
def writer_info(writer):
    if writer == 'Hemingway':
        return 'Информация о Хемингуэе'
    elif writer == 'Shakespeare':
        return 'Информация о Шекспире'
    else:
        return redirect('/writers')


@app.route('/books/<int:rank>')
def book_info(rank):
    if rank == 1:
        return 'Информация о книге на первом месте в топе'
    elif rank == 3:
        return 'Информация о книге на третьем месте в топе'
    else:
        return redirect('/books')


@app.route('/writers/<writer>/<book>')
def book_by_writer(writer, book):
    if writer == 'Hemingway' and book == 'The_Old_Man_and_the_Sea':
        return 'Информация о книге "Старик и море"'
    elif writer == 'Hemingway' and book == 'The_Sun_Also_Rises':
        return 'Информация о книге "И восходит солнце"'
    else:
        return redirect(f'/writers/{writer}')


@app.route('/writers/')
def writer_books():
    writer = request.args.get('writers')
    year = request.args.get('year')
    if writer == 'Hemingway' and year == '1926':
        return 'Информация о книгах Хемингуэя в 1926 году'
    else:
        return redirect(f'/writers/{writer}')


@app.route('/cities/')
def writer_books_city():
    writer = request.args.get('writers')
    year = request.args.get('year')
    if writer == 'Hemingway' and year == '1940':
        return 'Информация о книгах Хемингуэя в 1940 году'
    else:
        return redirect(f'/writers/{writer}')


if __name__ == '__main__':
    app.run(debug=True)

