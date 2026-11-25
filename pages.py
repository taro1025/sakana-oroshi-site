"""ページの本文（ja・en）。{mail} {updated} {store} を build.py が埋める。"""

INDEX_JA = """<section class="hero">
<img src="icon-512.png" alt="さかなおろしのアイコン" width="120" height="120">
<h1>さかなおろし</h1>
<p class="sub">声で進む魚のさばき方</p>
<p>魚を前に、まな板の横に置いておく手順書です。魚の種類を選ぶと、おろし方が一歩ずつ図で出ます。魚をさわった手のまま「つぎ」と言えば次の手順へ。画面に触らなくていいので、動画を止めて手を洗う手間がありません。</p>
<p><a class="cta" href="{store}">App Store でダウンロード</a></p>
</section>
<section>
<h2>できること</h2>
<ul>
<li><b>声で進む</b> — 「つぎ」「もどる」「もう一回」を iPhone の中だけで聞き取ります。音声は保存も送信もしません。</li>
<li><b>魚ごとの手順</b> — アジのぜいご、サバの血合い骨、カレイの五枚おろし、サンマの大名おろし、カワハギの皮むき、イカのわた抜きまで。どこに刃を入れ、どちらへ引くかを図の線と矢印で示します。</li>
<li><b>気をつけるところで止まる</b> — アニサキスを目で探すところ、カサゴのとげ、イカの墨など、その魚で気をつける手順の前に一枚はさみます。</li>
<li><b>左利きにも</b> — 図を左右反転して、左手で包丁を持つ向きにできます。</li>
</ul>
<h2>料金</h2>
<p>アジ・サバ・イワシは無料で最後まで使えます。ほかの14種と刺身の切り分けは、買い切り980円で解放されます。サブスクリプションではありません。広告はありません。</p>
<h2>収録している魚</h2>
<p>アジ・サバ・イワシ・鯛・ブリ／ハマチ・サケ・カサゴ／メバル・カワハギ・太刀魚・サンマ・シロギス・ハゼ・カレイ・ヒラメ・スルメイカ・マダコ・刺身の切り分け（平造り・そぎ造り）</p>
</section>
"""

INDEX_EN = """<section class="hero">
<img src="../icon-512.png" alt="Oroshi app icon" width="120" height="120">
<h1>Oroshi</h1>
<p class="sub">Hands-free fish prep, step by step</p>
<p>A step-by-step guide that sits next to your cutting board. Pick the fish and Oroshi shows how to break it down, one clear diagram at a time. Your hands are wet and smell of fish, so just say "next" to move on.</p>
<p><a class="cta" href="{store}">Download on the App Store</a></p>
</section>
<section>
<h2>Features</h2>
<ul>
<li><b>Voice control</b> — Say "next", "back" or "again". Recognition runs entirely on your iPhone; nothing is recorded or sent.</li>
<li><b>Fish by fish</b> — 17 fish and techniques, from horse mackerel to flounder, squid, octopus and sashimi slicing. Diagrams show where the blade goes and which way to pull.</li>
<li><b>Safety stops</b> — A short note appears before the steps that matter: checking for parasites, spiny fins, squid ink.</li>
<li><b>Left-handed mode</b> — Mirrors every diagram.</li>
</ul>
<h2>Pricing</h2>
<p>Horse mackerel, mackerel and sardine are free forever. Unlock everything else with a one-time purchase. No ads, no subscription.</p>
</section>
"""

PRIVACY_JA = """<h1>プライバシーポリシー</h1>
<p class="date">最終更新: {updated}</p>
<p>Process Craft AI（以下「私たち」）は、iPhone アプリ「さかなおろし」（以下「本アプリ」）での情報の扱いを次のとおり定めます。</p>
<h2>集める情報</h2>
<p>本アプリは、利用者の個人情報・端末の識別子・利用状況を集めません。アカウントの登録はなく、広告や計測のための外部のサービスも使っていません。</p>
<h2>マイクと音声認識</h2>
<p>手順を声で進める機能のために、マイクと音声認識を使います。聞き取りは Apple の音声認識を iPhone の中だけで動かして行い（端末内での認識）、音声や聞き取った文を保存・送信しません。マイクを許可しなくても、画面を押して手順を進められます。</p>
<h2>端末に保存するもの</h2>
<p>はじめの案内での答え（魚の入手先・経験・よく手にする魚）、設定（声・読み上げ・左利き）、最後までさばいた魚の印を、iPhone の中だけに保存します。私たちのサーバーには送りません。アプリを削除すると消えます。</p>
<h2>購入</h2>
<p>買い切りの購入は Apple の App Store を通じて行われます。支払いの情報は Apple が扱い、私たちは受け取りません。</p>
<h2>お子さまの利用</h2>
<p>本アプリは包丁を使う調理の手順を扱います。お子さまが使うときは、保護者の方がそばで見守ってください。</p>
<h2>変更</h2>
<p>このポリシーを変えるときは、このページで知らせます。</p>
<h2>お問い合わせ</h2>
<p>Process Craft AI　<a href="mailto:{mail}">{mail}</a></p>
"""

