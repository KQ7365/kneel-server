import json
import sqlite3
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class SizesView():
    def get(self, handler, pk):
        
        if pk != 0:
            sql = "SELECT siz.id, siz.caret, siz.price FROM Sizes siz WHERE siz.id = ?"
            query_results = db_get_single(sql, pk)
            serialized_size = json.dumps(dict(query_results))

            return handler.response(serialized_size, status.HTTP_200_SUCCESS.value)
        else:
            sql = "SELECT siz.id, siz.caret, siz.price FROM Sizes siz"
            query_results = db_get_all(sql)
            metals = [dict(row) for row in query_results]
            serialized_sizes = json.dumps(metals)

            return handler.response(serialized_sizes, status.HTTP_200_SUCCESS.value)