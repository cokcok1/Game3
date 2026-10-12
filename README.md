# 九龍街頭 V0.1 — 可玩技術原型

## 使用
開啟 `index.html` 即可試玩，無須安裝套件、伺服器或 API Key。電腦以方向鍵/WASD 移動、E 上落車、R 重設位置；手機使用畫面按鈕。

## GitHub Pages 發布
1. 在 GitHub 建立公開 Repository，例如 `kowloon-streets`。
2. 將 `index.html` 上傳到 Repository 根目錄（README.md 可一併上傳）。
3. 進入 Settings → Pages，Source 選 Deploy from a branch，Branch 選 main，資料夾選 /(root)，儲存。
4. 等待 GitHub Pages 部署，打開 `https://你的帳號.github.io/kowloon-streets/`。

## 目前已有
- 可玩 2D 城市畫面、手機觸控及電腦鍵盤操作
- 步行／駕駛切換、建築物碰撞、簡單移動車流
- 跟隨鏡頭、街名提示、本機自動存檔

## 尚未完成（重要）
- **街道網格是為測試而繪製的旺角風格示意圖，不是真實地理座標，也不是已匯入的 OpenStreetMap 資料。** 街名用作風格標示，位置並不準確。
- 上落車為原型模式切換，未實作走近車輛、車輛佔用等邏輯。
- 未有真實交通導航、警察、任務、NPC、PWA 離線快取、音效及完整九龍地圖。

## 下一階段
1. 取得符合授權的 OpenStreetMap 九龍道路及建築資料，離線轉換成靜態 JSON。
2. 依真實座標投影道路，建立可駕駛路網、路口及碰撞。
3. 完善上落車、交通規則、行人、任務及分區載入。

這是原創 Web App 技術原型，不含 Rockstar Games 或 GTA 的美術素材。
