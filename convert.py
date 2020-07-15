import os
from pathlib import Path


for path in Path('.').rglob('*.html'):
    if path.parts[0] != "netcat_files":
        old_path = str(path) + ".old"
        os.rename(path, old_path)
        source = open(old_path, encoding="windows-1251")
        target = open(path, "w", encoding="utf-8")
        content = source.read()
        content = content.replace("charset=windows-1251", "charset=utf-8")
        target.write(content)
        os.remove(old_path)
