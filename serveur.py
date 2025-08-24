from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs #pour parser
import html  # pour sécuriser l’affichage et empecher les failles XSS, scripts ds les champsde formiulaires


class SimpleHandler(BaseHTTPRequestHandler):#SimpleHandler hérite de BaseHTTPRequestHandler
    def do_GET(self):
      if(self.path == "/home"):
        self.send_response(200)  # self correspond a l'objet courant, une instance de SimpleHandler générée directement des qu'une requete est envoyée (post ou get). Cette instance comporte les infos de la requete et va pouvoir executer la méthode correspondante et renvoyer ce qui est demandé
        self.send_header('Content-type', 'text/html')  
        self.end_headers()  # fin des headers
        with open("templates/home.html", "rb") as f:
          self.wfile.write(f.read())
       
      elif(self.path == "/about"):
        self.send_response(200)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers() 
        with open("templates/about.html", "rb") as f:
          self.wfile.write(f.read())
       
      elif(self.path == "/contact"):
        self.send_response(200)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers()
        with open("templates/contact.html", "rb") as f:
          self.wfile.write(f.read())
       
      else:
        self.send_response(404)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers() 
        self.wfile.write(b"Erreur, la page que vous recherchez n'existe pas !")
        
    def do_POST(self):
      if(self.path == "/envoi_contact"):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)  # ça te donne les données en bytes
        data = body.decode('utf-8')
        print("Données brutes :", data)
        parsed = parse_qs(data)# dictionnaire python
         # récupérer chaque champ
        firstname = parsed.get("fname", [""])[0]
        lastname = parsed.get("lname", [""])[0]
        message = parsed.get("message", [""])[0]
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
  

# 2️⃣ Créer et lancer le serveur
host = 'localhost'
port = 8000
server = HTTPServer((host, port), SimpleHandler)
print(f"Serveur en écoute sur http://{host}:{port}/home")
server.serve_forever() # garde le serveur actif