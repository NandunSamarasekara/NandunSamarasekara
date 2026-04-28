# ── CONFIG (edit only this section) ──────────────────────────────────────────
PROFILE = {
    "name":      "Nandun Samarasekara",
    "role":      "Data Science Undergraduate + ML Engineer",
    "research":  "AI × EEG × Mindfulness for university students",
    "location":  "Sri Lanka 🇱🇰",
    "side_quest": "Landscape Photographer",
    "available": "internships · freelance · open source collabs",
    "philosophy": "Building AI that listens to the brain",
    "github":    "NandunSamarasekara",
    "linkedin":  "nandun-samarasekara-5564162b8",
    "medium":    "nandunneelaka",
    "email":     "nandunneelaka@gmail.com",
    "repos":     ["REPO_NAME_1", "REPO_NAME_2", "REPO_NAME_3", "REPO_NAME_4"],
}

THEME = {
    "bg":         "0d1117",
    "accent":     "00d9ff",
    "text":       "c9d1d9",
    "fire":       "ff6b6b",
    "dark_grad":  "0:0f0f23,50:1a1a3e,100:16213e",
    "light_grad": "0:e0e7ff,50:c7d2fe,100:a5b4fc",
}

SKILLS = {
    "💻 Languages": [
        ("Python",      "3776AB", "python"),
        ("JavaScript",  "F7DF1E", "javascript"),
        ("Java",        "ED8B00", "openjdk"),
    ],
    "🤖 ML & Data": [
        ("TensorFlow",  "FF6F00", "tensorflow"),
        ("Pandas",      "150458", "pandas"),
        ("scikit-learn","F7931E", "scikit-learn"),
        ("NumPy",       "013243", "numpy"),
    ],
    "🌐 Web & Infra": [
        ("React",       "20232A", "react"),
        ("Node.js",     "339933", "node.js"),
        ("Express",     "000000", "express"),
        ("Tailwind",    "06B6D4", "tailwindcss"),
        ("Docker",      "2496ED", "docker"),
    ],
    "🗄️ Databases & Tools": [
        ("PostgreSQL",  "316192", "postgresql"),
        ("MySQL",       "4479A1", "mysql"),
        ("Git",         "F05032", "git"),
        ("Linux",       "FCC624", "linux"),
        ("VS Code",     "007ACC", "visual-studio-code"),
    ],
}

# ── BUILDERS ─────────────────────────────────────────────────────────────────
gh  = PROFILE["github"]
bg  = THEME["bg"]
acc = THEME["accent"]
txt = THEME["text"]


def badge(label, color, logo, logo_color="white"):
    safe = label.replace("-", "--").replace(" ", "%20")
    return (f"![{label}](https://img.shields.io/badge/{safe}-{color}"
            f"?style=for-the-badge&logo={logo}&logoColor={logo_color}&labelColor={bg})")


def skill_section(title, items):
    badges = "\n".join(badge(n, c, l) for n, c, l in items)
    return f"### {title}\n{badges}\n"


def pin_card(repo):
    url = (f"https://github-readme-stats.vercel.app/api/pin/?username={gh}&repo={repo}"
           f"&theme=tokyonight&hide_border=true&title_color={acc}&icon_color={acc}"
           f"&text_color={txt}&bg_color={bg}&border_radius=12")
    return f'<a href="https://github.com/{gh}"><img width="49%" src="{url}"/></a>'


def stats_url(endpoint, extra=""):
    base = (f"https://github-readme-stats.vercel.app/api/{endpoint}?username={gh}"
            f"&theme=tokyonight&hide_border=true&title_color={acc}&icon_color={acc}"
            f"&text_color={txt}&bg_color={bg}&border_radius=12")
    return base + extra


def capsule(text, desc="", grad=None, font_color=None):
    grad = grad or THEME["dark_grad"]
    fc   = font_color or acc
    url  = (f"https://capsule-render.vercel.app/api?type=venom&color={grad}"
            f"&height=200&section=header&text={text}&fontSize=50"
            f"&fontColor={fc}&animation=twinkling&fontAlignY=35")
    if desc:
        url += f"&desc={desc}&descSize=20&descAlignY=55&descAlign=50"
    return url


# ── ASSEMBLE ─────────────────────────────────────────────────────────────────
p = PROFILE

skills_md = "\n".join(skill_section(t, items) for t, items in SKILLS.items())

pins_md = "\n\n".join(
    f'<div align="center">\n  {pin_card(p["repos"][i])}  {pin_card(p["repos"][i+1])}\n</div>'
    for i in range(0, len(p["repos"]), 2)
)

header_text = "Ayubowan+🙏"
header_desc = f"I'm+{p['name'].replace(' ', '+')}"

