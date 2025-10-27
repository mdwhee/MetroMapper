from metro_mapper.elements import create_map, line

mapdata={
    'background': {
        'width': 800,
        'height': 800,
        'color': '#000000',
        'major': 100,
        'minor': 10
    },
    'testline':{
        'color':'#FF0000',
        'width':4,
        'points':[
            (100,100,10),
            (200,100,10),
            (200,200,10),
            (300,200,10)
        ]
    }
}

drawing=create_map(mapdata, 'outputs/SanFrancisco_map.svg', grid=True)
line(mapdata['testline'], drawing)
drawing.save()