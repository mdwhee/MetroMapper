from metro_mapper.elements import create_map, line

gap=10

styledata={
    'background_color':'#000000',
    'grid_color':'#444444',
    'gap': gap,
}

mapdata={
    'background': {
        'width': 800,
        'height': 800,
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
            (300,200,10),
            (300,100,10)
        ],
        'stops':[
            (150,100),
            (200,150),
            (300,170)
        ]
    },
    'testline2':{
        'color':'#00FF00',
        'width':4,
        'points':[
            (100,100-gap,10),
            (200+gap,100-gap,10+gap),
            (200+gap,170,10),
            (400,170,10)
        ],
        'stops':[
            (150,100-gap),
            (200+gap,150),
            (300+gap,170)
        ]
    },
}

drawing=create_map(mapdata, styledata, 'outputs/SanFrancisco_map.svg', grid=True)
linegroup=drawing.g(id='lines')
stopgroup=drawing.g(id='stops')
line(mapdata['testline'], styledata, linegroup, stopgroup)
line(mapdata['testline2'], styledata, linegroup, stopgroup)
drawing.add(linegroup)
drawing.add(stopgroup)
drawing.save()