from burp import IBurpExtender
from burp import IHttpListener


class BurpExtender(IBurpExtender, IHttpListener):

    # Implementation of the mandatory "registerExtenderCallbacks" interface.
    # Reference: https://portswigger.net/burp/extender/api/burp/IBurpExtender.html
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Custom header")
        callbacks.registerHttpListener(self)
        return

    # Calculate the custom HTTP header
    # TODO: modify this function to match the web application you are testing. Tip: look at the Javascript code to
    # identify how the custom header value is being calculated.
    def calc_header(self, http_request):
        hr_length = len(http_request)
        # TODO: change the value of 'header_value' to fit the variable type (e.g. int, string) you need for doing the
        # calculation
        header_value = 0

        # TODO: add code to calculate the custom header value, and return that value

        return header_value

    # "The listener will be notified of requests and responses made by any Burp tool. Extensions can perform custom
    # analysis or modification of these messages by registering an HTTP listener."
    # Source: https://portswigger.net/burp/extender/api/burp/IHttpListener.html
    # TODO: modify this function to match the web application you are testing
    def processHttpMessage(self, toolFlag, messageIsRequest, currentRequest):
        # Only process HTTP request messages, otherwise do nothing
        if not messageIsRequest:
            return

        # "request_info" will contain data such as the URL and HTTP headers.
        # For more info see: https://portswigger.net/burp/extender/api/burp/IRequestInfo.html
        request_info = self._helpers.analyzeRequest(currentRequest)

        # Depending on the application you are testing you may only have to add the custom header for specific URLs
        # TODO: customize or remove the URL check
        url = str(request_info.getUrl())
        if url.endswith('info.json') or url.endswith('info.xml'):
            # Transform from a Java ArrayList to a Python list
            headers = list(request_info.getHeaders())
            header_pos = 0
            for h in headers:
                # TODO: replace 'HEADER_NAME' (3 times) with the actual name of the header for which you want to
                # re-calculate its value
                if 'HEADER_NAME' in h:
                    new_headers = headers

                    # Get the content of the body from the HTTP request
                    # TODO: depending on how the value for the custom header is being calculated, you may have to
                    # involve other and/or additional data from the HTTP request.
                    body_bytes = currentRequest.getRequest()[request_info.getBodyOffset():]
                    body_string = self._helpers.bytesToString(body_bytes)

                    # Get the new value for the customer header 'HEADER_NAME'
                    new_header_value = self.calc_header(body_string)

                    # Replace the original header value with the new value
                    # TODO: converting the variable 'new_header_value' to a string, may not be necessary depending
                    # on the application you are testing
                    new_headers[header_pos] = 'HEADER_NAME: ' + str(new_header_value)

                    # Return the modified HTTP request when the header value has actually been changed,
                    # otherwise do nothing.
                    # TODO: make sure 'new_header_value' and 'old_header_value' are the same type
                    # In this example we are typecasting 'old_header_value' to an int.
                    old_header_value = int(h.replace('HEADER_NAME: ', ''))
                    if new_header_value != old_header_value:
                        new_message = self._helpers.buildHttpMessage(new_headers, body_string)
                        # print can be used for debugging
                        #print "Sending modified HTTP request"
                        currentRequest.setRequest(new_message)
                    return

                header_pos += 1
        else:
            return
