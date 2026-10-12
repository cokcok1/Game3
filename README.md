# 九龍街頭 V0.83 — 旺角街網校準版

## 已實作
- 保留 V0.82 WebGL 3D 第三身鏡頭、360° 旋轉、雙指縮放、手機搖桿。
- 建築外牆依照 OSM 多邊形輪廓建立（不再以建築 bounding box 取代）。
- 加入北向固定小地圖、附近街道名稱、地標快速定位（定位至對應 OSM 道路附近，非精確 POI 入口）。
- 顯示 OSM 授權標示。

## 限制
- 道路中心線與建築輪廓為真實 OSM 資料；道路寬度是估計值，建築高度、顏色、外觀為模擬。
- 地標定位以同名道路近中心點代替，非精準門牌地址。
- 仍未有完整車輛、NPC、格鬥或任務。
- 未有手機實機測試；只完成語法和封裝檢查。

## 安裝
解壓後把 index.html、mongkok-map.json、manifest.webmanifest 上傳 GitHub Pages repository 根目錄。開啟網站，不能直接用 file:// 雙擊 HTML。

## 授權
地圖資料 © OpenStreetMap contributors，Open Database License (ODbL) 1.0。https://www.openstreetmap.org/copyright
