import svgwrite
import math

def create_map(mapdata, filepath, grid=True):

    bg = mapdata['background']
    width = bg['width']
    height = bg['height']

    dwg = svgwrite.Drawing(filepath, size = (width, height))

    dwg.add(
        dwg.rect(
            insert = (0, 0),
            size = (width, height),
            fill = bg['color']
        )
    )

    if grid:
        major = bg['major']
        minor = bg['minor']
        xmajor = major
        xminor = minor
        ymajor = major
        yminor = minor
        while xminor < width:
            dwg.add(
                dwg.line(
                    start = (xminor, 0),
                    end = (xminor, height),
                    stroke = "#777777"
                )
            )
            xminor += minor
        while yminor < height:
            dwg.add(
                dwg.line(
                    start = (0, yminor),
                    end = (width, yminor),
                    stroke = '#777777'
                )
            )
            yminor += minor
        while xmajor < width:
            dwg.add(
                dwg.line(
                    start = (xmajor, 0),
                    end = (xmajor, height),
                    stroke = '#777777',
                    stroke_width = 2
                )
            )
            xmajor += major
        while ymajor < height:
            dwg.add(
                dwg.line(
                    start = (0, ymajor),
                    end = (width, ymajor),
                    stroke = '#777777',
                    stroke_width = 2
                )
            )
            ymajor += major

    return dwg

def line(linedata, dwg):
    color = linedata.get('color', '#000000')
    width = linedata.get('width', 4)
    points = linedata.get('points', [])
    if len(points) < 2:
        raise ValueError("Need at least two points for a path")

    # Normalize points to (x, y, r)
    pts = []
    for p in points:
        if len(p) == 2:
            pts.append((*p, 0))
        elif len(p) == 3:
            pts.append(p)
        else:
            raise ValueError("Each point must be (x, y) or (x, y, radius)")

    path = dwg.path(d=f"M {pts[0][0]},{pts[0][1]}", fill="none",
                    stroke=color, stroke_width=width,
                    stroke_linecap="round", stroke_linejoin="round")

    for i in range(1, len(pts) - 1):
        p1, p2, p3 = pts[i-1], pts[i], pts[i+1]
        r = p2[2]

        if r <= 0:
            # Sharp corner
            path.push(f"L {p2[0]},{p2[1]}")
            continue

        # Direction vectors
        v1 = (p1[0] - p2[0], p1[1] - p2[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])

        len1 = math.hypot(*v1)
        len2 = math.hypot(*v2)
        if len1 == 0 or len2 == 0:
            continue
        v1n = (v1[0] / len1, v1[1] / len1)
        v2n = (v2[0] / len2, v2[1] / len2)

        # Angle between segments
        dot = v1n[0]*v2n[0] + v1n[1]*v2n[1]
        angle = math.acos(max(-1, min(1, dot)))

        # Distance to trim on each segment
        tangent = math.tan(angle / 2)
        dist = min(r / tangent, len1 / 2, len2 / 2)

        # Compute arc start and end points
        start = (p2[0] + v1n[0]*dist, p2[1] + v1n[1]*dist)
        end   = (p2[0] + v2n[0]*dist, p2[1] + v2n[1]*dist)

        cross = v1n[0] * v2n[1] - v1n[1] * v2n[0]
        angle_dir = '+' if cross < 0 else '-'

        path.push(f"L {start[0]},{start[1]}")
        path.push_arc(target=end, rotation=0, r=r,
                      large_arc=False, angle_dir=angle_dir)

    # Line to last point
    path.push(f"L {pts[-1][0]},{pts[-1][1]}")

    dwg.add(path)
    return path

def station(mapdata, dwg):
    pass


