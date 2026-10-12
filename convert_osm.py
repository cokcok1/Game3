#!/usr/bin/env python3
"""Convert an OSM Overpass JSON export to local game geometry. Python standard library only."""
import json,sys,math
from pathlib import Path
if len(sys.argv)!=3:
 print('用法：python3 convert_osm.py mongkok-overpass.json data/mongkok-map.json');sys.exit(1)
data=json.loads(Path(sys.argv[1]).read_text());els=data.get('elements',[])
roads=[];buildings=[]
# Fixed Mong Kok bounding box; intentionally no external API requests.
west,east,south,north=114.162,114.177,22.313,22.327
w,h=2600,2300
for e in els:
 if e.get('type')!='way' or not e.get('geometry'):continue
 tags=e.get('tags',{});g=e['geometry']
 pts=[]
 for p in g:
  x=(p['lon']-west)/(east-west)*w;y=(north-p['lat'])/(north-south)*h
  pts.append([round(x,1),round(y,1)])
 if tags.get('highway') in ['motorway','trunk','primary','secondary','tertiary','residential','unclassified','service','living_street']:
  widths={'primary':33,'secondary':29,'tertiary':25,'residential':19,'service':13}
  roads.append({'name':tags.get('name:zh-Hant') or tags.get('name:zh') or tags.get('name',''),'width':widths.get(tags['highway'],23),'points':pts})
 if 'building' in tags and len(pts)>2:buildings.append({'points':pts})
out={'source':'OpenStreetMap contributors','license':'ODbL 1.0','bbox':[south,west,north,east],'roads':roads,'buildings':buildings}
Path(sys.argv[2]).parent.mkdir(parents=True,exist_ok=True)
Path(sys.argv[2]).write_text(json.dumps(out,ensure_ascii=False,separators=(',',':')))
print('已輸出',len(roads),'條道路及',len(buildings),'個建築輪廓')
