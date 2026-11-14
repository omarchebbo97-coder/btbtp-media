# Builds guides/src/food_after_transplant_ar.html (lead magnet: food after transplant, Arabic only).
# Same design as post_transplant_ar.html (blood test guide v2): its CSS is reused as is.
# Content source: Hôtel-Dieu de France nutrition department handouts given to Omar after his transplant,
# copied as they are (Omar, 14 Nov 2026). Additions are marked in the HTML comments.
import os, re
D = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(D, "post_transplant_ar.html"), encoding="utf-8").read()
css = re.search(r"<style>(.*?)</style>", base, re.S).group(1)

css += """
.ok,.no{list-style:none;padding:0;margin:2px 0 0}
.ok li,.no li{position:relative;padding-right:22px;font-size:13.4px;line-height:1.75;margin:3px 0}
.ok li:before{content:"✓";position:absolute;right:0;top:0;color:#b08a3c;font-weight:600}
.no li:before{content:"✗";position:absolute;right:0;top:0;color:#c62828;font-weight:600}
.tag{display:inline-block;font-size:12px;font-weight:600;color:#fff;border-radius:7px;padding:2px 9px;margin-bottom:4px}
.tag.y{background:#1f2a44}.tag.n{background:#c62828}
.lat{direction:ltr;unicode-bidi:isolate}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
.grid .card{margin:0;text-align:center;padding:14px 8px}
.grid svg{width:58px;height:58px;display:block;margin:0 auto 6px}
.grid p{font-size:14px;font-weight:600;color:#1f2a44;line-height:1.5}
.hand{background:#fffbf0;border:1.5px dashed #b08a3c}
.hand p{font-size:15px}
.pills{display:flex;gap:8px}
.pills .range{flex:1}
.mine td{height:44px}
.mine td:first-child{width:42%;font-weight:600;color:#1f2a44}
"""

FOOT = '<div class="foot"><span>هذه لائحة مستشفاي. اسأل فريقك الطبي.</span><span class="h">@omar_organtransplants</span></div>'
AR = "٠١٢٣٤٥٦٧٨٩"
def n2(i): return "".join(AR[int(c)] for c in f"{i:02d}")

def page(img, num, title, body, pos="center 55%", h=None):
    hh = f";height:{h}" if h else ""
    ban = f'<div class="banner" style="background-image:url(img/{img});background-position:{pos}{hh}"></div>' if img else ""
    top = "" if img else ' style="margin-top:22px"'
    return f'<section class="page">\n {ban}\n <div class="num"{top}>{n2(num)}</div>\n <h1>{title}</h1>\n{body}\n {FOOT}\n</section>\n'

def lst(cls, items): return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def ok(items, title="المأكولات المسموحة"): return f'<div class="card"><span class="tag y">{title}</span>{lst("ok", items)}</div>'
def no(items, title="المأكولات الغير مسموحة"): return f'<div class="card"><span class="tag n">{title}</span>{lst("no", items)}</div>'
def omar(t): return f'<div class="omar"><p>«{t}»</p><div class="who">عمر</div></div>'

ICON = {
 "sep": '<svg viewBox="0 0 64 64"><path d="M10 22h36m0 0-9-9m9 9-9 9M54 42H18m0 0 9-9m-9 9 9 9" fill="none" stroke="#1f2a44" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "wash": '<svg viewBox="0 0 64 64"><path d="M12 20h22a8 8 0 0 1 8 8v6" fill="none" stroke="#1f2a44" stroke-width="5" stroke-linecap="round"/><path d="M22 12v8M16 12h12" stroke="#1f2a44" stroke-width="5" stroke-linecap="round"/><path d="M42 42c-3 5-5 7-5 10a5 5 0 0 0 10 0c0-3-2-5-5-10z" fill="#b08a3c"/></svg>',
 "hot": '<svg viewBox="0 0 64 64"><path d="M12 32h40v12a10 10 0 0 1-10 10H22a10 10 0 0 1-10-10z" fill="#1f2a44"/><path d="M8 34h4M52 34h4M22 28h20" stroke="#1f2a44" stroke-width="4" stroke-linecap="round"/><path d="M24 22c-3-4 3-6 0-10M32 22c-3-4 3-6 0-10M40 22c-3-4 3-6 0-10" fill="none" stroke="#b08a3c" stroke-width="3.5" stroke-linecap="round"/></svg>',
 "cold": '<svg viewBox="0 0 64 64"><g stroke="#1f2a44" stroke-width="4.5" stroke-linecap="round" fill="none"><path d="M32 8v48M11 20l42 24M11 44l42-24"/><path d="M26 12l6 6 6-6M26 52l6-6 6 6M12 28l8-2-2-8M52 36l-8 2 2 8M12 36l8 2-2 8M52 28l-8-2 2-8"/></g></svg>',
}

