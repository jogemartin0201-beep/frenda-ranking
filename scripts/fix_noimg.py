import re

html_file = "index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the NOIMG IDs to inherit from older seasons if available
def replace_noimg(match):
    full_str = match.group(0)
    # Extract searchName
    name_match = re.search(r'searchName:\s*"([^"]+)"', full_str)
    if not name_match: return full_str
    
    search_name = name_match.group(1)
    
    # Find all IMG_ ids for this searchName in the whole HTML
    img_matches = re.findall(r'{[^}]*id:\s*"(IMG_\d+)"[^}]*searchName:\s*"([^"]+)"', html)
    
    fallback_id = None
    for im_id, s_name in img_matches:
        if s_name == search_name:
            fallback_id = im_id
            break
            
    if fallback_id:
        return re.sub(r'id:\s*"NOIMG_\d+"', f'id: "{fallback_id}"', full_str)
    
    return full_str

new_html = re.sub(r'{[^}]*id:\s*"NOIMG_\d+"[^}]*}', replace_noimg, html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Fixed NOIMG placeholders to inherit photos from older seasons.")
