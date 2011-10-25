import urllib, urllib2, base64, json
from urlparse import urlparse, urlunparse

class Stripe(object):
    """API for Stripe Payment."""
    
    api_url = "https://api.stripe.com"
    api_version = "v1"

    def __init__(self, api_key, password = ""):
        self.api_key = api_key
        self.password = password

    def _getRequest(self, action, data=None):
        request = urllib2.Request(self._createApiUrl(action, data))
        return self._sendRequest(request)

    def _postRequest(self, action, data):
        request = urllib2.Request(self._createApiUrl(action))
        self._formatData(data)
        request.add_data(urllib.urlencode(data))
        return self._sendRequest(request)

    def _formatData(self, data):
        formatters = {
            'dict': self._formatInnerDict,
        }

        for key in data.keys():
            try:
                formatters.get(data[key].__class__.__name__)(data, key)
            except TypeError:
                continue
        print data

    def _formatInnerDict(self, data, key):
        for k, v in data[key].iteritems():
            data["{}[{}]".format(key, k)] = v
        data.pop(key)

    def _createApiUrl(self, action, data = None):
        url = urlparse(self.api_url)
        api_path = "{}/{}/{}".format(url.path, self.api_version, action)
        
        api_query = ""
        if data is not None:
            api_query = urllib.urlencode(data)

        api_url = urlunparse((
            url.scheme, 
            url.netloc, 
            api_path, 
            url.params,
            api_query, 
            url.fragment, 
        ))
        return api_url

    def _sendRequest(self, request):
        opener = urllib2.build_opener()
        opener.addheaders = [
            ("Content-type", "application/x-www-form-urlencoded"),
            ("Accept", "text/plain"),
            ("Authorization", "Basic {}".format(self._createAuthHeader())),
        ]
        
        try:
            response = opener.open(request, timeout=3)
            return json.loads(response.read())
        except urllib2.URLError, e:
            error = json.loads(e.read())["error"]
            print "Failed to load {} - {}:{}".format(request.get_full_url(), error["type"], error["message"])
            return None


    def _createAuthHeader(self):
        return base64.urlsafe_b64encode("{}:{}".format(self.api_key, self.password))

