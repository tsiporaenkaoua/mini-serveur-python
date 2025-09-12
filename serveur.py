import os
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs #pour parser
import html  # pour sécuriser l’affichage et empecher les failles XSS, scripts ds les champsde formiulaires


class SimpleHandler(BaseHTTPRequestHandler):#SimpleHandler hérite de BaseHTTPRequestHandler
    def do_GET(self):
      if(self.path == "/home"):
        self.render_html("templates/home.html")
       
      elif(self.path == "/about"):
        self.render_html("templates/about.html")
       
      elif(self.path == "/contact"):
        self.render_html("templates/contact.html")

      elif self.path.startswith("/static/"):  # gestion des fichiers statiques
          filepath = self.path.lstrip("/")  # enlève le premier "/"
          if os.path.exists(filepath):  # si le fichier existe sur le disque
              self.send_response(200)
              mime_type, _ = mimetypes.guess_type(filepath)  # devine le type selon son extension.
              if mime_type:
                  self.send_header("Content-type", mime_type) #Cela  permet au nav de savoir comment interpréter le fichier
              else:
                  self.send_header("Content-type", "application/octet-stream")
              self.end_headers()
              with open(filepath, "rb") as f: # corps de la réponse http
                  self.wfile.write(f.read())
      else:
          self.render_html("templates/erreur404.html", response=404)
        
    def do_POST(self):
      if(self.path == "/envoi_contact"):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)  # ça te donne les données en bytes
        data = body.decode('utf-8')
        print("Données brutes :", data)
        parsed = parse_qs(data)# dictionnaire python
         # récupérer chaque champ
        firstname = parsed.get("fname", [""])[0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # Lire le HTML comme texte
        with open("templates/envoi_contact.html", "r", encoding="utf-8") as f:
          html_template = f.read()
        # Remplacer le placeholder par la valeur sécurisée
        safe_firstname = html.escape(firstname)
        html_response = html_template.replace("{{firstname}}", safe_firstname)
        # Envoyer au navigateur
        self.wfile.write(html_response.encode("utf-8"))
      else:
         self.render_html("templates/erreur404.html", response=404)  


    def render_html(self, filename, response=200):
        self.send_response(response)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers() 
        with open(filename, "rb") as f:
          self.wfile.write(f.read()) 
      


# 2️⃣ Créer et lancer le serveur
host = 'localhost'
port = 8000
server = HTTPServer((host, port), SimpleHandler)
print(f"Serveur en écoute sur http://{host}:{port}/home")
server.serve_forever() # garde le serveur actif

