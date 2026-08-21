#!/usr/bin/env python3
import json, os, sys

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_path = os.path.join(base_dir, 'SKILL.md')
    reg_path = os.path.join(base_dir, 'references', 'gems_registry.json')
    gems_dir = os.path.join(base_dir, 'gems')

    print("開始驗證 FunFun Edu Gem Hub 結構...")
    
    # Check SKILL.md
    if not os.path.exists(skill_path):
        print("❌ 找不到 SKILL.md！")
        sys.exit(1)
    with open(skill_path, 'r', encoding='utf-8') as f:
        skill_text = f.read()
    if not skill_text.startswith("---") or "name: funfun-edu-gem-hub" not in skill_text:
        print("❌ SKILL.md frontmatter 格式不符！")
        sys.exit(1)
    print("✅ SKILL.md 格式驗證通過！")

    # Check gems_registry.json
    if not os.path.exists(reg_path):
        print("❌ 找不到 references/gems_registry.json！")
        sys.exit(1)
    with open(reg_path, 'r', encoding='utf-8') as f:
        gems = json.load(f)
    print(f"✅ references/gems_registry.json 載入成功（共 {len(gems)} 款 Gems）！")

    # Check individual gem files
    gem_files = [f for f in os.listdir(gems_dir) if f.endswith('.md')]
    print(f"✅ gems/ 目錄包含 {len(gem_files)} 個 Markdown 檔案！")

    if len(gem_files) != len(gems):
        print(f"⚠️ 警告：Markdown 檔案數量 ({len(gem_files)}) 與 Registry 數量 ({len(gems)}) 不完全一致。")
    else:
        print("✅ 所有 Gem Markdown 檔案與資料庫數量完全吻合！")

    print("\n🎉 所有驗證皆已順利通過！")

if __name__ == '__main__':
    main()
