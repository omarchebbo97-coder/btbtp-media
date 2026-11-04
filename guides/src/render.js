const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.resolve(process.argv[2]));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.pdf({path:process.argv[3],width:'5.625in',height:'10in',printBackground:true});await b.close();})();
