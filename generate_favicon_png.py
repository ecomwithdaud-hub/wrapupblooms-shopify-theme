import zlib
import struct
import math

def create_flower_png(filename, size=64):
    width = size
    height = size
    # Create RGBA buffer
    pixels = []
    cx, cy = (width - 1) / 2.0, (height - 1) / 2.0
    r_max = (size / 2.0) - 2.0

    raw_data = bytearray()
    
    for y in range(height):
        raw_data.append(0)  # filter type 0 (None)
        for x in range(width):
            dx = x - cx
            dy = y - cy
            dist = math.hypot(dx, dy)
            angle = math.atan2(dy, dx)
            
            # 5-petal flower shape: r(theta) = r_base + amp * cos(5 * theta)
            # Petal shape formula
            petal_curve = 0.65 + 0.32 * math.cos(5 * angle)
            flower_r = r_max * petal_curve
            
            # Center pistil radius
            center_r = r_max * 0.28
            
            if dist <= center_r:
                # Golden core / pistil
                # radial gradient from gold to warm honey
                t = dist / center_r
                r = int(255 * (1 - t*0.2))
                g = int(210 * (1 - t*0.3))
                b = int(70 * (1 - t*0.5))
                a = 255
            elif dist <= flower_r:
                # Pink petal with smooth gradient
                t = (dist - center_r) / (flower_r - center_r + 1e-5)
                # Anti-aliasing at the edge
                edge_dist = flower_r - dist
                if edge_dist < 1.0:
                    alpha_factor = max(0.0, edge_dist)
                else:
                    alpha_factor = 1.0
                
                # Rose pink to blush tip
                # Inner: #F48FB1, Outer: #E91E63 / #C2185B
                r = int(248 - 30 * t)
                g = int(140 - 70 * t)
                b = int(165 - 40 * t)
                a = int(255 * alpha_factor)
            elif dist <= flower_r + 1.0:
                # Outer anti-aliasing edge
                alpha_factor = max(0.0, 1.0 - (dist - flower_r))
                r, g, b = 218, 70, 125
                a = int(255 * alpha_factor)
            else:
                r, g, b, a = 0, 0, 0, 0

            raw_data.extend([r, g, b, a])

    def chunk(chunk_type, data):
        c = chunk_type + data
        crc = struct.pack(">I", zlib.crc32(c) & 0xffffffff)
        return struct.pack(">I", len(data)) + c + crc

    png_bytes = bytearray(b"\x89PNG\r\n\x1a\n")
    # IHDR: width, height, bit_depth=8, color_type=6 (RGBA), compression=0, filter=0, interlace=0
    ihdr_data = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    png_bytes.extend(chunk(b"IHDR", ihdr_data))
    
    # IDAT
    compressed = zlib.compress(bytes(raw_data), 9)
    png_bytes.extend(chunk(b"IDAT", compressed))
    
    # IEND
    png_bytes.extend(chunk(b"IEND", b""))
    
    with open(filename, "wb") as f:
        f.write(png_bytes)
    print(f"Generated {filename} ({len(png_bytes)} bytes)")

create_flower_png("favicon.png", 64)
create_flower_png("WrapUpBlooms-Theme/assets/favicon.png", 64)
