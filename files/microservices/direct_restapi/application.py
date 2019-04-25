#!/usr/bin/python
# -*- coding: utf8 -*-

import logging
from flask import Flask
from flask_restful import Api
from flask_restful import Resource
import psycopg2
from psycopg2.extras import RealDictCursor


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
api = Api(app)


class Health(Resource):
    def get(self):
        return '', 204


class PgSettings(Resource):
    def get(self):
        return self.get_data_from_db("""select * from pg_settings""")

    def get_data_from_db(self, db_select):
        try:
            conn_string = "host=\'{host}\' port=\'{port}\' dbname=\'{dbname}\' user=\'{user}\' password=\'{password}\'".format(host=app.config['DIRECT_EXAM_DB_HOST'],
                                                                                                                               port=app.config['DIRECT_EXAM_DB_PORT'],
                                                                                                                               dbname=app.config['DIRECT_EXAM_DB_NAME'],
                                                                                                                               user=app.config['DIRECT_EXAM_DB_USER'],
                                                                                                                               password=app.config['DIRECT_EXAM_DB_PASSWORD'])
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor(cursor_factory=RealDictCursor)

        except Exception as e:
            print("I am unable to connect to the database due to the following\n -> {}".format(e))

        try:
            cursor.execute(db_select)
            return cursor.fetchall()
        except Exception as e:
            print("Unable to execute the operation due to the following\n -> {}".format(e))


api.add_resource(Health, '/health')
api.add_resource(PgSettings, '/pg-settings')


if __name__ == '__main__':
    app.run(host=app.config['DIRECT_EXAM_APP_INTERFACE'], port=app.config['DIRECT_EXAM_APP_PORT'], debug=True, threaded=True)
