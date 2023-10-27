import json
import sqlite3
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class StylesView():
    def get(self, handler, pk):
        
        if pk != 0:
            sql = "SELECT sty.id, sty.style, sty.price FROM Styles sty WHERE sty.id = ?"
            query_results = db_get_single(sql, pk)
            serialized_style = json.dumps(dict(query_results))

            return handler.response(serialized_style, status.HTTP_200_SUCCESS.value)
        else:
            sql = "SELECT sty.id, sty.style, sty.price FROM Styles sty"
            query_results = db_get_all(sql)
            metals = [dict(row) for row in query_results]
            serialized_styles = json.dumps(metals)

            return handler.response(serialized_styles, status.HTTP_200_SUCCESS.value)