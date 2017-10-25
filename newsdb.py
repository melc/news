# Populate the news feed data
import psycopg2

# Initialize database name: news"
DBNAME = "news"


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect(database=DBNAME)


def popular_articles():
    """Return top three popular articles all time"""
    db = connect()
    c = db.cursor()
    ret_val = ''

    sqlstat = """
              SELECT title, count(log.path) AS cnt FROM articles
              LEFT JOIN log ON articles.slug = SUBSTRING(log.path, 10)
              AND log.path LIKE '/article%' GROUP BY articles.title
              ORDER BY cnt DESC LIMIT 3; """

    try:
        c.execute(sqlstat)
        ret_val = c.fetchall()

    except psycopg2.Error as e:
        print(e)
    finally:
        db.close()

    return ret_val


def popular_authors():
    """Return top three popular authors all time"""
    db = connect()
    c = db.cursor()
    ret_val = ''

    sqlstat = """
                SELECT name, sum(popular_articles.cnt) AS sum_cnt FROM
                (
                    SELECT title, count(log.path) AS cnt FROM articles
                    LEFT JOIN log ON articles.slug = SUBSTRING(log.path, 10)
                    AND log.path LIKE '/article%' GROUP BY articles.title
                    ORDER BY cnt DESC) AS popular_articles, articles, authors
                    WHERE popular_articles.title = articles.title AND
                    articles.author = authors.id GROUP BY name
                    ORDER BY sum_cnt DESC LIMIT 3; """

    try:
        c.execute(sqlstat)
        ret_val = c.fetchall()
    except psycopg2.Error as e:
        print(e)
    finally:
        db.close()

    return ret_val


def get_http_error():
    """Return percentage of HTTP error each day. HTTP error refers to
    those records which status is not 200 OK"""
    db = connect()
    c = db.cursor()
    http_error = ''

    sqlstat = """
              SELECT to_char(err_day,'Month DD, YYYY'),
              trunc((err_cnt::NUMERIC / cnt * 100), 2) AS error FROM
              (
                SELECT time::DATE AS err_day, count(time::DATE) AS err_cnt
                FROM log WHERE status != '200 OK' GROUP BY time::DATE
                ORDER BY time::DATE) AS http_err,
                (
                  SELECT time::DATE AS day, count(time :: DATE) AS cnt FROM log
                  GROUP BY time::DATE ORDER BY time::DATE ) AS http
                  WHERE err_day = day AND
                  trunc((err_cnt::NUMERIC / cnt * 100), 2) > 1;"""

    try:
        c.execute(sqlstat)
        http_error = c.fetchall()
    except psycopg2.Error as e:
        print(e)
    finally:
        db.close()

    return http_error
