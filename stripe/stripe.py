import urllib, urllib2, base64, json

class Stripe(object):
    """API for Stripe Payment."""
    
    api_url = "https://api.stripe.com"
    api_version = "v1"

    def __init__(self, api_key, password = ""):
        self.api_key = api_key
        self.password = password

    def _getRequest(self, action):
        request = urllib2.Request(self._createApiUrl(action))
        return self._sendRequest(request)

    def _postRequest(self, action, data):
        request = urllib2.Request(self._createApiUrl(action), urllib.urlencode(data))
        return self._sendRequest(request)

    def _createApiUrl(self, action):
        return "{}/{}/{}".format(self.api_url, self.api_version, action)

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
            print "Failed to load {} - {}".format(apiUrl, e)
            return None


    def _createAuthHeader(self):
        return base64.urlsafe_b64encode("{}:{}".format(self.api_key, self.password))

