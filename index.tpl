<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="./style.css">
   <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
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
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAy-LUs1hW_K0wSh38-nNVwkXUnJgPxyYU&callback=initMap">
    </script>
  </head>
  <body>
    <div class="container">
      <div class="menu">
        <div class="logo"></div>
        <form action="" method="post" autocomplete="off">
          <input list="browsers" name="ville" class="search" placeholder="ex: Nantes">
          <input list="browsers2" name="activite" class="search" placeholder="ex: Basket-Ball">
            <select name="niveau" class="search">
              <%
              for n in niveau:
              %>
                  <option value={{n}}>{{n}}</option>
              %end
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
          <datalist id="browsers2">
          <%
          if activites != None:
          for c in activites:
          %>
              <option value={{c}}>
          %end
          %end
          </datalist>
          <input type="submit" value="Search">
          <hr>
        </form>
        <div class="info">
        </div>
      </div>
      <div id="map">
      </div>
    </div>
  </body>
</html>