P = []

# 1 COVER
P.append('''<section class="page cover">
 <div class="img" style="background-image:url(img/food_ai03_jug.jpg);background-position:center 55%"></div>
 <div class="txt">
  <div class="k">دليل مجاني · بعد الزراعة</div>
  <h1>ماذا آكل بعد الزراعة؟</h1>
  <p>الطعام النظيف والمناعة: ما المسموح، ما الممنوع، وكيف تحفظ طعامك. الإرشادات التي أعطاني إياها قسم التغذية في المستشفى بعد الزراعة.</p>
  <div class="by" style="color:#9aa3b5;font-size:11px;margin-bottom:-8px">آخر تحديث: تشرين الثاني ٢٠٢٦</div>
  <div class="by">من عمر · زُرعت لي كلية أخي أمين في ١٣ حزيران ٢٠٢٤<br><bdi dir="ltr">@omar_organtransplants</bdi></div>
 </div>
</section>
''')

TOC = ["قبل أن تبدأ", "الطعام النظيف (المعقم) والمناعة", "بعد الزرع مباشرةً: بلا نيّ", "وسائل حفظ الطعام بطريقة سليمة",
       "بقايا الطعام والحليب", "الخبز والنشويات", "اللحوم والبيض", "الحليب ومشتقاته", "الفاكهة والعصير",
       "الخضار، الدهون والمكسرات", "الصلصات والتوابل، والحلويات", "السوائل والمشروب", "أسئلة لفريقك الطبي", "لائحتي أنا"]
rows = "".join(f'<p style="display:flex;gap:10px;border-bottom:1px solid #f0e8da;padding:5px 0"><span class="q" style="min-width:22px">{n2(i+1)}</span><span>{t}</span></p>' for i, t in enumerate(TOC))
P.append(f'<section class="page">\n <div class="num" style="margin-top:26px">المحتوى</div>\n <h1>في هذا الدليل</h1>\n <div class="card">{rows}</div>\n {FOOT}\n</section>\n')

NOTICE = '''<section class="page" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 34px">
 <div style="width:150px;height:150px;border-radius:50%;background:#c62828;color:#fff;font-size:120px;font-weight:600;line-height:150px;margin-bottom:34px">!</div>
 <p style="font-size:24px;line-height:1.75;font-weight:600;color:#1f2a44">كل مريض مختلف.<br>كل جسم مختلف.<br>كل فريق طبي مختلف.</p>
 <p style="font-size:19px;line-height:1.8;color:#2b2a33;margin-top:18px">تأكّد دائماً مع فريقك الطبي مما هو مناسب لك.</p>
 <p style="font-size:15px;line-height:1.8;color:#6b6878;margin-top:22px">هذا الدليل للمعلومات فقط، ومبنيّ على تجربتي كمريض. ليس نصيحة طبية.</p>
 ''' + FOOT + '\n</section>\n'
P.append(NOTICE)

