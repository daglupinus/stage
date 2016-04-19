<script language="javascript" type="text/javascript">
<!-- 
//Browser Support Code
function ajaxFunction(){

  //alert("Jestem w funkcji");

   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }

   
   // Create a function that will receive data
   // sent from the server and will update
   // div section in the same page.
   //ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxDisplay = document.getElementById('ajaxDiv');
         //ajaxDisplay.innerHTML = ajaxRequest.responseText;
      }
   } 
   // Now get the value from user and pass it to
   // server script.
   var nom = document.getElementById('nom').value;
   var type = document.getElementById('type').value;
   var latitude = document.getElementById('latitude').value;
   var longitude = document.getElementById('longitude').value;
   var tarif = document.getElementById('tarif').value;
   var date_recensement = document.getElementById('date_recensement').value;
   var photo = document.getElementById('photo').value;
   var prenom_participant = document.getElementById('prenom_participant').value;
   var commentaire = document.getElementById('commentaire').value;

   var queryString = "send=1&type=" + type + "&latitude=" + latitude +"&longitude=" + longitude + "&tarif=" + tarif + "&date_recensement="
    + date_recensement +"&photo=" + photo + "&prenom_participant=" + prenom_participant +"&commentaire=" + commentaire;
   
   //alert(queryString);

   ajaxRequest.onreadystatechange = function() {
      if(ajaxRequest.readyState == 4 && ajaxRequest.status == 200) {
        var return_data = ajaxRequest.responseText;
      document.getElementById("status").innerHTML = "Gotowe!!!";
      }
    }
    // Send the data to PHP now... and wait for response to update the status div
  
   ajaxRequest.open("POST", "add.php", true);
   ajaxRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");




   ajaxRequest.send(queryString);
   document.getElementById("status").innerHTML = "Dodaje...";



   var elements = document.getElementsByTagName("input");
   var textarea = document.getElementsByTagName("textarea");
   textarea[0].value="";


  for (var ii=0; ii < elements.length; ii++) {
  if (elements[ii].type == "text" || elements[ii].type == "date") {
     elements[ii].value = "";
  }
}

 }
//-->
</script>

<?php


if(@$_POST['send'] == 1)
{
  

    include ('php/bdd.php');

    $nom = $_POST['nom'];
    $type = $_POST['type'];
    $latitude = $_POST['latitude'];
    $longitude  = $_POST['longitude'];
    $tarif = $_POST['tarif'];
    $date_recensement = $_POST['date_recensement'];
    $photo = $_POST['photo'];
    $prenom_participant = $_POST['prenom_participant'];
    $commentaire = $_POST['commentaire'];

    $maBd = connexionbd();
    $maRequeteObtenir = "INSERT INTO lieux
     (nom,type,latitude,longitude,tarif,date_recensement,photo,prenom_participant,commentaire)
    VALUES('$nom', '$type', '$latitude', '$longitude', 
      '$tarif', '$date_recensement', '$photo', '$prenom_participant', '$commentaire' )";
    $monResultat = requete($maBd, $maRequeteObtenir);

  
    if($monResultat == NULL)
    {
      echo "dane dodane";
    }else{
      echo "nie dodalem!!";
      mysql_error();
    }   

}

/*
  <form method="POST" action="add.php">
                 <input type="submit"  class="btn btn-default" value="Submit"/>


*/
?>

            <form  class="col-md-5 col-md-offset-3" id="form">
              <h1>Ajout d'un lieu d'interet </h1>
              <div class="form-group">
                <label>nom</label>
                <input type="text" class="form-control" id="nom" name="nom" placeholder="nom">
              </div>
              <div class="form-group">
                <label>type</label>
                <input type="text" class="form-control" id="type" name="type" placeholder="nom">
              </div>
              <div class="form-group">
                <label>latitude</label>
                <input type="text" class="form-control" id="latitude" name="latitude" placeholder="latitude">
              </div>
              <div class="form-group">
                <label>longitude</label>
                <input type="text" class="form-control" id="longitude" name="longitude" placeholder="longitude">
              </div>
              <div class="form-group">
                <label>tarif</label>
                <input type="text" class="form-control" id="tarif" name="tarif" placeholder="tarif">
              </div>
              <div class="form-group">
                <label>date_recensement</label>
                <input type="date" class="form-control" id="date_recensement" name="date_recensement" placeholder="date_recensement">
              </div>
              <div class="form-group">
                <label>photo</label>
                <input type="text" class="form-control" id="photo" name="photo" placeholder="photo">
              </div>
              <div class="form-group">
                <label>prenom_participant</label>
                <input type="text" class="form-control" id="prenom_participant" name="prenom_participant" placeholder="prenom_participant">
              </div>
              <input type="hidden" name="send" value="1">
              <div class="form-group">
                <label>commentaire</label>
                <textarea class="form-control" id="commentaire" name="commentaire" rows="4"></textarea>
              </div>
              <div id="status"></div>
              <input type="button" onclick="ajaxFunction()" class="btn btn-default" value="Submit"/>
            </form>

      
