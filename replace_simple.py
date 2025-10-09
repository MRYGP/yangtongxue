import glob, os

def replace_uniform():
    files = glob.glob('copies/*.md')
    
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 简单替换，避免复杂正则表达式
            # 统一箭头
            content = content.replace('S4->S1->S0', 'S4→S1→S0')
            content = content.replace('S4→S1->S0', 'S4→S1→S0')
            content = content.replace('S4->S1→S0', 'S4→S1→S0')
            content = content.replace('S4->S1', 'S4→S1')
            
            # 统一范围
            content = content.replace('50-70%', '50–70%')
            content = content.replace('50–70%', '50–70%')
            content = content.replace('4-8 weeks', '4–8 weeks')
            content = content.replace('4–8 weeks', '4–8 weeks')
            
            # 引号统一
            content = content.replace('"', '"').replace('"', '"')
            content = content.replace(''', "'").replace(''', "'")
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Processed {file}")
            
        except Exception as e:
            print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    replace_uniform()
    print("Replacement completed")
