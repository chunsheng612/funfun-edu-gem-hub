#!/usr/bin/env python3
import json, csv, os

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    reg_path = os.path.join(base_dir, 'references', 'gems_registry.json')
    out_csv = os.path.join(base_dir, 'references', 'gems_export.csv')

    with open(reg_path, 'r', encoding='utf-8') as f:
        gems = json.load(f)

    with open(out_csv, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['序號', 'Gem ID', 'Gem 名稱', '擁有者', '說明 (Description)', '系統提示詞 (System Instructions)', 'Gem 連結'])
        for idx, g in enumerate(gems, 1):
            writer.writerow([idx, g['id'], g['name'], g.get('owner', ''), g['description'], g['instructions'], g['url']])

    print(f"成功匯出 {len(gems)} 款 Gems 至 {out_csv}")

if __name__ == '__main__':
    main()
