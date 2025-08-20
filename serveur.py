from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):#SimpleHandler hérite de BaseHTTPRequestHandler
    def do_GET(self):
      if(self.path == "/"):
        self.send_response(200)  # self correspond a l'objet courant, une instance de SimpleHandler générée directement des qu'une requete est envoyée (post ou get). Cette instance comporte les infos de la requete et va pouvoir executer la méthode correspondante et renvoyer ce qui est demandé
        self.send_header('Content-type', 'text/html')  
        self.end_headers()  # fin des headers
        self.wfile.write(b"Bienvenue a la page d'accueil !")  # corps de la réponse
        print("home")
      elif(self.path == "/about"):
        self.send_response(200)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers() 
        self.wfile.write(b"Bienvenue a la page d'a propos !")
        print("about")
      elif(self.path == "/contact"):
        self.send_response(200)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers() 
        self.wfile.write(b"Bienvenue a la page de contact !")
        print("contact")
      else:
        self.send_response(404)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers() 
        self.wfile.write(b"Erreur, la page que vous recherchez n'existe pas !")
        print("error")

        

# 2️⃣ Créer et lancer le serveur
host = 'localhost'
port = 8000
server = HTTPServer((host, port), SimpleHandler)
print(f"Serveur en écoute sur http://{host}:{port}/")
server.serve_forever() # garde le serveur actif