PRIVACY_EN = """<h1>Privacy Policy</h1>
<p class="date">Last updated: {updated}</p>
<p>This policy explains how Process Craft AI ("we") handles information in the iPhone app Oroshi (the "App").</p>
<h2>Information we collect</h2>
<p>The App does not collect personal information, device identifiers or usage data. There are no accounts, and no third-party advertising or analytics services.</p>
<h2>Microphone and speech recognition</h2>
<p>To let you move through the steps by voice, the App uses the microphone and Apple's speech recognition running on your iPhone (on-device recognition). Audio and transcripts are never saved or sent. You can always tap the screen instead.</p>
<h2>Data stored on your device</h2>
<p>Your answers in the intro, your settings and which fish you have finished are stored only on your iPhone. Nothing is sent to our servers. Deleting the App deletes this data.</p>
<h2>Purchases</h2>
<p>The one-time purchase is handled by Apple through the App Store. We do not receive your payment information.</p>
<h2>Children</h2>
<p>The App describes cooking steps that use knives. Children should use it under adult supervision.</p>
<h2>Changes</h2>
<p>We will post any changes to this policy on this page.</p>
<h2>Contact</h2>
<p>Process Craft AI — <a href="mailto:{mail}">{mail}</a></p>
"""

TERMS_JA = """<h1>利用規約</h1>
<p class="date">最終更新: {updated}</p>
<p>この規約は、Process Craft AI（以下「私たち」）が提供する iPhone アプリ「さかなおろし」（以下「本アプリ」）の利用条件を定めます。本アプリを使うことで、この規約に同意したものとみなします。</p>
<h2>1. 本アプリの内容</h2>
<p>本アプリは、魚介類の下ごしらえとおろし方の一般的な手順を図と文で示すものです。魚の大きさ・鮮度・道具によって、実際の作業は手順と異なることがあります。</p>
<h2>2. 安全について</h2>
<p>包丁・キッチンばさみ・熱湯は、利用者自身の責任で安全に扱ってください。本アプリに載せた寄生虫（アニサキスなど）や食中毒についての注意は、厚生労働省の案内に沿った一般的な内容であり、食中毒を防ぐことを保証するものではありません。体調に異変があれば医療機関を受診してください。</p>
<h2>3. 購入</h2>
<p>有料の内容は App Store での買い切り（1回のお支払い）で解放されます。自動で更新されることはありません。返金は Apple の定めに従います。機種変更などのときは「購入を復元」で同じ Apple アカウントの購入を戻せます。</p>
<h2>4. 禁止すること</h2>
<p>本アプリの図・文の無断での転載・再配布、本アプリの解析・改変、法令や公序良俗に反する利用を禁止します。</p>
<h2>5. 権利</h2>
<p>本アプリの図・文・プログラムの権利は私たちに帰属します。</p>
<h2>6. 免責</h2>
<p>私たちは、本アプリの利用によって生じたけが・損害について、私たちの故意または重大な過失による場合を除き、責任を負いません。</p>
<h2>7. 変更と準拠法</h2>
<p>この規約は必要に応じて変更し、このページで知らせます。この規約は日本法に従います。</p>
<h2>お問い合わせ</h2>
<p>Process Craft AI　<a href="mailto:{mail}">{mail}</a></p>
"""

TERMS_EN = """<h1>Terms of Use</h1>
<p class="date">Last updated: {updated}</p>
<p>These terms govern your use of the iPhone app Oroshi (the "App") provided by Process Craft AI ("we"). By using the App you agree to these terms.</p>
<h2>1. What the App is</h2>
<p>The App shows general steps for cleaning and filleting fish and seafood with diagrams and text. Real fish vary in size, freshness and tools, so your work may differ from the steps.</p>
<h2>2. Safety</h2>
<p>You are responsible for handling knives, shears and boiling water safely. Notes about parasites (such as anisakis) and food poisoning are general information based on guidance from Japan's Ministry of Health, Labour and Welfare and do not guarantee food safety. See a doctor if you feel unwell.</p>
<h2>3. Purchases</h2>
<p>Paid content is unlocked with a one-time App Store purchase. It does not renew. Refunds follow Apple's policies. Use "Restore Purchase" to recover a purchase made with the same Apple Account.</p>
<h2>4. Prohibited use</h2>
<p>You may not copy or redistribute the App's diagrams or text, reverse-engineer or modify the App, or use it unlawfully.</p>
<h2>5. Ownership</h2>
<p>All rights in the App's diagrams, text and software belong to us.</p>
<h2>6. Disclaimer</h2>
<p>Except in cases of our intent or gross negligence, we are not liable for injury or loss arising from use of the App.</p>
<h2>7. Changes and governing law</h2>
<p>We may update these terms and will post changes on this page. These terms are governed by the laws of Japan.</p>
<h2>Contact</h2>
<p>Process Craft AI — <a href="mailto:{mail}">{mail}</a></p>
"""

