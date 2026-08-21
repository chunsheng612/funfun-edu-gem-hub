#!/usr/bin/env python3
import json, argparse, os, sys

def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    reg_path = os.path.join(base_dir, 'references', 'gems_registry.json')
    cat_path = os.path.join(base_dir, 'references', 'categories.json')
    
    if not os.path.exists(reg_path):
        print(f"Error: Could not find {reg_path}")
        sys.exit(1)
        
    with open(reg_path, 'r', encoding='utf-8') as f:
        gems = json.load(f)
    with open(cat_path, 'r', encoding='utf-8') as f:
        categories = json.load(f)
        
    return gems, categories

def main():
    parser = argparse.ArgumentParser(description="FunFun Edu Gem Hub 搜尋工具")
    parser.add_argument("-k", "--keyword", help="搜尋關鍵字 (名稱、說明或提示詞)")
    parser.add_argument("-c", "--category", help="搜尋指定領域分類 (例如: special_education, lesson_planning, assessment_and_grading, language_and_reading, classroom_management, visual_and_design, gamification, school_admin)")
    parser.add_argument("-i", "--id", help="以 Gem ID 查詢詳細資料")
    parser.add_argument("--show-prompt", action="store_true", help="顯示完整系統提示詞內容")
    args = parser.parse_args()

    gems, categories = load_data()

    if args.id:
        match = next((g for g in gems if g['id'] == args.id), None)
        if match:
            print(f"\n=== {match['name']} ===")
            print(f"Gem ID: {match['id']}")
            print(f"連結: {match['url']}")
            print(f"說明: {match['description']}")
            if args.show_prompt:
                print("\n[系統提示詞 / System Instructions]:")
                print("-" * 50)
                print(match['instructions'])
                print("-" * 50)
        else:
            print(f"找不到 ID 為 {args.id} 的 Gem。")
        return

    if args.category:
        if args.category in categories:
            cat_data = categories[args.category]
            print(f"\n=== 分類：{cat_data['title']} (共 {len(cat_data['gems'])} 個) ===")
            for idx, g in enumerate(cat_data['gems'], 1):
                print(f"{idx:2d}. {g['name']} (ID: {g['id']}) -> gems/{g.get('filename', '')}")
        else:
            print(f"無效的分類名稱。可用分類：{', '.join(categories.keys())}")
        return

    keyword = args.keyword.strip() if args.keyword else ""
    if not keyword:
        print(f"總共收錄 {len(gems)} 款 Gems。請使用 -k/--keyword 或 -c/--category 進行搜尋。")
        return

    results = []
    for g in gems:
        if (keyword.lower() in g['name'].lower() or 
            keyword.lower() in g['description'].lower() or 
            keyword.lower() in g['instructions'].lower()):
            results.append(g)

    print(f"\n找到 {len(results)} 個符合「{keyword}」的 Gems：")
    print("-" * 70)
    for idx, g in enumerate(results, 1):
        desc = g['description'].replace('\n', ' ')[:45] if g['description'] else '（無描述）'
        print(f"{idx:2d}. {g['name']:<30} | ID: {g['id']} | {desc}")
        if args.show_prompt:
            print(f"   [提示詞摘要]: {g['instructions'][:100].replace(chr(10), ' ')}...")
            print("-" * 70)

if __name__ == '__main__':
    main()
