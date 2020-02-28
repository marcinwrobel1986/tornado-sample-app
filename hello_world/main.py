import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write("Hello, world")

class HealthCheck(tornado.web.RequestHandler):
    async def get(self):
        self.write("OK")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/healthcheck", HealthCheck),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()