SUPPORT_JA = """<h1>サポート</h1>
<h2>よくある質問</h2>
<h3>「つぎ」と言っても進みません</h3>
<p>設定アプリ →「さかなおろし」で、マイクと音声認識が許可されているか確かめてください。手順の画面の上に「「つぎ」「もどる」「もう一回」で進みます」と出ていれば聞き取り中です。換気扇や水の音が大きいときは、少し iPhone に近づいて言ってみてください。聞き取りは iPhone の中で行うため、この機能に対応していない機種では、画面のどこかを押して進みます。</p>
<h3>機種を変えたら有料の魚が使えません</h3>
<p>設定（右上の歯車）→「購入を復元」を押してください。購入したときと同じ Apple アカウントでサインインしている必要があります。</p>
<h3>左利きです</h3>
<p>設定 →「左利き（図を左右反転）」をオンにすると、すべての図が左右反転します。</p>
<h3>どんな包丁が要りますか</h3>
<p>手順ごとに、はじめに使う道具を出しています。出刃包丁が無ければ、よく切れる三徳包丁で多くの魚をおろせます。鯛の頭を割るときだけは出刃包丁を使ってください。</p>
<h2>お問い合わせ</h2>
<p>不具合・ご要望（足してほしい魚など）は、メールでお知らせください。iPhone の機種と iOS のバージョンを書いていただけると助かります。</p>
<p><a href="mailto:{mail}?subject=さかなおろし">{mail}</a></p>
"""

SUPPORT_EN = """<h1>Support</h1>
<h2>FAQ</h2>
<h3>Saying "next" does nothing</h3>
<p>Open Settings → Oroshi and make sure Microphone and Speech Recognition are allowed. While listening, the steps screen shows "Say next, back or again". Recognition runs on your iPhone; on models that don't support it, tap anywhere on the screen to move on.</p>
<h3>I changed phones and lost the paid fish</h3>
<p>Go to Settings (the gear) → Restore Purchase, signed in with the same Apple Account you bought with.</p>
<h3>I'm left-handed</h3>
<p>Turn on Settings → Left-handed to mirror every diagram.</p>
<h2>Contact</h2>
<p>Bug reports and requests (including fish you'd like added) are welcome. Please include your iPhone model and iOS version.</p>
<p><a href="mailto:{mail}?subject=Oroshi">{mail}</a></p>
"""

PAGES = {
    "ja": {
        "index": ("さかなおろし - 声で進む魚のさばき方｜三枚おろしから五枚おろしまで",
                  "さかなおろしは、魚種ごとのさばき方を一歩ずつ図で示し、濡れた手のまま「つぎ」と言えば次の手順へ進む iPhone アプリです。アジ・サバ・イワシは無料。", INDEX_JA),
        "privacy": ("さかなおろし｜プライバシーポリシー", "さかなおろしのプライバシーポリシー。個人情報を集めず、声は iPhone の中だけで聞き取ります。", PRIVACY_JA),
        "terms": ("さかなおろし｜利用規約", "さかなおろしの利用規約。", TERMS_JA),
        "support": ("さかなおろし｜サポート", "さかなおろしのよくある質問とお問い合わせ先。", SUPPORT_JA),
    },
    "en": {
        "index": ("Oroshi: Hands-Free Fish Prep | Step-by-step fish filleting",
                  "Oroshi shows how to clean and fillet 17 kinds of fish and seafood, one diagram at a time. Say “next” to move on, hands-free.", INDEX_EN),
        "privacy": ("Oroshi | Privacy Policy", "Oroshi privacy policy. No data collection; voice is processed only on your iPhone.", PRIVACY_EN),
        "terms": ("Oroshi | Terms of Use", "Oroshi terms of use.", TERMS_EN),
        "support": ("Oroshi | Support", "Oroshi FAQ and contact.", SUPPORT_EN),
    },
}
