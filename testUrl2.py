#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'application/octet-stream'
        self.response.out.write(self.request.body)

    def put(self):
        return self.post();

    def delete(self):
        self.response.out.write("Hello world");

    def options(self):
        self.delete()

    def trace(self):
        self.delete()

    def connect(self):
        self.delete()

application = webapp.WSGIApplication(
                                     [('/testUrl2', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
