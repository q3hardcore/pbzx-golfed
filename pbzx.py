import lzma,struct,sys;a=sys.argv;u=struct.unpack;r=open(a[1],'rb').read;w=open(a[2],'wb').write;r(12);b=r(8)
while b:
 l=u('>Q',b);s=u('>Q',r(8));d=r(s[0])
 if l>s:d=lzma.decompress(d)
 w(d);b=r(8)