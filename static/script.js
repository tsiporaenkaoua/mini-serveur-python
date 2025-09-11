
// couleur de ciblage lorsqu'on est dans un champs particulier - focus
//verif les commentaires en bas de page


let firstname = document.getElementById("fname");
let lastname = document.getElementById("lname");
let email = document.getElementById("email");
let tel = document.getElementById("tel");
let message = document.getElementById("message");
let form = document.querySelector("form");

console.log("✅ script.js chargé !");

//remplissage de chaque champs et erreur si pas de remplissage - blur
no_value(firstname, "Veuillez remplir le prénom") 
no_value(lastname, "Veuillez remplir le nom de famille") 
no_value(email, "Veuillez remplir le mail") 
no_value(tel, "Veuillez remplir le tel") 

isValidityOK(tel);
isValidityOK(email);

//affichage erreur lors du submit pas complet - submit
form.addEventListener("submit", function(event){
  if (firstname.value =="" || lastname.value ==""|| email.value =="" || tel.value ==""){
    event.preventDefault(); // empêche l'envoi du formulaire
    document.getElementById("error-submit").textContent= "Champs obligatoires à remplir avant soumission"
  }
} )
/*********************************************Finir validation du tel et email (required....)****** */
//affichage erreur si mail/tel non valide
function isValidityOK(element){
  element.addEventListener("input",function(){
   if(!element.checkValidity()){
    document.getElementById(`error-${element.id}`).textContent= "Le format nest pas valide"
   }
  })
}

//remplissage de chaque champs et erreur si pas de remplissage - blur
function no_value(element, message){
  element.addEventListener("blur",function(){
    if (element.value === ""){
    document.getElementById(`error-${element.id}`).textContent= message
    }
    else{
      document.getElementById(`error-${element.id}`).textContent=""
    }
  })
}


/*) Que fais tu si je désactive javascript juste parce que je suis un vilain petit canard malveillant?
Quoi que tu fasses coté client tu devrais prévoir la ceinture de sécurité coté serveur, surtout pour les valeurs $_POST et $_GET car n'importe qui peut les modifier :
*Primo; est-ce que ce dont tu as besoin existe (isset)
*Secundo; est ce que la valeur est sécurisée? (ça tu le fais un peu avec htmlspecialchar )
*Tercio; la valeur est-elle conforme à ton besoin? (Par exemple le mail au format mail, tu peux te faire tes propres petites fonctions, et tu repasses tout à la moulinette)*/