# 01 START (Omar's line = his own stated facts)
b = '''<p class="lead">هذه الإرشادات أعطاني إياها قسم التغذية في مستشفى أوتيل ديو دو فرانس بعد الزراعة. أنقلها هنا كما هي. <span style="background:#c62828;color:#fff;font-weight:600;padding:1px 5px;border-radius:5px;box-decoration-break:clone;-webkit-box-decoration-break:clone">ليست بديلاً عن فريقك الطبي.</span></p>
''' + omar("بعد الزراعة: لا أكل نيّ أو مش مستوي منيح، لا جريب فروت، لا رمّان. وملح وسكر أقل، وبلا أكل مصنّع.") + '''
 <div class="card"><p><b>١. «النظيف» يعني المعقّم.</b> عنوان الورقة نفسها: «الطعام النظيف (المعقم) والمناعة».</p></div>
 <div class="card"><p><b>٢. لماذا؟</b> أدوية منع الرفض تُخفّض عمل جهاز المناعة، وهذا قد يزيد خطر الالتهابات الخطيرة. لذلك يهمّ أن يكون الطعام نظيفاً.</p></div>
 <div class="card"><p><b>٣. هذه لائحة مستشفاي.</b> لائحة فريقك الطبي قد تختلف، وقد تتغيّر مع الوقت بعد الزراعة.</p></div>
 <div class="card" style="background:#c62828"><p style="color:#fff"><b style="color:#fff">٤. غير متأكّد من طعام معيّن؟</b> اسأل فريقك الطبي قبل أن تأكله.</p></div>'''
P.append(page("food_newkidney_master.jpg", 1, "قبل أن تبدأ", b, "center 50%"))

# 02 FOUR RULES (verbatim labels)
cells = [("sep", "فصل المأكولات"), ("wash", "الغسل والتعقيم"), ("hot", "الحفاظ على حرارة المأكولات المطبوخة"), ("cold", "الحفاظ على برودة المأكولات المثلّجة")]
grid = '<div class="grid">' + "".join(f'<div class="card">{ICON[k]}<p>{t}</p></div>' for k, t in cells) + '</div>'
b = '<p class="lead">أربع قواعد على رأس الورقة. كل ما يأتي في هذا الدليل يعود إليها.</p>\n' + grid
P.append(page("food_intestines_master.jpg", 2, "الطعام النظيف (المعقم) والمناعة", b, "center 60%"))

# 03 RIGHT AFTER (box verbatim + handwritten note)
b = '''<div class="card"><p>بعد الزرع مباشرةً ينصح بتناول غذاء دون ني <bdi dir="ltr">"sans crudités"</bdi> ← أي يجب تفادي الخضار والفواكه النيّة وتناولها دائماً مسلوقة طازجة (خضار مطبوخة ساخنة جيّداً أو كومبوت فاكهة محفوظة في غلافات فرديّة)</p></div>
 <div class="card hand"><p class="small" style="font-size:11.5px;color:#8a7440">ملاحظة مكتوبة بخط اليد على ورقتي:</p><p>← لمدة ٦ أسابيع، من ثمّ يمكن تعقيم الخضار والفاكهة دون سلق</p></div>
 <div class="range"><span class="l">المدة على ورقتي</span><span class="v">٦ أسابيع</span></div>
 <div class="warn"><p>المدة قد تختلف عندك. اسأل فريقك الطبي متى تعود إلى الخضار والفاكهة النيّة.</p></div>'''
P.append(page("food_ai20_bed.jpg", 3, "بعد الزرع مباشرةً: بلا نيّ", b, "center 62%"))

