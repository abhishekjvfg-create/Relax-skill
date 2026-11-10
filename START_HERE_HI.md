# Aurelia Studio — kaise install aur use karein

## 1. ZIP extract karein
Python 3.10 ya newer installed hona chahiye. Download ki hui ZIP extract karein. Terminal us folder mein kholein jahan `aurelia-studio` folder hai.

macOS / Linux:
```sh
python3 aurelia-studio/install.py --target generic
```
Windows:
```powershell
py -3 aurelia-studio/install.py --target generic
```
Agar aapke system par command `python` hai to `python3` ki jagah `python` use karein. Installer Python ki standard library use karta hai; pip/npm ki zaroorat nahi.

Antigravity project folder mein:
```sh
python3 aurelia-studio/install.py --target antigravity
```
Is preset ka destination `.agent/skills/aurelia-studio` hai. Agar aapke host/version mein skill folder alag hai, `--dest /actual/skills/path` dein. Installer sirf files copy karta hai, host ki capabilities change nahi karta. `--dry-run` se pehle destination check kar sakte hain.

## 2. Library dekhein
`aurelia-studio/index.html` browser mein kholein. Isse designs, components, animations, fonts aur agent logos browse kar sakte hain. Internet ki zaroorat nahi. Fonts bhi local files hain.

## 3. AI host mein use karein
AI tool ko installed `SKILL.md` aur `agents/registry.json` read karne dein. `PROMPT.txt` ka content paste karein aur apna project brief likhein.

Chhota prompt:
```text
Use Aurelia Studio. Read SKILL.md and the six agents/*.md files.
Mera project: [apna app/website brief likhein].
Native subagents available hon to six discovery roles parallel chalao; warna
clearly disclose sequential single-model mode. Authorized models hi use karo.
Real backend, APIs, persistence aur error states implement karo. Missing keys
ko blocked dikhao, fake success mat dikhao. Actual build/browser/API tests
run karke evidence do; bugs fix karke tests dobara run karo.
```

## 4. Six specialist roles
1. **ATLAS** — 3D structure/modeling; Three.js, Blender, Unity, Godot guidance.
2. **VELVET** — clean premium UI, motion aur responsive interaction.
3. **CHROMA** — fonts, colors, typography aur suitable animation selection.
4. **LUMEN** — lighting, polish aur authorized reference matching.
5. **FORGE** — backend, integrations aur visual/code mistakes ki repair.
6. **SENTINEL** — independent QA, bugs, security aur fake functionality audit.

Har role ka original SVG logo `logos/` mein hai. Ye bundled LLM models nahi; ye instructions aur workflow roles hain. Inka actual skill level aapke selected model, host ke tools aur verification par depend karta hai.

## 5. Sach mein parallel API run
Optional Python runner six consultation API calls ek saath karta hai; uske baad Forge implementation aur Sentinel static audit karta hai. Total maximum 8 requests per successful run. Iske liye apna authorized provider endpoint, actual model IDs, API key aur cost consent chahiye.

`models.example.json` ki private copy banakar base URL aur six model IDs configure karein. API key environment variable `AURELIA_API_KEY` mein securely set karein, file mein nahi. Exact steps `README.md` mein hain.

Offline plan (free, koi API request nahi):
```sh
python3 aurelia-studio/scripts/runner.py --plan
```
Configured paid run:
```sh
python3 aurelia-studio/scripts/runner.py --config /path/to/models.local.json --brief aurelia-studio/templates/brief.txt --out ./aurelia-runs --confirm-api-cost
```
Runner generated source deta hai lekin us code ko execute, install ya deploy nahi karta. API-only review actual browser testing nahi hai. Isliye result `GENERATED_UNVERIFIED` aur `release_ready=false` rahega, chahe model khud pass bole. Host mein actual tests ke baad hi release karein.

## Important sachchai
- 1,080 designs = 18 domains × 12 layouts × 5 themes. Ye recipes hain, 1,080 bespoke complete websites nahi.
- 520 components = 52 semantic patterns × 10 themes. Integration notes mein demo/unconnected functionality clearly likhi hai.
- 160 real font families aur licenses included; normal 400 weight only, mostly Latin subsets. Hindi ke liye correct Devanagari subset separately choose/fetch karein.
- 64 CSS animation recipes with reduced-motion fallback; browser support vary karega.
- Kisi bhi terminal ya LLM mein ek universal magic install standard nahi hai. Arena naam ke products/model catalogs alag ho sakte hain.
- Skill kisi tool ko paid models, credits, engine installation ya permissions nahi de sakti.
- Blender/Unity/Godot ke actual execution ke liye installed engines chahiye.
- 80–95% exact copy ya bug-free result ki guarantee nahi. Authorized references se structure/style analyze karke original/licensed assets use karein.
- Real AI, payment, email, auth aur storage ke liye real services, credentials aur tests chahiye.

## Verification
19 automated tests inventory, installer, safe file writing aur local mock API ke through parallel runner behavior check karte hain. Browser test four library pages ko 360/768/1440 widths par aur selected real interactions/fonts/motion ko check karta hai. Yeh skill library ka testing hai, kisi future generated app ka production certification nahi. `TEST_REPORT.json` mein actual package-creation evidence diya hai.
