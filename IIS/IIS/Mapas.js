function initialize() {
    var marcadores = [
      ['Tecnologico Regional', 22.774062, -102.626439],
      ['Hospital General', 22.778394, -102.618986],
      ['Unidad Deportica Norte', 22.774466, -102.612903],
      ['Campus UAZ S.XXI', 22.769944, -102.642213],
      ['Presidencia Municipal', 22.774516, -102.587283],
      ['Hospital ISSSTE', 22.765068, -102.577090],
      ['Plaza Bicentenario', 22.769530, -102.571908],
      ['Parada de autobus de Ingenieria', 22.767973, -102.566801],
      ['Parada de autobus de Minas', 22.764476, -102.557477],
      ['Parada de autobus de la Feria', 22.763160, -102.550326],
      ['Parada de autobus Soriana', 22.762394, -102.548165],
      ['Unidad de Odontologia', 22.753407, -102.525469]
    ];
    var map = new google.maps.Map(document.getElementById('mapa'), {
      zoom: 14,
      center: new google.maps.LatLng(22.769530, -102.571908),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    var infowindow = new google.maps.InfoWindow();
    var marker, i;
    for (i = 0; i < marcadores.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
        map: map
      });
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(marcadores[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }
  }
  google.maps.event.addDomListener(window, 'load', initialize);