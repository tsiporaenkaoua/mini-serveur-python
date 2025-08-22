from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs #pour parser


class SimpleHandler(BaseHTTPRequestHandler):#SimpleHandler hérite de BaseHTTPRequestHandler
    def do_GET(self):
      if(self.path == "/"):
        self.send_response(200)  # self correspond a l'objet courant, une instance de SimpleHandler générée directement des qu'une requete est envoyée (post ou get). Cette instance comporte les infos de la requete et va pouvoir executer la méthode correspondante et renvoyer ce qui est demandé
        self.send_header('Content-type', 'text/html')  
        self.end_headers()  # fin des headers
        self.wfile.write(b"Bienvenue a la page d'accueil !")  # corps de la réponse
       
      elif(self.path == "/about"):
        self.send_response(200)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers() 
        self.wfile.write(b"Bienvenue a la page d'a propos !")
       
      elif(self.path == "/contact"):
        self.send_response(200)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers()
        html="""
        <h2>Formulaire de contact</h2>
        <form method = 'POST', action="/contact">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value=""><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value=""><br>
        <label for="message">Description</label><br>
        <textarea name="message"></textarea><br>
        <input type="submit" value="Submit">
        </form>
        """
        self.wfile.write(html.encode())
       
      else:
        self.send_response(404)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers() 
        self.wfile.write(b"Erreur, la page que vous recherchez n'existe pas !")
        
    def do_POST(self):
      if(self.path == "/contact"):
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
        html= f"""
        <h2>Merci {firstname}</h2>
        <h3>Votre message a bien été enregistré<br>
        <a href="/">Retourner à la page d'accueil</a>
        </h3>
        """
        self.wfile.write(html.encode())
  

# 2️⃣ Créer et lancer le serveur
host = 'localhost'
port = 8000
server = HTTPServer((host, port), SimpleHandler)
print(f"Serveur en écoute sur http://{host}:{port}/")
server.serve_forever() # garde le serveur actif