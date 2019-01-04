import tornado.web
import tornado.wsgi
import tornado.ioloop
import tornado.options
import tornado.httpserver
import sys
import os
import os.path
from router import urls



if __name__ == '__main__':

    setting = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        cookie_secret="FAasfADGDkpgOYI420WRI0DUGUDSGOJWGJpojPOJposjd",
        login_url="/login",
        autoescape=None,
        debug=True,
        appversion="1.0.0")
    
    webApp = tornado.web.Application(urls, **setting)
    application = tornado.wsgi.WSGIAdapter(webApp)
    webApp.listen(80, '*')
    tornado.ioloop.IOLoop.instance().start()
