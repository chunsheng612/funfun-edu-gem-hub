# FunFun Edu Gem Hub 🎓
> **全能教育 AI 助理與 172 款 Gemini Gems 智慧調度中樞 (Universal Educational AI Agent Skill)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gemini Gems](https://img.shields.io/badge/Gemini%20Gems-172%20Total-blue.svg)](https://gemini.google.com/)
[![108 Curriculum](https://img.shields.io/badge/Taiwan%20Curriculum-108%E8%AA%B2%E7%B6%B1-green.svg)](https://www.k12ea.gov.tw/)
[![AI Agent Ready](https://img.shields.io/badge/AI%20Agent-Skill%20Specification-purple.svg)](./SKILL.md)

---

## 📖 專案簡介 (Overview)

`funfun-edu-gem-hub` 是一個專為**臺灣教育現場（K-12、特殊教育、行政管理）**打造的頂級 AI 智能調度 Skill。

本專案彙整了現場教師與教育工作者精雕細琢的 **172 款 Gemini Gems**，將其結構化、模組化為單一的 AI Agent Skill。當教師或使用者提出任何教學問題時，中樞系統能自動識別需求、錨定目標學科與年級，並自動載入最佳對應的 Gem 專業提示詞架構，產出完全符合臺灣教育在地語境的高品質成果。

---

## 🌟 八大核心教育領域 (Core Domains)

| 領域分類 | 收錄 Gems 範例 | 核心功能與情境 |
| :--- | :--- | :--- |
| **1. 特殊教育與個別化支持** | `UDL教材重編`、`AAC溝通圖卡`、`ABC行為紀錄`、`易讀版轉換`、`情緒調節` | 融合教育、IEP目標撰寫、低認知負荷教材、社交故事與行為介入 |
| **2. 課程設計與素養教案** | `素養教案設計顧問`、`公開觀課教案`、`SEL教案`、`探究實作設計` | 108 課綱三面九項核心素養、逆向設計 (UbD)、跨領域與公開課演示 |
| **3. 評量命題與作業批改** | `國小/國中/高中作文批改`、`直式手寫OCR`、`雙向細目表試題`、`作業追問` | 國中小至學測指考手寫作文辨識、六級分診斷、4F思考學習單 |
| **4. 語文學習與閱讀素養** | `生字故事漫畫`、`成語看圖猜謎`、`古文漫畫`、`PIRLS閱讀測驗`、`英文錯題` | 國語文深度理解、歷史典故漫畫腳本、文言文趣味轉化、英文文法補救 |
| **5. 班級經營與親師溝通** | `開學第一週救命包`、`親師LINE訊息轉譯`、`家長問題回覆`、`學期評語` | 親師溝通情緒降溫、班級常規建立、正向語言聯絡簿、學期綜合評語 |
| **6. 視覺設計與教育繪圖** | `教材心智圖`、`4x4情緒圖卡`、`LINE貼圖大師`、`課表美編`、`研習海報` | 教學視覺化、多風格個人插畫 (日系/美式/莫蘭迪/普普)、資訊圖表 |
| **7. 遊戲化學習與教具** | `EduGame (教案轉HTML遊戲)`、`2D橫版遊戲藍圖`、`媒體素養冒險劇本` | 將教學文本自動轉換為免安裝單一 HTML 互動遊戲與遊戲化學習關卡 |
| **8. 行政公文與專案計畫** | `FormalHelp (公文函稿)`、`計畫撰寫傭人`、`教學卓越獎診斷`、`校事會議` | 學校標準公文簽呈、教育部競爭型計畫書起草、創新教學獎項論述 |

---

## 📂 目錄架構 (Repository Structure)

```text
.
├── SKILL.md                     # AI Agent Skill 核心規範文件 (含 YAML Frontmatter)
├── README.md                    # 專案說明與使用手冊
├── LICENSE                      # MIT 開源授權協議
├── requirements.txt             # Python 工具相依套件
├── .gitignore                   # Git 忽略檔案設定
├── .github/                     # GitHub Actions CI 與 Issue 範本
│   ├── workflows/
│   │   └── validate-skill.yml   # 自動化驗證 Skill 與 JSON 語法
│   └── ISSUE_TEMPLATE/
│       ├── new_gem_request.yml  # 新增 Gem 提案範本
│       └── bug_report.yml       # 錯誤回報範本
├── gems/                        # 172 款 Gem 獨立 Markdown 檔案目錄
│   ├── FunFun.AI-故事語織小幫手.md
│   ├── FunFun.AI-素養導向教案設計資深顧問.md
│   ├── FunFun.AI-UDL教材重編小幫手(特殊教育).md
│   └── ... (共 172 個 Markdown 檔)
├── references/                  # 結構化資料與索引參考庫
│   ├── gems_registry.json       # 172 款 Gems 完整 JSON 資料庫 (含 Prompt 與 ID)
│   ├── gems_quick_index.md      # 快速對照索引表 (含觸發關鍵字)
│   └── categories.json          # 八大領域分類映射表
└── scripts/                     # 實用輔助工具腳本
    ├── search_gems.py           # 本地關鍵字與領域搜尋 CLI 工具
    ├── export_gems_csv.py       # 匯出為 Excel/CSV 總表腳本
    └── validate_skill.py        # 完整性與 JSON Schema 檢驗腳本
```

---

## 🚀 使用方式 (How to Use)

### 1. 於 AI Agent 平台載入 (Gemini / Claude / AutoGen / CrewAI)
直接將根目錄下的 `SKILL.md` 與 `references/` 資料夾引入您的 AI Agent Workspace 或 Skill 目錄：
- 當使用者提出：「*請幫我把三年級這篇自然課文改成易讀版學習單*」
- 系統將自動觸發 `funfun-edu-gem-hub`，並檢索載入 `FunFun.AI-易讀版教材轉換機器人(特殊教育)` 的提示詞規範進行高品質輸出。

### 2. 使用本地搜尋 CLI 尋找 Gems
本專案內建 Python 搜尋工具，方便快速查閱 172 款 Gem 的完整提示詞：

```bash
# 搜尋與「作文」相關的 Gem
python scripts/search_gems.py --keyword 作文

# 瀏覽「特殊教育」分類下的所有 Gem
python scripts/search_gems.py --category special_education

# 顯示特定 Gem 的完整 Prompt 內容
python scripts/search_gems.py --id 1bWDlh53dK2-564ABlpX-xxUFeRyDTOKY --show-prompt
```

### 3. 匯出 CSV 試算表
若需在 Microsoft Excel 或 Google 試算表檢視所有 Gems：
```bash
python scripts/export_gems_csv.py
```

---

## 🛠️ 開發與貢獻 (Contributing)

歡迎廣大教育工作者共同擴充與優化本專案：

1. **Fork 本專案**
2. **新增或修改 `gems/` 中的 Markdown 檔案**
3. **執行驗證腳本**：
   ```bash
   python scripts/validate_skill.py
   ```
4. **提交 Pull Request**，我們將於第一時間進行審查並合併！

---

## 📄 授權條款 (License)

本專案採用 [MIT License](LICENSE) 授權開源，歡迎教育界同仁、各級學校與非營利組織自由使用、修改與推廣。

---
*Created with ❤️ for Taiwan Educators.*
