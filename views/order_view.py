import json
import sqlite3
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class OrdersView():
    def get(self, handler, pk):
        
        if pk != 0:
            sql = "SELECT o.id, o.metal_id, o.style_id, o.size_id FROM Orders o WHERE o.id = ?"
            query_results = db_get_single(sql, pk)
            serialized_orders = json.dumps(dict(query_results))

            return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)
        else:
            sql = "SELECT o.id, o.metal_id, o.style_id, o.size_id FROM Orders o"
            query_results = db_get_all(sql)
            metals = [dict(row) for row in query_results]
            all_orders = json.dumps(metals)

            return handler.response(all_orders, status.HTTP_200_SUCCESS.value)
        
    def add_order(self, handler, order_data):
    # Adjust the SQL query to insert data into the 'Orders' table
        sql = """
    INSERT INTO Orders (metal_id, style_id, size_id) VALUES (?, ?, ?)
    """
    # Assuming dock_data contains metal_id, style_id, and size_id

    # Execute the SQL query to create an order
        number_of_rows_created = db_create(
        sql,
        (order_data['metal_id'], order_data['style_id'], order_data['size_id'])
    )

    # Assuming the response_sql is intended to fetch details of the created orders
        response_sql = "SELECT id, metal_id, style_id, size_id FROM Orders"
        query_results = db_get_all(response_sql)
        row_orders = [dict(row) for row in query_results]
        response_orders = json.dumps(row_orders)

    # Adjust the response based on the number of rows affected by the SQL execution
        if number_of_rows_created > 0:
            return handler.response(response_orders, status.HTTP_201_SUCCESS_CREATED.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def delete_order(self, handler, pk):
        row_deleted = db_delete("DELETE FROM Orders WHERE id = ?", pk)

        if row_deleted > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