# 04 STORAGE 1 (verbatim)
b = '<div class="card">' + lst("ok", [
 "اغسل الخضار والفواكه الطازجة.",
 "عقم الخضار والفاكهة بالدواء المطهر <u>نصف</u> ساعة قبل تقديمه أو طبخه.",
 "اشتري عدد البيض اللازم لمدة أسبوع أو أسبوعين فقط. لا تترك البيض النيء خارج البراد لأكثر من ساعتين. لا تغسل البيض قبل حفظه في البراد واحفظه في علبة خاصة مغلقة.",
 "احفظ الطعام في البراد أو الثلاجة مباشرةً بعد عملية التسوق فحرارة الطعام ترتفع بسرعة مما يساعد على تكاثر البكتيريا المؤذية.",
 "راقب حرارة البراد بواسطة ميزان حرارة خاص، من وقت إلى آخر. يجب أن تكون حرارته بين <bdi dir=\"ltr\">4°C</bdi> و <bdi dir=\"ltr\">5°C</bdi> وحرارة الثلاجة <bdi dir=\"ltr\">18°C</bdi> تحت الصفر.",
]) + '</div>\n <div class="pills"><div class="range"><span class="l">البراد</span><span class="v">4 – 5°C</span></div><div class="range"><span class="l">الثلاجة</span><span class="v">−18°C</span></div></div>'
P.append(page("food_e8_cup.jpg", 4, "وسائل حفظ الطعام بطريقة سليمة قبل تناولها", b, "center 58%", "2.5in"))

# 05 STORAGE 2 (verbatim)
b = '<p class="lead">تكملة اللائحة نفسها.</p><div class="card">' + lst("ok", [
 "سخن بقايا الطعام على درجة <bdi dir=\"ltr\">74 °C</bdi> في الفرن 5 دقائق قبل تقديمهم.",
 "( ملاحظة يمكن استعمال بقايا الطعام إذا تم حفظهم في البراد أو الثلاجة بغضون ساعة بعد تحضيرهم).",
 "لا تترك الطعام على الطاولة دون تغطيته.",
 "احفظ بواقي المأكولات في البراد أو في الثلاجة اذا اردت حفظها لمدة اطول",
 "اشتر الحليب المبستر أو المعقم وليس الحليب الطازج.",
]) + '</div>\n <div class="pills"><div class="range"><span class="l">تسخين البقايا</span><span class="v">74°C · 5 min</span></div><div class="range"><span class="l">إلى البراد خلال</span><span class="v">ساعة</span></div></div>'
P.append(page("food_h_end1.jpg", 5, "بقايا الطعام والحليب", b, "center 58%"))

# 06 BREAD
b = ok(["الخبز الطازج والمغلّف والذي لا يحتوي على فاكهة مجففة", "كورنفليكس دون فاكهة مجففة",
        "نشويات كالرز والبطاطا والمعكرونة والحبوب المطهوة جيداً والطازجة", "مناقيش طازجة وساخنة (بكميات قليلة).",
        "كروسان مغلّف مباشرةً بعد الخَبز (بكميات قليلة)"]) + no(["المأكولات التي تحتوي على فاكهة مجففة أو مكسرات", "الخميرة الغير مطبوخة"])
P.append(page("food_e9_build.jpg", 6, "الخبز والنشويات", b, "center 62%"))

# 07 MEAT + EGGS (Omar's line from his TT21 repost)
b = '<h2>اللحوم</h2>' + ok(["جميع أنواع اللحوم مطبوخة جيداً", "طون سردين معلب"]) + no(["اللحوم النيّة أو الغير مطبوخة جيداً", "مرتديلا، جانبون وغيرها من اللحوم المعلّبة", "اللحوم المدخّنة، السوشي"]) \
  + '<h2 style="margin-top:8px">البيض</h2>' + ok(["المطبوخ جيداً"]) + no(["البيض الني أو الغير المطبوخ أو البيض برشت", "المايونيز"]) \
  + omar("السوشي شطبتو من صحني بعد الزراعة.")
P.append(page("food_h_in2.jpg", 7, "اللحوم والبيض", b, "center 58%", "2.1in"))

# 08 DAIRY
b = ok(["حليب بودرة أو مبستر", "الأجبان البيضاء (القليلة الملح) المغلّفة و المبسترة. يجب الحرص على عدم تناول الجبنة أكثر من مرّة بعد فتح الغلاف.",
        "لبن ولبنة مبسترة", "البوظة المعلبة المصنوعة مع حليب مبستر"]) \
  + no(["الحليب الطازج الغير معقم، الأجبان الغير معقمة والأجبان التي تحتوي على أعشاب أو بهارات.",
        'الأجبان المخمّرة: <bdi dir="ltr">Camembert / Blue / Gorgonzola / Roquefort / Brie / cheese</bdi>', "البوظة غير المغلفة."])
