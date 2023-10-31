import json
import sqlite3
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class OrdersView():
    

    def get(self, handler, pk):
        parsed_url = handler.parse_url(handler.path)
       
        if pk != 0:
            expand_params = parsed_url['query_params'].get('_expand')
        
            if expand_params:
                sql = """SELECT 
                    o.id,
                    o.metal_id,
                    o.style_id,
                    o.size_id,
                    o.timestamp,
                    m.id AS metalId,
                    m.metal,
                    m.price as metal_price,
                    s.id AS sizeId,
                    s.caret,
                    s.price as size_price,
                    st.id AS styleId,
                    st.style,
                    st.price as style_price
                    FROM Orders o
                    LEFT JOIN Metals m ON o.metal_id = m.id
                    LEFT JOIN Sizes s ON o.size_id = s.id
                    LEFT JOIN Styles st ON o.style_id = st.id
                    WHERE o.id = ?
                    """
                query_results = db_get_single(sql, pk)
                
                expanded_data = {
                    "id": query_results['id'],
                    "timestamp": query_results['timestamp'],
                    "metal_id": query_results['metal_id'],
                    "style_id": query_results['style_id'],
                    "size_id": query_results['size_id']
                }

                if 'metal' in expand_params or expand_params == 'all':
                    expanded_data["metal"] = {
                        "id": query_results['metalId'],
                        "metal": query_results['metal'],
                        "price": query_results['metal_price']
                    }
                if 'style' in expand_params or expand_params == 'all':
                    expanded_data["style"] = {
                        "id": query_results['styleId'],
                        "style": query_results['style'],
                        "price": query_results['style_price']
                    }
                if 'size' in expand_params or expand_params == 'all':
                    expanded_data["size"] = {
                        "id": query_results['sizeId'],
                        "caret": query_results['caret'],
                        "price": query_results['size_price']
                    }

                serialized_orders = json.dumps(expanded_data)

            else:
                sql = "SELECT o.id, o.metal_id, o.style_id, o.size_id, o.timestamp FROM Orders o WHERE o.id = ?"
                query_results = db_get_single(sql, pk)
                serialized_orders = json.dumps(dict(query_results))

            return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)
        else:
            sql = "SELECT o.id, o.metal_id, o.style_id, o.size_id, o.timestamp FROM Orders o"
            query_results = db_get_all(sql)
            orders = [dict(row) for row in query_results]
            all_orders = json.dumps(orders)

        return handler.response(all_orders, status.HTTP_200_SUCCESS.value)
    
        
    def add_order(self, handler, order_data):
    # Adjust the SQL query to insert data into the 'Orders' table
        sql = """
    INSERT INTO Orders (metal_id, style_id, size_id) VALUES (?, ?, ?)
    """

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
