import docker
from flask import Flask, render_template, request

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def index():
    containers = client.containers.list()
    return render_template('index.html', containers=containers)

@app.route('/stop_container', methods=['POST'])
def stop_container():
    container_id = request.form['container_id']
    try:
        container = client.containers.get(container_id)
        container.stop()
        return 'Container parado com sucesso.'
    except docker.errors.NotFound:
        return 'Container não encontrado.'

if __name__ == '__main__':
    app.run(debug=True)
