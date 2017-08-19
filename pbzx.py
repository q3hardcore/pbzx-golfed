import lzma,struct,sys;x,y,z=sys.argv;u=struct.unpack;r=open(y,'rb').read;w=open(z,'wb').write;r(12);b=r(8)
while b:
 l,=u('>Q',b);s,=u('>Q',r(8));d=r(s)
 if l>s:d=lzma.decompress(d);w(d);b=r(8)