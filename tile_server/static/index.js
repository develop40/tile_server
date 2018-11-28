alert('hi');
 var map = new ol.Map({
    target: 'map',
    layers: [

      new ol.layer.Tile({
        source: new ol.source.OSM({
        })
      }),
      new ol.layer.Tile({
        source: new ol.source.XYZ({
            url: 'http://localhost:8000/myview/xyz/1.0.0/land/{z}/{x}/{y}.png',
            projection: 'EPSG:4326'
        })
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([37.41, 44.82]),
      zoom: 1
    })
  });