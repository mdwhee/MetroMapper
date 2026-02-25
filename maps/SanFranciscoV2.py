from metro_mapper.elements import create_map, lines
import os

fg=20
hg=fg/2**0.5
qg=fg*(2**0.5-1)

g53=fg*5/3
g54=fg*5/4
g34=fg*3/4
g45=fg*4/5
g35=fg*3/5

mapdata={
    'style':{
        'grid':{
            'major':100,
            'minor':10,
            'color':'#444444'
        },
        'background': {
            'width':1600,
            'height':2000,
            'color':'#000000',
        },
        'fg':fg,
        'center':(1200,600),
        'gap':fg,
    },
    'lines':{},
}

bart = {
    'color':'#BBBB77',
    'width':fg/2,
    'points':[
        (1000,-210,fg),
        (280,-210,10*fg),
        (-280,210,10*fg),
        (-280,640,fg)
    ],
    'stops':[
        (180,-135),
        (100,-75),
        (0,0),
        (-80-40/3-g53+g35,70+g45),
        (-280,380),
        (-280,600)
    ]
}
m_line = {
    'color':'#00FF00',
    'width':fg/2,
    'points':[
        (150,200,fg),
        (270,110,fg),
        (270,-70+40/3,fg),
        (200-g35,-150-g45,fg),
        (-600-g53,450,fg)
    ],
    'stops':[
        (150,200),
        (230,140),
        (270,40),
        (260,-70),
        (180-g35,-135-g45),
        (100-g35,-75-g45),
        (0-g35,0-g45),
        (-80-40/3-g53,70),
        (-240,180-g54),
        (-440,330-g54),
        (-540,405-g54),
    ]
}
m_line_n_branch = {
    'color':'#00FF00',
    'width':fg/2,
    'points':[
        (180-g35,-135-g45,fg),
        (-360-g53,270,fg),
        (-1000,270,fg)
    ],
    'stops':[
        (-500,270),
    ]
}
m_line_j_branch = {
    'color':'#00FF00',
    'width':fg/2,
    'points':[
        (180-g35,-135-g45,fg),
        (-360-g53,270,fg),
        (-440,270,fg),
        (-440,1000,fg)
    ],
    'stops':[
    ]
}
j_line = {
    'color':'#FF7700',
    'width':fg/2,
    'points':[
        (-1000,270+fg,fg),
        (-440,270+fg,fg),
        (-440,450,fg)
    ],
    'stops':[
        (-500,270+fg),
        (-440,330-g54+fg),
    ]
}
f_line = {
    'color':'#FFFF00',
    'width':fg/2,
    'points':[
        (-30,-450-fg,fg),
        (-140+fg,-450-fg,fg),
        (-140,-450,fg),
        (-440+fg,-450,fg),
        (-440+fg,380,fg),
        (-90+g53,380,fg),
        (270+g35,110+g45,2*fg),
        (270+fg,110,2*fg),
        (270+fg,-70+40/3,2*fg),
        (270+g45,-70+40/3-g35,2*fg),
        (-25-g34+g54,-450-fg,fg),
        (-100,-450-fg,fg/2),
        (-100,-450,fg/2),
        (-25+g54,-450,fg),
        (-25+g54+g35,-450+g45,fg),
    ],
    'stops':[
        (-200,-410),
        (-320,-410),
        (-440+fg,-370),
        (-440+fg,-310),
        (-440+fg,-150-fg),
        (-440+fg,-60),
        (-440+fg,70),
        (-440+fg,220),
        (-440+fg,330-g54+fg),
        (-280-fg,380),
        (-90,380),
        (30+g35,290+g45),
        (150+g35-g45,200+g45+g35),
        (230+g35,140+g45),
        (270+fg,40),
        (260+g45,-70-g35),
        (200+g45-g35,-150-g45-g35),
        (110+g45,-270-g35),
        (50+g45,-350-g35),
        (-30,-450-fg),
        (-30,-450),
    ]
}
f_line_ext = {
    'color':'#FFFF00',
    'width':fg/2,
    'points':[
        (-440+fg,-480,fg),
        (-440+fg,380,fg),
        (220+hg,380,fg),
    ],
    'stops':[
        (-440+fg,-480),
        (220+hg,380)
    ]
}
c_line = {
    'color':'#FF0000',
    'width':fg/2,
    'points':[
        (220,1000,fg),
        (220,240,fg),
        (180,240,fg),
        (-30,-40,fg),
        (-30,-300,fg),
        (-50,-320,fg),
        (-50,-430+fg,fg),
        (-30,-450+fg,fg)
    ],
    'stops':[
        (220,560),
        (220,490),
        (220,420),
        (220,365-hg),
        (220,280),
        (150+g35,200+g45),
        (105,140),
        (30+g35,40+g45),
        (0-2*g35,-2*g45),
        (-30,-200+fg),
        (-40,-310),
        (-30,-450+fg),
    ]
}
c_line_ext = {
    'color':'#FF0000',
    'width':fg/2,
    'points':[
        (190-hg,-80-hg,fg),
        (-50,-320,fg),
        (-280,-320,fg),
        (-330,-370,fg),
        (-400,-370,fg)
    ],
    'stops':[
        (190-hg,-80-hg),
        (80,-190),
        (-220,-320),
        (-400+2*fg,-370)
        ]
}
g_line = {
    'color':'#9933FF',
    'width':fg/2,
    'points':[
        (1000,280,fg),
        (210-g54,280,fg),
        (-45-g54,-60,fg),
        (-1000,-60,3*fg),
        (-1000,1000,fg)
    ],
    'stops':[
        (220+fg,280),
        (150-g45,200+g35),
        (30+g35-g45,40+g45+g35),
        (0-g45-2*g35,-2*g45+g35),
        (-220,-60),
        (-440+2*fg,-60),
        (-600,-60),
        (-750,-60),
        (-900,-60),
    ]
}
w_line = {
    'color':'#00FFFF',
    'width':fg/2,
    'points':[
        (190-2*hg,-80,fg),
        (70-2*hg,-200,fg),
        (-50,-200,fg),
        (-80,-170,fg),
        (-400,-170,fg)
    ],
    'stops':[
        (190-2*hg,-80),
        (80-hg,-190+hg),
        (-30,-200),
        (-120,-170),
        (-220,-170),
        (-310,-170),
        (-440+2*fg,-170),
        ]
}
caltrain = {
    'color':'#AAAAAA',
    'width':fg/4,
    'points':[
        (150,1000,2*fg),
        (150,450-g54,2*fg),
        (30,290-g54,2*fg),
        (230-g35,140-g45,2*fg),
        (110,-20,2*fg),
        (270,-140,2*fg),
        (1000,-140,2*fg)
    ],
    'stops':[
        (150,520),
        (150-g35,200-g45),
        (190,-80)
    ]
}
newtrain = {
    'color':'#AAAAAA',
    'width':fg/4,
    'points':[
        (190,-80,2*fg),
        (-10,70,2*fg),
        (-400,70,2*fg)
    ],
    'stops':[
        (30,40),
        (-80-40/3-g53-fg,70),
        (-440+2*fg,70),
    ]
}

mapdata['lines']['Bart'] = bart
mapdata['lines']['M Line'] = m_line
mapdata['lines']['M Line N Branch'] = m_line_n_branch
mapdata['lines']['M Line J Branch'] = m_line_j_branch
mapdata['lines']['F Line'] = f_line
mapdata['lines']['F Line Ext'] = f_line_ext
mapdata['lines']['J Line'] = j_line
mapdata['lines']['C Line'] = c_line
mapdata['lines']['C Line Ext'] = c_line_ext
mapdata['lines']['G Line'] = g_line
mapdata['lines']['W Line'] = w_line
mapdata['lines']['Caltrain'] = caltrain
mapdata['lines']['New Train'] = newtrain

filename = 'outputs/SanFrancisco_map.svg'
drawing=create_map(mapdata, filename, grid=1)
linegroup=drawing.g(id='lines')
stopgroup=drawing.g(id='stops')
lines(mapdata, linegroup, stopgroup)
drawing.add(linegroup)
drawing.add(stopgroup)
drawing.save()