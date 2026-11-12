// node render2.js spec.json outdir  -> ig 1080x1350 (English only), tiktok 1080x1920 (Arabic only). Spec fields: en/ar, label/label_ar, eyebrow/eyebrow_ar, sig/sig_ar, cta:[en,ar]
const {chromium}=require('playwright');require('./fontcheck')();const fs=require('fs');const path=require('path');
(async()=>{const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));const out=process.argv[3];fs.mkdirSync(out,{recursive:true});
// One language per platform (Omar, 12 Nov): IG 100% English, TikTok 100% Arabic. Every visible field needs its Arabic twin.
{const miss=[];spec.slides.forEach((s,i)=>{const n=i+1;if(s.en&&!s.ar)miss.push(n+': ar');if(s.ar&&!s.en)miss.push(n+': en');if(s.label&&!s.label_ar)miss.push(n+': label_ar');if(s.eyebrow&&!s.eyebrow_ar)miss.push(n+': eyebrow_ar');if(s.cta&&!(s.cta[0]&&s.cta[1]))miss.push(n+': cta [en, ar]');});
 if(miss.length){console.error('MISSING TRANSLATIONS (IG is English-only, TikTok Arabic-only):\n'+miss.join('\n'));process.exit(1);}}
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const [tag,w,h] of [['ig',1080,1350],['tiktok',1080,1920]]){const p=await b.newPage({viewport:{width:w,height:h}});
 for(let i=0;i<spec.slides.length;i++){const s={...spec.slides[i],w,h};
  if(tag==='tiktok'&&s.photo_tt) s.photo=s.photo_tt;
  if(s.photo) s.photo='file://'+path.resolve(path.dirname(process.argv[2]),s.photo);
  const tpl=s.photo?'card.html':'template.html';
  await p.goto('file://'+path.resolve(__dirname,tpl)+'?i='+i+'&t='+tag+'#'+encodeURIComponent(JSON.stringify(s)));
  await p.evaluate(()=>document.fonts.ready);{const bad=await p.evaluate(async()=>{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>{})));return [...document.fonts].filter(f=>f.status!=='loaded').map(f=>f.family)});if(bad.length){console.error('FONT FAILED TO LOAD: '+bad.join(', '));process.exit(1);}}
  if(spec.swipe){await p.evaluate(([i,n,tag])=>{const ar=tag==='tiktok';const d2=x=>ar?String(x).replace(/\d/g,c=>'٠١٢٣٤٥٦٧٨٩'[c]):String(x);
   if(i<2){const c=document.createElement('div');c.style.cssText='position:fixed;'+(ar?'left:96px;':'left:50%;transform:translateX(-50%);')+'bottom:'+(ar?470:110)+'px;background:#E8C269;color:#3B2C0A;font:600 36px "Readex Pro","Source Sans 3",sans-serif;padding:12px 30px;border-radius:999px;box-shadow:0 6px 20px rgba(0,0,0,.25);z-index:99;direction:'+(ar?'rtl':'ltr');c.textContent=ar?'كمّل ←':'Swipe →';document.body.appendChild(c);}
  },[i,spec.slides.length,tag]);}
  await p.waitForTimeout(250);
  await p.screenshot({path:`${out}/${spec.post}_${tag}_${String(i+1).padStart(2,'0')}.png`});}
 await p.close();}
await b.close();})();
