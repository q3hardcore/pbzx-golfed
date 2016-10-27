q=require;z=q('lzma-native');f=q('fs');p=f.openSync;e=f.readSync;w=f.writeSync;a=process.argv;B=Buffer;u='readUIntBE'
i=p(a[2],'r');b=new B(12);e(i,b,0,12);o=p(a[3],'w');n();function n(){if(e(i,b,4,8)){l=b[u](4,8)
e(i,b,4,8);m=b[u](4,8);d=new B(m);e(i,d,0,m);if(l>m)z.decompress(d,r=>{w(o,r,0,l);n()});else{w(o,d,0,m);n()}}}