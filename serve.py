from CTFd import create_app, socketio

app = create_app()
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, resources={r'api/v1/challenges/attempt': {"origins": "*"}})
# app.run(debug=True, threaded=True, host="127.0.0.1", port=4000)

socketio.run(app, debug=True, host="127.0.0.1", port=4000)
