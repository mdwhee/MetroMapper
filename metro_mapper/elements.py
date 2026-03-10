import svgwrite
import math

def create_map(mapdata, filepath, grid=True):

    background_color = mapdata['style']['background']['color']
    width = mapdata['style']['background']['width']
    height = mapdata['style']['background']['height']
    grid_color = mapdata['style']['grid']['color']
    grid_major = mapdata['style']['grid']['major']
    grid_minor = mapdata['style']['grid']['minor']
    center = mapdata['style'].get('center', (0, 0))

    dwg = svgwrite.Drawing(filepath, size = (width, height))

    dwg.add(
        dwg.rect(
            insert = (0, 0),
            size = (width, height),
            fill = background_color
        )
    )

    if grid:
        major = grid_major
        minor = grid_minor
        xmajor = major
        xminor = minor
        ymajor = major
        yminor = minor
        while xminor < width:
            dwg.add(
                dwg.line(
                    start = (xminor, 0),
                    end = (xminor, height),
                    stroke = grid_color,
                )
            )
            xminor += minor
        while yminor < height:
            dwg.add(
                dwg.line(
                    start = (0, yminor),
                    end = (width, yminor),
                    stroke = grid_color,
                )
            )
            yminor += minor
        while xmajor < width:
            dwg.add(
                dwg.line(
                    start = (xmajor, 0),
                    end = (xmajor, height),
                    stroke = grid_color,
                    stroke_width = 2
                )
            )
            xmajor += major
        while ymajor < height:
            dwg.add(
                dwg.line(
                    start = (0, ymajor),
                    end = (width, ymajor),
                    stroke = grid_color,
                    stroke_width = 2
                )
            )
            ymajor += major
        dwg.add(
            dwg.line(
                start = (center[0], 0),
                end = (center[0], height),
                stroke = grid_color,
                stroke_width = 4
            )
        )
        dwg.add(
            dwg.line(
                start = (0, center[1]),
                end = (width, center[1]),
                stroke = grid_color,
                stroke_width = 4
            )
        )

    return dwg

def lines(mapdata, lgrp, sgrp):
    cx, cy = mapdata['style'].get('center', (0, 0))
    for linedata in mapdata['lines'].values():
        color = linedata.get('color', '#000000')
        width = linedata.get('width', 4)
        gap = mapdata['style'].get('gap', 10)
        background_color = mapdata['style']['background'].get('color', '#000000')
        raw_points = linedata.get('points', [])
        center_stripe_width = linedata.get('center_stripe_width', width / 3)

        if len(raw_points) < 2:
            raise ValueError("Need at least two points for a path")

        # Flatten points and record tunnel index ranges
        pts = []
        tunnels = []  # list of (start_idx, end_idx) into pts
        for item in raw_points:
            if isinstance(item, list):
                start_idx = len(pts)  # tunnel starts at first point in sub-list
                for p in item:
                    if len(p) == 2:
                        pts.append((p[0] + cx, p[1] + cy, 0))
                    elif len(p) == 3:
                        pts.append((p[0] + cx, p[1] + cy, p[2]))
                    else:
                        raise ValueError("Each point must be (x, y) or (x, y, radius)")
                tunnels.append((start_idx, len(pts) - 1))
            else:
                p = item
                if len(p) == 2:
                    pts.append((p[0] + cx, p[1] + cy, 0))
                elif len(p) == 3:
                    pts.append((p[0] + cx, p[1] + cy, p[2]))
                else:
                    raise ValueError("Each point must be (x, y) or (x, y, radius)")

        def build_path(pt_indices):
            """Build an SVG path through a subset of pts by index."""
            idxs = list(pt_indices)
            if len(idxs) < 2:
                return None
            p = svgwrite.path.Path(d=f"M {pts[idxs[0]][0]},{pts[idxs[0]][1]}",
                                   fill="none", stroke_linecap="round", stroke_linejoin="round")
            for ii in range(1, len(idxs) - 1):
                i = idxs[ii]
                p1 = pts[i - 1] if i > 0 else pts[i]
                p2 = pts[i]
                p3 = pts[i + 1] if i < len(pts) - 1 else pts[i]
                r = p2[2]

                if r <= 0:
                    p.push(f"L {p2[0]},{p2[1]}")
                    continue

                v1 = (p1[0] - p2[0], p1[1] - p2[1])
                v2 = (p3[0] - p2[0], p3[1] - p2[1])
                len1 = math.hypot(*v1)
                len2 = math.hypot(*v2)
                if len1 == 0 or len2 == 0:
                    continue
                v1n = (v1[0]/len1, v1[1]/len1)
                v2n = (v2[0]/len2, v2[1]/len2)
                dot = v1n[0]*v2n[0] + v1n[1]*v2n[1]
                angle = math.acos(max(-1, min(1, dot)))
                tangent = math.tan(angle / 2)
                dist = min(r / tangent, len1/2, len2/2)
                start = (p2[0] + v1n[0]*dist, p2[1] + v1n[1]*dist)
                end   = (p2[0] + v2n[0]*dist, p2[1] + v2n[1]*dist)
                cross = v1n[0]*v2n[1] - v1n[1]*v2n[0]
                angle_dir = '+' if cross < 0 else '-'
                p.push(f"L {start[0]},{start[1]}")
                p.push_arc(target=end, rotation=0, r=r,
                           large_arc=False, angle_dir=angle_dir, absolute=True)

            p.push(f"L {pts[idxs[-1]][0]},{pts[idxs[-1]][1]}")
            return p

        # Draw base colored line (full path)
        base_path = build_path(range(len(pts)))
        base_path['stroke'] = color
        base_path['stroke-width'] = width
        lgrp.add(base_path)

        # Draw black center stripe for each tunnel
        for (start_idx, end_idx) in tunnels:
            stripe_path = build_path(range(start_idx, end_idx + 1))
            if stripe_path:
                stripe_path['stroke'] = '#000000'
                stripe_path['stroke-width'] = center_stripe_width
                lgrp.add(stripe_path)

        # Stops
        for stop in linedata.get('stops', []):
            sx, sy = stop
            stop_circle = svgwrite.shapes.Circle(center=(sx+cx, sy+cy), r=gap/2-gap/8,
                                                 fill=background_color, stroke=color,
                                                 stroke_width=gap/4)
            sgrp.add(stop_circle)

def station(mapdata, dwg):
    pass


