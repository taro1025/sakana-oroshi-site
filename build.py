"""さかなおろしの公開ページ（ja と en）を作る。  python3 build.py

アプリのアイコンは ~/sakana-oroshi/art/icon-1024.png から favicon などを作る。
App Store に並んだら APP_ID を入れて作り直す（トップの MobileApplication とボタンに App Store の URL が入る）。
"""
import json
import os

from PIL import Image

BASE = "https://taro1025.github.io/sakana-oroshi-site/"
APP_ID = ""
MAIL = "rintaro.sakino@process-craft-ai.com"
ICON = os.path.expanduser("~/sakana-oroshi/art/icon-1024.png")
UPDATED = {"ja": "2026年11月23日", "en": "November 23, 2026"}

T = {
    "ja": {"name": "さかなおろし", "full": "さかなおろし - 声で進む魚のさばき方", "home": "トップ", "privacy": "プライバシーポリシー",
           "terms": "利用規約", "support": "サポート", "lang": "English", "updated": "最終更新"},
    "en": {"name": "Oroshi", "full": "Oroshi: Hands-Free Fish Prep", "home": "Home", "privacy": "Privacy Policy",
           "terms": "Terms of Use", "support": "Support", "lang": "日本語", "updated": "Last updated"},
}


def store_url(lang):
    return f"https://apps.apple.com/{'jp' if lang == 'ja' else 'us'}/app/id{APP_ID}" if APP_ID else ""


def head(lang, page, title, desc):
    t = T[lang]
    url = BASE + ("" if lang == "ja" else "en/") + ("" if page == "index" else f"{page}.html")
    up = "" if lang == "ja" else "../"
    ld = json_ld(lang, url) if page == "index" else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ja" href="{BASE}{'' if page == 'index' else page + '.html'}">
<link rel="alternate" hreflang="en" href="{BASE}en/{'' if page == 'index' else page + '.html'}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{t['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}icon-512.png">
{f'<meta name="apple-itunes-app" content="app-id={APP_ID}">' if APP_ID else ''}
<link rel="icon" href="{up}favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="192x192" href="{up}icon-192.png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<link rel="stylesheet" href="{up}style.css">
{ld}
</head>
<body>
<header><a class="brand" href="{up}{'' if lang == 'ja' else 'en/'}"><img src="{up}icon-192.png" alt="" width="40" height="40">{t['name']}</a>
<a class="lang" href="{up}{'en/' if lang == 'ja' else ''}{'' if page == 'index' else page + '.html'}">{t['lang']}</a></header>
<main>
"""


def json_ld(lang, url):
    app = {"@type": "MobileApplication", "name": T[lang]["full"], "operatingSystem": "iOS",
           "applicationCategory": "LifestyleApplication", "url": store_url(lang) or url,
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "JPY" if lang == "ja" else "USD"}}
    site = {"@type": "WebSite", "@id": BASE + "#website", "name": T["ja"]["name"],
            "alternateName": ["Sakana Oroshi", "Oroshi", "さかなおろし 声で進む魚のさばき方"], "url": BASE, "inLanguage": lang}
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [site, app]},
                                                               ensure_ascii=False) + "</script>"


def foot(lang):
    t = T[lang]
    up = "" if lang == "ja" else "../"
    pre = up + ("" if lang == "ja" else "en/")
    return f"""</main>
<footer><nav><a href="{pre}">{t['home']}</a><a href="{pre}privacy.html">{t['privacy']}</a><a href="{pre}terms.html">{t['terms']}</a><a href="{pre}support.html">{t['support']}</a></nav>
<p>© 2026 Process Craft AI</p></footer>
</body>
</html>
"""


def write(lang, page, title, desc, body):
    path = page + ".html" if lang == "ja" else f"en/{page}.html"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(head(lang, page, title, desc) + body + foot(lang))


def icons():
    im = Image.open(ICON).convert("RGB")
    im.resize((180, 180), Image.LANCZOS).save("apple-touch-icon.png")
    im.resize((192, 192), Image.LANCZOS).save("icon-192.png")
    im.resize((512, 512), Image.LANCZOS).save("icon-512.png")
    im.save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])


def sitemap():
    pages = ["", "privacy.html", "terms.html", "support.html"]
    urls = [BASE + p for p in pages] + [BASE + "en/" + p for p in pages]
    with open("sitemap.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.write("".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    with open("robots.txt", "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")


if __name__ == "__main__":
    import pages
    icons()
    for lang in ("ja", "en"):
        for page, (title, desc, body) in pages.PAGES[lang].items():
            write(lang, page, title, desc, body.format(mail=MAIL, updated=UPDATED[lang], store=store_url(lang)))
    sitemap()
    open(".nojekyll", "w").close()
    print("ok")
