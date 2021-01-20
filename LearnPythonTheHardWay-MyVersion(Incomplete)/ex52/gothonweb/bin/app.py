import web
from gothonweb.map import *
urls = (
    '/game', 'GameEngine'
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base='layout')

class GameEngine(object):
    def GET(self):
        print session.room
        if session.room:
            return render.show_room(room=session.room)
        else:
            session.room = central_corridor
            return render.show_room(room=session.room)
            # # where is there here? do you need it?
            # shows character death
            # return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother('/game')

if __name__ == "__main__":
    app.run()
