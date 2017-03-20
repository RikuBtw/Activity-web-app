<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="./style.css">
    <script>
      function initMap() {
        var ville = {lat: 47.408949, lng: -1.653876};
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
    <form action="" method="post">
       <input type="text" name="search" placeholder="Entrez la ville recherchée..." autocomplete="off" onkeypress="change()">
      <input type="submit" value="Search">

    </form>

      <div id="map">
      </div>


  </body>
</html>
