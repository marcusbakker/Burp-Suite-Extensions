The Burp extension `custom_http_header.py` serves as a template to make sure that a custom HTTP security header, being added by the client itself, is always having the correct value when manipulating parameters in the HTTP request or doing Active scans.

Within the Python code I have added comments (`# TODO`) that should help you in customising the Python code to fit the web application you are testing.

The blog related to this extension can be found at: https://www.mbsecure.nl/blog/2018/7/bypass-client-side-generated-http-security-headers

## Installation
The Burp extension requires Jython.
1. Download the standalone Jython version 2.7.0: http://www.jython.org/downloads.html
2. Configure Burp to point to the location of Jython by going to the “Extension” tab and navigate to the “Options” sub-tab:
![Configure Jython](https://github.com/marcusbakker/Burp-Suite-Extensions/blob/master/jython.png)
3. Within the same tab (“Extensions”) go to the sub-tab “Extension” and Add the extension `custom_http_header.py`.
![Load the extension](https://github.com/marcusbakker/Burp-Suite-Extensions/blob/master/extension.png)
* If you do not get any errors while loading, everything is ok. Otherwise fix your code and reload the extension (uncheck and check).
