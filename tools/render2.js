// node render2.js spec.json outdir  -> ig 1080x1350 (EN first), tiktok 1080x1920 (AR first)
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));const out=process.argv[3];fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const [tag,w,h] of [['ig',1080,1350],['tiktok',1080,1920]]){const p=await b.newPage({viewport:{width:w,height:h}});
 for(let i=0;i<spec.slides.length;i++){const s={...spec.slides[i],w,h};
  if(s.photo) s.photo='file://'+path.resolve(path.dirname(process.argv[2]),s.photo);
  const tpl=s.photo?'card.html':'template.html';
  await p.goto('file://'+path.resolve(__dirname,tpl)+'?i='+i+'&t='+tag+'#'+encodeURIComponent(JSON.stringify(s)));
  await p.evaluate(()=>document.fonts.ready);
  if(spec.swipe){await p.evaluate(([i,n,tag])=>{const ar=tag==='tiktok';const d2=x=>ar?String(x).replace(/\d/g,c=>'٠١٢٣٤٥٦٧٨٩'[c]):String(x);
   if(i<2){const c=document.createElement('div');c.style.cssText='position:fixed;left:50%;transform:translateX(-50%);bottom:110px;background:#E8C269;color:#3B2C0A;font:600 36px "Readex Pro","Source Sans 3",sans-serif;padding:12px 30px;border-radius:999px;box-shadow:0 6px 20px rgba(0,0,0,.25);z-index:99;direction:'+(ar?'rtl':'ltr');c.textContent=ar?'كمّل ←':'Swipe →';document.body.appendChild(c);}
  },[i,spec.slides.length,tag]);}
  await p.waitForTimeout(250);
  await p.screenshot({path:`${out}/${spec.post}_${tag}_${String(i+1).padStart(2,'0')}.png`});}
 await p.close();}
await b.close();})();
