# 九龍街頭 V0.4 — 地圖資料管線原型

## 可玩內容
沿用 V0.3：步行、駕駛、車流、NPC、速遞、警察追捕、車況、觸控、小地圖、本機存檔。新增可讀取本地 OSM 幾何 JSON 的**視覺地圖層**。不需 API Key。

## 地圖真實度與限制（請先閱讀）
- **ZIP 沒有預先打包真實 OSM 地圖數據**，因此直接部署時仍會顯示示意街網。不能宣稱已完成真實旺角地圖。
- 提供 Overpass 查詢及純 Python 轉檔工具。只需在開發時一次性取得公開 OSM 資料，遊戲運行時完全不需要 API。
- 導入後會顯示按經緯度投影的道路及建築輪廓；**碰撞、交通、警車路徑、任務點仍使用舊版示意座標**，尚未與 OSM 幾何一致。現階段只用作視覺驗證，不是已完成真實地圖駕駛。
- OSM 資料可能有缺漏，且道路寬度是遊戲估算值。

## 如何匯入真實道路（選用）
1. 開啟 https://overpass-turbo.eu/ ，貼入 `overpass-query.txt` 內容，按 Run，Export → raw data → download JSON，命名為 `mongkok-overpass.json`。
2. 電腦有 Python 3 的話執行：`python3 convert_osm.py mongkok-overpass.json data/mongkok-map.json`。
3. 將整個資料夾上傳 GitHub Pages；程式會自動載入 `data/mongkok-map.json`。唔需要申請 API Key。

## GitHub Pages
上傳整個專案內容到公開 GitHub Repository 根目錄，Settings → Pages → Deploy from a branch → main / (root)。如果未匯入 OSM，直接可玩示意版本。

## 授權
若加入 OSM 衍生地圖資料，須顯示 `© OpenStreetMap contributors`、ODbL 授權連結 https://www.openstreetmap.org/copyright ，並遵守 ODbL 相關條款。程式碼與地圖資料授權分開處理。

## 已知問題
本版只係地圖資料管線雛形；實機跨瀏覽器測試未完成。真實街網碰撞及導航係下一階段工作。
