# v2 builder: captions top, colour per speaker, long lines split, end card only in the tail
import json,subprocess,os,sys,re
SP=os.environ.get('BTBTP_SP','/tmp/claude-0/-home-claude/988431de-1e8a-5e55-a69c-1b6d3578148a/scratchpad')
COL={'Wadad':'rgba(168,64,112,.92)','Souad':'rgba(62,112,84,.92)','New kidney':'rgba(176,128,30,.94)','guest':'rgba(61,88,108,.93)','end':'rgba(61,88,108,.95)'}
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
def split(ar,en):
    if len(ar)<=48: return [(ar,en)]
    def cut(s):
        m=len(s)//2;best=None
        for i,ch in enumerate(s):
            if ch in '،.؟?…,!' and 0.25*len(s)<i<0.8*len(s):
                if best is None or abs(i-m)<abs(best-m): best=i
        if best is None:
            sp=[i for i,ch in enumerate(s) if ch==' '];best=min(sp,key=lambda i:abs(i-m))
        return s[:best+1].strip(),s[best+1:].strip()
    a1,a2=cut(ar);e1,e2=cut(en);return [(a1,e1),(a2,e2)]
def build(cfg_path):
    cfg=json.load(open(cfg_path));out=cfg['out'];d=os.path.join(SP,'v2',out);os.makedirs(d,exist_ok=True);os.chdir(d)
    caps=[];plan=[]
    for i,l in enumerate(cfg['lines'],1):
        parts=split(l['ar'],l['en']);col=COL.get(l['who'],COL['guest'])
        names=[]
        for k,(a,e) in enumerate(parts):
            n=f'c{i}{"ab"[k]}';caps.append([n,{'ar':a,'en':e,'col':col}]);names.append((n,len(a)))
        plan.append(names)
    caps.append(['endcard',{'ar':cfg['end'],'en':cfg['endsub'],'col':COL['end'],'end':1}])
    js="const {chromium}=require('%s/tpl/node_modules/playwright');const path=require('path');const C=%s;(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});for(const [n,o] of C){await p.goto('file://'+path.resolve('%s/v2/cap2.html')+'?n='+n+'#'+encodeURIComponent(JSON.stringify(o)));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);await p.screenshot({path:n+'.png',omitBackground:true});}await b.close();})();"%(SP,json.dumps(caps,ensure_ascii=False),SP)
    open('cap.js','w').write(js);subprocess.run(['node','cap.js'],check=True)
    T=1.06;N=len(cfg['lines']);lst=open('list.txt','w');al=[]
    for i,l in enumerate(cfg['lines'],1):
        last=i==N;g=2.8 if last else 0.3
        a=l['audio'];sd=dur(a)/T;dd=sd+g;n=int(round(dd*30))
        img=l['img'];z0,z1,cx,cy=l['z']
        names=plan[i-1];ins=['-loop','1','-i',img];ov='[v]';k=1;tot=sum(x[1] for x in names);t0=0;chain=''
        for j,(nm,ln) in enumerate(names):
            ins+=['-i',nm+'.png'];t1=sd if j==len(names)-1 else sd*ln/tot+t0
            end=dd if (j==len(names)-1 and not last) else t1+ (0.25 if last else 0)
            chain+=f"{ov}[{k}]overlay=0:0:enable='between(t,{t0:.2f},{end:.2f})'[o{k}];";ov=f'[o{k}]';k+=1;t0=t1
        if last:
            ins+=['-i','endcard.png'];chain+=f"{ov}[{k}]overlay=0:0:enable='gte(t,{sd+0.25:.2f})'[o{k}];";ov=f'[o{k}]'
        fc=f"[0]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='iw*{cx}-iw/zoom/2':y='ih*{cy}-ih/zoom/2':d={n}:s=1080x1920:fps=30[v];"+chain+f"{ov}format=yuv420p"
        subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y',*ins,'-filter_complex',fc,'-t',str(round(dd,3)),'-r','30','-c:v','libx264','-preset','medium','-crf','18',f'seg_{i}.mp4'],check=True)
        subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',a,'-af',f'atempo={T},apad=pad_dur={g},aresample=44100','-t',str(round(dd,3)),'-ac','2',f'a{i}.wav'],check=True)
        lst.write(f"file 'seg_{i}.mp4'\n");al.append(f'a{i}.wav')
    lst.close();open('alist.txt','w').write(''.join(f"file '{x}'\n" for x in al))
    subprocess.run(f'ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i list.txt -c copy v.mp4 && ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i alist.txt -c copy a.wav && ffmpeg -hide_banner -loglevel error -y -i v.mp4 -i a.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart {out}.mp4 && ffmpeg -hide_banner -loglevel error -y -i {out}.mp4 -vf scale=540:960 -c:v libx264 -crf 28 -preset veryfast -c:a aac -b:a 96k -movflags +faststart {out}_preview.mp4 && ffmpeg -loglevel error -y -i {out}.mp4 -vf "fps=1/3,scale=240:427,tile=12x1" -frames:v 1 frames.jpg',shell=True,check=True)
    print(out,round(dur(out+'.mp4'),1))
build(sys.argv[1])
