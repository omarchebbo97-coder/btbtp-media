// Fails the render if the fonts are missing (Omar, 12 Nov: every story/carousel must use the same fonts; no fallback serif).
const fs=require('fs'),path=require('path');
module.exports=function(){const need=['@fontsource/source-sans-3/files/source-sans-3-latin-600-normal.woff2','@fontsource/source-sans-3/files/source-sans-3-latin-400-normal.woff2','@fontsource/readex-pro/files/readex-pro-arabic-400-normal.woff2','@fontsource/readex-pro/files/readex-pro-arabic-600-normal.woff2'];
const miss=need.filter(f=>!fs.existsSync(path.join(__dirname,'node_modules',f)));
if(miss.length){console.error('FONTS MISSING, run `npm i` in tools/ first:\n'+miss.join('\n'));process.exit(1);}};
