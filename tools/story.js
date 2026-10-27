// node story.js spec.json out.jpg -> 1080x1920 story (+ _preview.jpg 540x960). Photo path relative to spec.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const s=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));s.photo='file://'+path.resolve(path.dirname(process.argv[2]),s.photo);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.resolve(__dirname,'story.html')+'#'+encodeURIComponent(JSON.stringify(s)));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const out=process.argv[3];await p.screenshot({path:out,type:'jpeg',quality:90});
await p.setViewportSize({width:1080,height:1920});await b.close();})();
