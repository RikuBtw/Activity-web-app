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
    <div id = "rectangle-up">
      <div id = "container-search">
        <form action="" method="post" autocomplete="off">
          Ville <input list="browsers" name="ville">
          Activité <input list="browsers2" name="activite">
          <select name="niveau">
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
        </form>
      </div>
    </div>
    <div class="container-info">
      <div class="info-haut">
        <%
        if data != None :
        for i in data:
        %>
            <li>{{i}}</li>
        %end
        %end

        <%
        if erreur != None :
        %>
        <p>{{erreur}}</p>
        %end
      </div>
    </div>
    <div id="map">
    </div>


  </body>
</html>
