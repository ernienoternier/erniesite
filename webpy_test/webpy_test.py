import web

urls = (
'/todos', 'todo',
'/storywall', 'storywall',
'/todos/add', 'todoadd'
)

db = web.database(dbn='mysql', user='root', pw='888888', db='webpy_test')

render = web.template.render('templates/')

class index:
	def GET(self, name):
		return render.index(name)
class todo:
	def GET(self):
		todos = db.select('todo')
		return render.todo(todos)
class storywall:
	def GET(self):
		stories = db.select('story', limit = "3, 6")
		print dir(stories)
		return render.story(stories)
class todoadd:
	def POST(self):
		i = web.input()
		n = db.insert('todo', title=i.title)
		raise web.seeother('/todos')


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
