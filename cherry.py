import cherrypy

class FirstPage(object):
    def HandleData(self, data=None):
        return data

    def index(self):
        return('''<form action="HandleData" method=post>
        <input type="text" name="data">
        <input type="submit" value="submit">''')

    index.exposed = True
    HandleData.exposed = True

cherrypy.quickstart(FirstPage())