#!/usr/bin/python3.5
from flask import Flask, render_template
from newsdb import popular_articles, popular_authors, get_http_error

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    # Main page of the news reporting tool. #
    p_articles = []
    articles_str = 'What are the most popular three articles of all time?\n'
    for title, count in popular_articles():
        # retrieve three top popular articles #
        p_articles.append([title, count])
        articles_str += title + ' -- ' + str(count) + " views\n"

    p_authors = []
    authors_str = '\n\nWho are the most popular article authors of all time?\n'
    for name, count in popular_authors():
        # retrieve three top popular authors #
        p_authors.append([name, count])
        authors_str += name + ' -- ' + str(count) + " views\n"

    http_errors = []
    http_errors_str = '\n\nOn which days did more than 1% of requests lead to errors?\n'
    for day, error in get_http_error():
        # return percentage of HTTP error each day. #
        # HTTP error refers to those records which status is 200 OK #
        http_errors.append([day, error])
        http_errors_str += ' '.join(day.split()) + ' -- ' + str(error) + "% errors\n"

    f = open('news.txt', 'w')

    f.write(articles_str + authors_str + http_errors_str)
    f.close()

    return render_template('index.html', articles=p_articles,
                           authors=p_authors,
                           http_errors=http_errors)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8000)


