#!/usr/bin/env python3
"""Create missing RGBA placeholder sprites for queued asset slots, no dependencies."""
import json, struct, zlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def png_chunk(tag,data):
    return struct.pack('>I',len(data))+tag+data+struct.pack('>I',zlib.crc32(tag+data)&0xffffffff)
def placeholder(w,h):
    scan=bytearray()
    for y in range(h):
        scan.append(0)
        for x in range(w):
            border=x in (1,w-2) or y in (1,h-2)
            inset=(3<=x<w-3 and 3<=y<h-3)
            if border: rgba=(84,101,121,255)
            elif inset: rgba=(166,177,188,160) if (x//8+y//8)%2 else (196,202,210,160)
            else: rgba=(0,0,0,0)
            scan.extend(rgba)
    return b'\x89PNG\r\n\x1a\n'+png_chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,8,6,0,0,0))+png_chunk(b'IDAT',zlib.compress(bytes(scan),9))+png_chunk(b'IEND',b'')
if __name__=='__main__':
    q=json.loads((ROOT/'art/queue.json').read_text())
    count=0
    for batch in q['batches']:
        for a in batch['assets']:
            out=ROOT/a['path']
            if out.exists(): continue
            out.parent.mkdir(parents=True,exist_ok=True)
            out.write_bytes(placeholder(a['canvas']['width'],a['canvas']['height']))
            count+=1
    print(f'Created {count} missing placeholders; preserved all existing PNG files')