P.append(page("food_e4_relief.jpg", 8, "الحليب ومشتقاته", b, "center 58%", "2.5in"))

# 09 FRUIT + JUICE (+ grapefruit: Omar's line from TT12 + MedlinePlus tacrolimus)
b = ok(["الفاكهة المعلّبة والمطبوخة (الكومبوت)", "الفاكهة المعقمة (يجب التعقيم حتّى الفاكهة ذات قشرة سميكة كالليمون...)", "العصير الطازج المصنوع من الفاكهة المعقمة"]) \
  + no(["العصير المعلّب، رغم أنّه نظيف ومعقم، لكنّه يحتوي على كميات كبيرة من السكر", "العصير في علب كبيرة والذي يتم السكب منه أكثر من مرة", "الفاكهة المجففة."]) \
  + '<div class="warn"><p><b>ليس على ورقة المستشفى، لكنّه مهمّ:</b> تجنّب الجريب فروت وعصيره مع التاكروليموس (البروغراف).</p></div>' \
  + omar("العصير الوحيد الممنوع عليّ بعد الزراعة: الجريب فروت. وبتجنّب الرمّان كمان.")
P.append(page("food_e7_hug.jpg", 9, "الفاكهة والعصير", b, "center 58%", "2.1in"))

# 10 VEG + FATS
b = '<h2>الخضار</h2>' + ok(["جميع الخضار المطبوخة والمعقّمة"]) + no(["الخضار الغير معقمة", "الكبيس"]) \
  + '<h2 style="margin-top:8px">الدهون والمكسرات</h2>' + ok(["زيت، زبدة ، كريم القهوة، المرغرين، في غلاف فردي."]) + no(["زيتون، كريما مخفوقة", "المكسرات"])
P.append(page("food_aunties_master.jpg", 10, "الخضار، الدهون والمكسرات", b, "center 60%"))

# 11 SAUCES + SWEETS
b = '<h2>الصلصات التوابل البهارات</h2>' + ok(["التوابل والبهارات في غلاف فردي", "كاتشب وخردل في غلاف فردي (بكميات قليلة لإحتوائها على الكثير من الملح)"]) + no(["الزعتر"]) \
  + '<h2 style="margin-top:8px">الحلويات (بكميات قليلة)</h2>' + ok(["كيك ناشف مغلف مباشرة بعد الطهي، شوكولا", "بسكويت غلاف فردي، مربى وعسل مبستر"]) \
  + no(['الحلويات العربية، الحلويات التي تحتوي على الكريما: <bdi dir="ltr">Mille feuille, éclair, choux à la crème, mousse, tarte, crème chantilly…</bdi>'])
P.append(page("food_st02_sugar.jpg", 11, "الصلصات والتوابل، والحلويات", b, "center 62%", "2.3in"))

# 12 DRINKS (+ Omar's water numbers, his stated facts)
b = ok(["المياه المعدنية أو النظيفة المكررة والمعقمة.", "مكعبات الثلج المصنوعة من المياه المغلية.", "حليب مبستر أو بودرة.",
        "شاي (ظرف) مصنوع من مياه نظيفة مغليّة، قهوة ويانسون وكاكاو", "مشروبات غازية (عبوة فرديّة)", "شوربا طازجة"]) \
  + no(["الشاي البارد وجميع الشراب المحضر مسبقاً", "مشروبات روحية"]) \
  + omar("المي عندي: ٥ ليتر باليوم بالأول، بعدين ٤، وهلّق ٣. الكمية بيحدّدها فريقك الطبي.")
P.append(page("food_e8_happy.jpg", 12, "السوائل والمشروب", b, "center 55%", "2.3in"))

