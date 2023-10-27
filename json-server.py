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

        if url["requested_resource"] == "metals":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)
        if url["requested_resource"] == "styles":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)
        if url["requested_resource"] == "sizes":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)

        else: 
            return self.response("Try again", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_POST(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)
      
        if url["requested_resource"] == "metals":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)
        if url["requested_resource"] == "styles":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)
        if url["requested_resource"] == "sizes":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)
  
        else: 
            url["requested_resource"] == "orders"
            return self.response("Try again", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_DELETE(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        if url["requested_resource"] == "metals":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)
        if url["requested_resource"] == "styles":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)
        if url["requested_resource"] == "sizes":
            return self.response("No changes allowed for this item", status.HTTP_405_UNSUPPORTED_METHOD.value)
        
        else: 
            url["requested_resource"] == "orders"
            return self.response("Try again", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

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