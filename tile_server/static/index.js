alert('hi');
var map = new ol.Map({
    target: 'map',
    layers: [

        new ol.layer.Tile({
            source: new ol.source.OSM(),
        }),
        // new ol.layer.Tile({
        //     source: new ol.source.XYZ({
        //         url: 'http://localhost:8000/myview/xyz/1.0.0/mrsk_communication_line/{z}/{x}/{y}.png',
        //         projection: 'EPSG:4326'
        //     }),
        //     extent: ol.proj.transformExtent([38.18, 44.65, 50, 51.28], 'EPSG:4326', 'EPSG:3857'),
        // }),
        // new ol.layer.Tile({
        //     source: new ol.source.XYZ({
        //         url: 'http://localhost:8000/myview/xyz/1.0.0/mrsk_accident_avar/{z}/{x}/{y}.png',
        //         projection: 'EPSG:4326'
        //     }),
        //     extent: ol.proj.transformExtent([38.18, 44.65, 50, 51.28], 'EPSG:4326', 'EPSG:3857'),
        // }),

        new ol.layer.Tile({
            source: new ol.source.XYZ({
                url: 'http://localhost:8000/myview/xyz/1.0.0/mrsk_area_energy/{z}/{x}/{y}.png',
                projection: 'EPSG:4326'
            }),
            extent: ol.proj.transformExtent([38.18, 44.65, 50, 51.28], 'EPSG:4326', 'EPSG:3857'),
        }),

    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([37.41, 44.82]),
        zoom: 5
    })
});