# 13 QUESTIONS + SOURCES
qs = ["متى أستطيع أن آكل الخضار والفاكهة النيّة من جديد؟", "أي مطهّر أستعمل للخضار والفاكهة، وكيف؟",
      "ما الأطعمة والمشروبات الممنوعة مع أدويتي؟", "كم ملح وسكر مسموح لي في اليوم؟",
      "متى أستطيع أن آكل في المطعم أو عند الأصدقاء؟", "كم ماء أشرب في اليوم؟"]
b = '<div class="card">' + "".join(f'<p><span class="box"></span>{q}</p>' for q in qs) + '</div>' \
  + '<div class="omar" style="margin-top:6px;background:#c62828"><p style="font-weight:600">هذه تجربتي ولائحة مستشفاي، وليست نصيحة طبية. كل مريض مختلف. اسأل فريقك الطبي.</p></div>' \
  + '''<div class="card src"><p style="font-weight:600;font-size:11.5px">المصادر (تم التحقّق في ١٤ تشرين الثاني ٢٠٢٦)</p><ul>
  <li>قسم التغذية، مستشفى أوتيل ديو دو فرانس: «الطعام النظيف (المعقم) والمناعة» و«إرشادات لتغذية صحيّة ونظيفة بعد الزرع» (الورقة التي أُعطيت لي بعد الزراعة)</li>
  <li>MedlinePlus (المكتبة الوطنية الأميركية للطب): التاكروليموس (المناعة والالتهابات، الجريب فروت)</li>
 </ul></div>'''
P.append(page("food_e12_arrive.jpg", 13, "أسئلة لفريقك الطبي", b, "center 60%", "2.3in"))

# 14 MY LIST
b = '''<p class="lead">اكتب ما قاله لك فريقك الطبي، وارجع إليه حين تشكّ.</p>
 <table class="mine">
  <tr><th>عن ماذا</th><th>ما قاله فريقي الطبي</th></tr>
  <tr><td>تاريخ الزراعة</td><td></td></tr>
  <tr><td>متى أعود إلى الخضار والفاكهة النيّة</td><td></td></tr>
  <tr><td>المطهّر الذي أستعمله</td><td></td></tr>
  <tr><td>ممنوع عليّ مع أدويتي</td><td></td></tr>
  <tr><td>الملح والسكر</td><td></td></tr>
  <tr><td>الماء في اليوم</td><td></td></tr>
  <tr><td>أطعمة أريد أن أسأل عنها</td><td></td></tr>
 </table>
 <div class="card" style="margin-top:10px;background:#c62828"><p style="color:#fff;font-weight:600;font-size:15px">بتعرف حدا زرع كلية أو كبد؟ ابعتلو هالدليل.</p></div>
 <div class="omar" style="margin-top:8px">
  <p>وإذا بدك دليل تحاليلك بعد الزراعة، اكتب «تحاليل» بالتعليقات.</p>
  <p style="margin-top:8px;display:flex;align-items:center;gap:8px;justify-content:flex-start"><svg width="22" height="22" viewBox="0 0 24 24" style="vertical-align:-6px"><rect x="2" y="2" width="20" height="20" rx="6" fill="none" stroke="#fff" stroke-width="2"/><circle cx="12" cy="12" r="4.5" fill="none" stroke="#fff" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.3" fill="#fff"/></svg><svg width="22" height="22" viewBox="0 0 24 24" style="vertical-align:-6px"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/><path d="M14 3c.4 2.8 2.3 4.6 5 4.8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/></svg><bdi dir="ltr" style="font-weight:600;color:#e8c269">@omar_organtransplants</bdi></p>
 </div>'''
P.append(page(None, 14, "لائحتي أنا", b))

P.append(NOTICE)

html = f'<!doctype html>\n<html lang="ar" dir="rtl"><head><meta charset="utf-8">\n<style>{css}</style></head><body>\n' + "".join(P) + "</body></html>\n"
open(os.path.join(D, "food_after_transplant_ar.html"), "w", encoding="utf-8").write(html)
print(len(P), "pages")
