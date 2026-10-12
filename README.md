# 九龍街頭 V0.8 — 真實旺角 OSM 地圖技術測試

## 部署
將 index.html、mongkok-map.json、manifest.webmanifest 一起上傳到 GitHub Pages Repository 根目錄，並啟用 Pages。必須透過 http(s) 網站開啟，直接雙擊 index.html 會因瀏覽器限制而無法 fetch 地圖。

## 功能
- 真實旺角道路及建築輪廓，來自用戶提供的 Geofabrik Hong Kong 2026-10-10 OSM PBF；提取區域約 114.1605–114.1785 E、22.309–22.329 N
- 2.5D 投影建築、角色移動、車輛、行人、基礎碰撞、上落車、出拳、任務、本機存檔、手機搖桿及鏡頭縮放
- 本版本為可玩技術原型，並非正式道路交通模擬：交通車輛僅沿所屬路段移動並在路段端點循環；不會智能過路口。道路寬度、單雙程、車道位置、轉彎、碰撞及任務位置尚未逐條校準；角色也可能在非道路地面行走。部分行人、車輛與建築可能重疊。警察追捕 AI 尚未整合。
- 使用真實街道幾何，並不代表每個遊戲模型、招牌、建築高度都真實。

## 授權與資料來源
Map data © OpenStreetMap contributors (https://www.openstreetmap.org/copyright), licensed under ODbL 1.0. Extract obtained from Geofabrik (https://download.geofabrik.de/asia/china.html). If you redistribute an adapted OSM database, review the ODbL share-alike requirements. 本遊戲程式可自由修改，地圖資料仍受其原授權約束。

## 操作
電腦 WASD / 方向鍵、E 上落車、J 出拳、空白鍵煞車、滑鼠滾輪縮放；手機左側搖桿及右側按鈕。自動儲存於本機瀏覽器。
