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
    'color':'#999999',
    'width':fg/2,
    'points':[
        [
            (1000,-210,fg),
            (280,-210,10*fg),
            (-280,210,10*fg),
            (-280,800,fg)
        ],
    ],
    'stops':[
        (180,-135),
        (100,-75),
        (0,0),
        (-80-40/3-g53+g35,70+g45),
        (-280,380),
        (-280,700)
    ]
}
m_line = {
    'color':'#00FF00',
    'width':fg/2,
    'points':[
        (150-g45,200+g35,fg),
        (270,110,fg),
        (270,-70+40/3,fg),
        [
            (230,-110,fg),
            (200-g35,-150-g45,fg),
            (-600-g53,450,fg)
        ],
    ],
    'stops':[
        (150-g45,200+g35),
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
n_branch = {
    'color':'#00FF00',
    'width':fg/3,
    'points':[
        (180-g35,-135-g45,fg),
        (-360-g53,270,fg),
        (-1000,270,fg)
    ],
    'stops':[
        (-500,270),
    ]
}
j_branch = {
    'color':'#00FF00',
    'width':fg/3,
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
        (150+g35-g45,200+g45+g35,fg),
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
        (-30,-450-fg,fg),
        (-140+fg,-450-fg,fg),
        (-140,-450,fg),
        (-440+fg,-450,fg),
        (-440+fg,380,fg),
        (-90+g53,380,fg),
        (150+g35,200+g45,fg),
    ],
    'stops':[
        (-200,-450),
        (-320,-450),
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
    ]
}
f_line_exp = {
    'color':'#FFFF00',
    'width':fg/2,
    'points':[
        (-440+fg,-480,fg),
        (-440+fg,380,fg),
        (240+fg,380,fg),
    ],
    'stops':[
        (-440+fg,-480),
        (240+fg,380)
    ]
}
c_line = {
    'color':'#FF0000',
    'width':fg/2,
    'points':[
        (240,1000,fg),
        (240,260,fg),
        (195,260,fg),
        (-30,-40,fg),
        (-30,-200+fg,fg)
    ],
    'stops':[
        (240,780),
        (240,660),
        (240,550),
        (240,460),
        (240,380),
        (240,300),
        (150+2*g35,200+2*g45),
        (105,140),
        (30+g35,40+g45),
        (0-2*g35,-2*g45),
        (-30,-200+fg),
    ]
}
c_line_ext = {
    'color':'#FF0000',
    'width':fg/2,
    'points':[
        (-30,-200+fg,fg),
        (-30,-300,fg),
        (-50,-320,fg),
        (-50,-430+fg,fg),
        (-30,-450+fg,fg)
    ],
    'stops':[
        (-40,-310),
        (-30,-450+fg),
    ]
}
c_line_exp = {
    'color':'#FF0000',
    'width':fg/2,
    'points':[
        (190-hg,-80-hg,fg),
        (-50,-320,fg),
        (-280,-320,fg),
        (-330,-370,fg),
        (-440+2*fg,-370,fg)
    ],
    'stops':[
        (190-hg,-80-hg),
        (80,-190),
        (-220,-320),
        (-440+2*fg,-370)
        ]
}
g_line_init = {
    'color':'#9933FF',
    'width':fg/2,
    'points':[
        (150+2*g35-g45,200+2*g45+g35),
        (-45-g54,-60,fg),
        (-500,-60,3*fg)
    ],
    'stops':[
        (240+fg,300),
        (150-g45,200+g35),
        (30+g35-g45,40+g45+g35),
        (0-g45-2*g35,-2*g45+g35),
        (-220,-60),
        (-440+2*fg,-60)
    ]
}
g_line = {
    'color':'#9933FF',
    'width':fg/2,
    'points':[
        (1000,300,fg),
        (225-g54,300,fg),
        (-45-g54,-60,fg),
        (-1100,-60,3*fg),
        (-1100,1000,fg)
    ],
    'stops':[
        (240+fg,300),
        (150-g45,200+g35),
        (30+g35-g45,40+g45+g35),
        (0-g45-2*g35,-2*g45+g35),
        (-220,-60),
        (-440+2*fg,-60),
        (-620,-60),
        (-800,-60),
        (-1000,-60),
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
    'color':'#CCCCCC',
    'width':fg/4,
    'points':[
        (150,1000,2*fg),
        (150,450-g54,2*fg),
        (30,290-g54,2*fg),
        (150-g35,200-g45,2*fg)
    ],
    'stops':[
        (150,620),
        (150-g35,200-g45)
    ]
}
portal = {
    'color':'#CCCCCC',
    'width':fg/4,
    'points':[
        (150-g35,200-g45),
        (230-g35,140-g45,2*fg),
        (110,-20,2*fg),
        (190,-80,2*fg)
    ],
    'stops':[
        (190,-80)
    ]
}
link21 = {
    'color':'#CCCCCC',
    'width':fg/4,
    'points':[
        (190,-80,2*fg),
        (270,-140,2*fg),
        (1000,-140,2*fg)
    ],
    'stops':[
    ]
}
newtrain = {
    'color':'#CCCCCC',
    'width':fg/4,
    'points':[
        (190,-80,2*fg),
        (-10,70,2*fg),
        (-620,70,2*fg),
        (-620,-60-fg,2*fg),
    ],
    'stops':[
        (30,40),
        (-80-40/3-g53-fg,70),
        (-440+2*fg,70),
        (-620,-60-fg),
    ]
}
tunnels = {
    'color':mapdata['style']['background']['color'],
    'width':fg/6,
    'points':[
        (180-g35,-135-g45,fg),
        (-360-g53,270,fg),
    ],
    'stops':[
    ]
}

phase = 0
# Phase 0 is existing
# Phase 1 is reroutes and retrofits
# Phase 2 is planned projects and extensions
# Phase 3+ are new projects and expansions

if phase < 1: mapdata['lines']['J Branch'] = j_branch
if phase > 1: mapdata['lines']['C Line Ext'] = c_line_ext
if phase > 2: mapdata['lines']['F Line Ext'] = f_line_ext
if phase > 3: mapdata['lines']['F Line Exp'] = f_line_exp
if phase > 0: mapdata['lines']['J Line'] = j_line
if phase > 2: mapdata['lines']['C Line Exp'] = c_line_exp
if 1 < phase < 3: mapdata['lines']['G Line Init'] = g_line_init
if phase > 2: mapdata['lines']['G Line'] = g_line
if phase > 3: mapdata['lines']['W Line'] = w_line
if phase > 1: mapdata['lines']['Portal'] = portal
if phase > 2: mapdata['lines']['Link21'] = link21
if phase > 3: mapdata['lines']['New Train'] = newtrain
mapdata['lines']['Bart'] = bart
mapdata['lines']['N Line'] = n_branch
mapdata['lines']['M Line'] = m_line
mapdata['lines']['C Line'] = c_line
mapdata['lines']['Caltrain'] = caltrain
mapdata['lines']['F Line'] = f_line
# mapdata['lines']['Tunnels'] = tunnels

filename = 'outputs/SanFrancisco_map.svg'
drawing=create_map(mapdata, filename, grid=1)
linegroup=drawing.g(id='lines')
stopgroup=drawing.g(id='stops')
lines(mapdata, linegroup, stopgroup)
drawing.add(linegroup)
drawing.add(stopgroup)
drawing.save()