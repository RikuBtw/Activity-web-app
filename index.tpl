<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="./style.css">
   <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
   <link href="https://fonts.googleapis.com/css?family=Lobster" rel="stylesheet">
    <script>
      function initMap() {

        var ville = {lat: 47.237225, lng: -1.25};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 9,
          center: ville
        });

        google.maps.event.addListener(map, 'click', function(event) {
           placeMarker(event.latLng);
        });

        var markers ={{!markers}};
        var infowindow = new google.maps.InfoWindow(), marker, i;
        for (i = 0; i < markers.length; i++) {
            marker = new google.maps.Marker({
            position: new google.maps.LatLng(markers[i][0][0], markers[i][0][1]),
            title: markers[i][0],
            map: map
        });

        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent("<b>"+markers[i][1][0]+"</b>" + "<br/><br/>" + markers[i][1][1] + "<br/>" + markers[i][2][0] + " " + markers[i][2][1] + "<br/>"+ markers[i][3][0]+ " "+ markers[i][3][1]+ " "+ markers[i][3][2]);
                infowindow.open(map, marker);
                map.setZoom(14);
                map.setCenter(marker.getPosition());
                var theDiv = document.getElementById("info");
                theDiv.innerHTML = "<h1>" + markers[i][1][0] + "</h1>" + "<br>\n<p>" + markers[i][1][1] + "<br>\n" + markers[i][2][0] + " " + markers[i][2][1] + "<br/>"+ markers[i][3][0]+ " "+ markers[i][3][1]+ " "+ markers[i][3][2] +"</p>" ;
            }
        })(marker, i));
      }


      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAy-LUs1hW_K0wSh38-nNVwkXUnJgPxyYU&callback=initMap">
    </script>
  </head>
  <body>
    <div class="container">
      <div class="menu">
        <div class="logo"><p>Sportifind</p></div>
        <form action="" method="post" autocomplete="off">
          <input list="browsers" name="ville" class="search" placeholder="ex: Nantes">
          <input list="browsers2" name="activite" class="search" placeholder="ex: Basket-Ball">
            <select name="niveau" class="select"  value="Non défini">
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
        <div id="info">
          <%
          if markers == []:
          %>
            <div class="no-result"></div>
            Aucun résultat
          <%
          else:
          %>
          <p>Cliquez sur un marqueur pour afficher les informations :)</p>
          %end
        </div>
      </div>
      <div id="map">
      </div>
    </div>
  </body>
</html>
