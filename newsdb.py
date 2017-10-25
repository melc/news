# Execute query of the news feed data
import psycopg2

# Initialize database news
DBNAME = "news"


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect(database=DBNAME)


def execute_query(query):
    """Execute query"""
    db = connect()
    c = db.cursor()
    ret_val = ''

    try:
        c.execute(query)
        ret_val = c.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        db.close()

    return ret_val


def popular_articles():
    """Return top three popular articles all time"""

    sqlstat = """
                SELECT title, views
                FROM articles
                INNER JOIN
                  (SELECT path, count(path) AS views
                    FROM log
                    GROUP BY log.path) AS log
                ON log.path = '/article/' || articles.slug
                ORDER BY views DESC LIMIT 3; """

    return execute_query(sqlstat)


def popular_authors():
    """Return popular authors all time"""

    sqlstat = """
                SELECT name, sum(popular_articles.views) AS sum_cnt FROM
                (
                  SELECT title, views
                  FROM articles
                  INNER JOIN
                  (
                    SELECT path, count(path) AS views
                    FROM log
                    GROUP BY log.path) AS log
                  ON log.path = '/article/' || articles.slug)
                  AS popular_articles, articles, authors
                  WHERE popular_articles.title = articles.title AND
                  articles.author = authors.id GROUP BY name
                  ORDER BY sum_cnt DESC;"""

    return execute_query(sqlstat)


def get_http_error():
    """Return percentage of HTTP error each day. HTTP error refers to
    those records which status is not 200 OK"""

    sqlstat = """
              SELECT to_char(err_day,'Month DD, YYYY'),
              round((err_cnt::NUMERIC / cnt * 100), 2) AS error FROM
              (
                SELECT time::DATE AS err_day, count(time::DATE) AS err_cnt
                FROM log
                WHERE status != '200 OK' GROUP BY time::DATE) AS http_err,
              (
                SELECT time::DATE AS day, count(time::DATE) AS cnt
                FROM log GROUP BY time::DATE) AS http
              WHERE err_day = day AND
              err_cnt::NUMERIC / cnt * 100 > 1;"""

    return execute_query(sqlstat)
