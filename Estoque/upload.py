from sistema import app

app.config['UPLOAD_FOLDER'] = 'static/uploads/'

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #Limite de 16 Mb para upload

ARQUIVOS_PERMITIDOS = {'png', 'jpg', 'jpeg', 'gif'}

def arquivos_permitidos(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ARQUIVOS_PERMITIDOS