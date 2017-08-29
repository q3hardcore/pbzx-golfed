import lzma,struct,sys;x,y,z=sys.argv;u=struct.unpack;r=open(y,'rb').read;w=open(z,'wb').write;r(12);b=r(16)
while b:
 l,s=u('>QQ',b);d=r(s)
 if l>s:d=lzma.decompress(d)
 w(d);b=r(16)