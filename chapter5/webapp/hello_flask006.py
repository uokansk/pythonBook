from flask import Flask, render_template, request
from markupsafe import escape
from vsearchForWeb import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        # print(req.form, file=log, end='|')
        # print(req.remote_addr, file=log, end='|')
        # print(req.user_agent, file=log, end='|')
        # print(res, file=log)
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    # view_the_log()
    return render_template('results.html',
                           the_phrase=phrase,
                           the_title=title,
                           the_results=results,
                           the_letters=letters, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    # contents = log.readlines()
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run(debug=True)
