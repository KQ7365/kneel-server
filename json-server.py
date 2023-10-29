import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import MetalsView, SizesView, StylesView, OrdersView


class JSONServer(HandleRequests):

    def do_GET(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        try:
            view.get(self, url["pk"])
        except AttributeError:
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_PUT(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        disallowed_methods = {
        "metals": "No changes allowed for this item",
        "styles": "No changes allowed for this item",
        "sizes": "No changes allowed for this item"
        }

        requested_resource = url["requested_resource"]

        if requested_resource in disallowed_methods:
            return self.response(disallowed_methods[requested_resource], status.HTTP_405_UNSUPPORTED_METHOD.value)

        else: 
            return self.response("Try again", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_POST(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        disallowed_methods = {
        "metals": "No additions allowed for this item",
        "styles": "No additions allowed for this item",
        "sizes": "No additions allowed for this item"
        }

        requested_resource = url["requested_resource"]

        if requested_resource in disallowed_methods:
            return self.response(disallowed_methods[requested_resource], status.HTTP_405_UNSUPPORTED_METHOD.value)

        try:
            view.add_order(self, self.get_request_body())
        except AttributeError:
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)


    def do_DELETE(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        disallowed_methods = {
        "metals": "No deletions allowed for this item",
        "styles": "No deletions allowed for this item",
        "sizes": "No deletions allowed for this item"
        }

        requested_resource = url["requested_resource"]

        if requested_resource in disallowed_methods:
            return self.response(disallowed_methods[requested_resource], status.HTTP_405_UNSUPPORTED_METHOD.value)

        try:
            view.delete_order(self, self.get_request_body())
        except AttributeError:
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

        #!May need to add else when it comes to orders or just reverse if statement to where Else becomes any other url
        # try:
        #     view.delete(self, url["pk"])
        # except AttributeError:
        #     return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)


    def determine_view(self, url):
        """Lookup the correct view class to handle the requested route

        Args:
            url (dict): The URL dictionary

        Returns:
            Any: An instance of the matching view class
        """
        try:
            routes = {
                "sizes": SizesView,
                "styles": StylesView,
                "metals": MetalsView,
                "orders": OrdersView
            }

            matching_class = routes[url["requested_resource"]]
            return matching_class()
        except KeyError:
            return status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value








#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()