README = f'''<!-- DARK/LIGHT MODE AWARE HEADER -->
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="{capsule(header_text, header_desc, grad=THEME['dark_grad'],  font_color=acc)}"/>
  <source media="(prefers-color-scheme: light)" srcset="{capsule(header_text, header_desc, grad=THEME['light_grad'], font_color='1e3a8a')}"/>
  <img src="{capsule(header_text, header_desc, grad=THEME['dark_grad'], font_color=acc)}"/>
</picture>

<!-- TYPING INTRO -->
<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=2800&pause=800&color={acc}&center=true&vCenter=true&width=650&lines=Data+Science+Undergraduate;ML+Engineer+from+Sri+Lanka+🇱🇰;Building+AI+that+listens+to+the+brain+🧠;Landscape+Photographer+between+commits+📸;Open+to+Internships+%26+Freelance+💼)](https://git.io/typing-svg)

</div>

<!-- STATUS BADGES -->
<div align="center">

[![Status](https://img.shields.io/badge/🟢-Open%20to%20Work-%2300C853?style=for-the-badge&labelColor={bg})](https://www.linkedin.com/in/{p['linkedin']})
&nbsp;
[![Profile Views](https://komarev.com/ghpvc/?username={gh}&label=👀%20Profile%20Views&color={acc}&style=for-the-badge&labelColor={bg})](https://github.com/{gh})
&nbsp;
[![GitHub Followers](https://img.shields.io/github/followers/{gh}?label=Followers&style=for-the-badge&color={acc}&labelColor={bg}&logo=github)](https://github.com/{gh})

</div>

<br/>

---

## 🧠 `$ whoami`

```yaml
🧑‍💻  name        : {p['name']}
🎓  role        : {p['role']}
🧠  research    : {p['research']}
📍  location    : {p['location']}
📸  side_quest  : {p['side_quest']}
🤝  available   : {p['available']}
💡  philosophy  : "{p['philosophy']}"
```

---

## 🛠️ Tech Arsenal

<div align="center">

{skills_md}
</div>

---

## 📊 GitHub Analytics

<div align="center">

  <img height="180em" src="{stats_url('', '&show_icons=true&include_all_commits=true&count_private=true')}"/>
  <img height="180em" src="{stats_url('top-langs', '&layout=compact&langs_count=8')}"/>

  <img width="90%" src="https://github-readme-streak-stats.herokuapp.com/?user={gh}&theme=tokyonight&hide_border=true&stroke={acc}&ring={acc}&fire={THEME['fire']}&currStreakLabel={acc}&sideLabels={txt}&background={bg}&border_radius=12"/>

  <img width="95%" src="https://github-readme-activity-graph.vercel.app/graph?username={gh}&theme=tokyo-night&hide_border=true&bg_color={bg}&color={acc}&line={acc}&point=ffffff&area=true&area_color={acc}&radius=12"/>

</div>

---

## 🏆 GitHub Trophies

<div align="center">

[![trophy](https://github-profile-trophy.vercel.app/?username={gh}&theme=tokyonight&no-frame=true&no-bg=true&margin-w=4&row=1&column=7)](https://github.com/ryo-ma/github-profile-trophy)

</div>

---

## 📌 Pinned Projects

{pins_md}

> 💡 **Replace `REPO_NAME_1`, `REPO_NAME_2`, etc. with your actual repository names!**

---

## ⏱️ WakaTime Coding Stats

<div align="center">

  <img width="60%" src="{stats_url('wakatime', '&layout=compact')}"/>

</div>

> 💡 **Sign up at [wakatime.com](https://wakatime.com) and install the plugin in your IDE to see your real coding stats!**

---

## ✍️ Latest from Medium

<div align="center">

📖 I write deep-dives on **ML, Data Science & Neuro-AI** on [Medium →](https://medium.com/@{p['medium']})

</div>

---

## 🤝 Let\'s Connect & Build

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-%230A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor={bg})](https://www.linkedin.com/in/{p['linkedin']})
[![Medium](https://img.shields.io/badge/Medium-Read-%23000000?style=for-the-badge&logo=medium&logoColor=white&labelColor={bg})](https://medium.com/@{p['medium']})
[![Gmail](https://img.shields.io/badge/Gmail-Email%20Me-%23EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor={bg})](mailto:{p['email']})

</div>

<br/>

<!-- FOOTER -->
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://capsule-render.vercel.app/api?type=waving&color={THEME['dark_grad']}&height=120&section=footer&animation=fadeIn"/>
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color={THEME['light_grad']}&height=120&section=footer&animation=fadeIn"/>
  <img src="https://capsule-render.vercel.app/api?type=waving&color={THEME['dark_grad']}&height=120&section=footer&animation=fadeIn"/>
</picture>
'''

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(README)

print(f"README.md saved! ({len(README):,} chars)")
