---
theme: /home/aruncs/Desktop/Projects/slides/styles/theme.json
author: Arun CS
---

# Slide One


```bash
~~~bash
toilet -f smblock 'Python'
~~~
```

```python
import time
import  sys
r = '\033[1;31m'
g= '\033[1;32m'


def write(in_text):
 for char in in_text:
  time.sleep(1)
  sys.stdout.write(char)
  sys.stdout.flush()
write(f"{g}[+]{r} St")
print("\t")
```

---


### Output
```bash
cat ./Git_slides.md
```
