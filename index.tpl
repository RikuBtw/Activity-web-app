<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="./style.css">
    <script>
      function initMap() {
        var ville = {lat: {{latitude}}, lng: {{longitude}}};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 10,
          center: ville
        });
        var marker = new google.maps.Marker({
          position: ville,
          map: map
        });
      }

      function change() {
        document.getElementsByTagName('body')[0].style.height = '0px';
        document.getElementById('rectangle-up').setAttribute('id','rectangle-uped');
        document.getElementById('container-search').setAttribute('id','container-searched');

      }

    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAy-LUs1hW_K0wSh38-nNVwkXUnJgPxyYU&callback=initMap">
    </script>
  </head>

  <body>
    <form action="" method="post" autocomplete="off">
      <input list="browsers" name="search">
      <select name="recherche">
        <option value="Ville">Ville</option>
        <option value="Sport">Sport</option>
      </select>
      <datalist id="browsers">
      <%
      if villes != None:
      for c in villes:
      %>
          <option value={{c}}>
      %end
      %end
      </datalist>
      <input type="submit" value="Search">
    </form>
    <%
    if data != None :
    for i in data:
    %>
        <li>{{i}}</li>
    %end
    %end

      <div id="map">
      </div>


  </body>
</html>
