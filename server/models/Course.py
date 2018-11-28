from server.models.Base import Base
from server import conn, server, jwt, bcrypt
import psycopg2.extras


class Course(Base):
    def all(self):
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM courses ORDER BY name ASC")
        courses = cur.fetchall()
        cur.close()
        return courses
