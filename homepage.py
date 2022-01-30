from bottle import route, run, template, error, post, request, get

@route('/')
def index():
    return template('index')

@error(404)
def error404(error):
    return '404 Nothing here, sorry'

@route('/CV')
def CV():
	return template('CV')

@route('/projectindex')
def projectindex():
	return template('projectindex')


@route('/project_network')
def projectindex():
	return template('project_network')

@route('/project_IP')
def projectindex():
	return template('project_IP')


run(host='localhost', port=8080, debug=True)
