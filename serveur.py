from http.server import HTTPServer, BaseHTTPRequestHandler

host = 'localhost'
port = 8000


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # code HTTP 200 = OK
        self.send_header('Content-type', 'text/html')  # type de contenu
        self.end_headers()  # fin des headers
        self.wfile.write(b"Hello, World !")  # corps de la réponse
        

# 2️⃣ Créer et lancer le serveur
server = HTTPServer((host, port), SimpleHandler)
print(f"Serveur en écoute sur http://{host}:{port}/")
server.serve_forever() # garde le serveur actif