require"xz";i=File.new($*[0],"rb");o=File.new($*[1],"wb");i.read(12)
while b=i.read(8)
b=b.unpack("Q>")[0];c=i.read(8).unpack("Q>")[0];e=i.read(c)
o.write(b>c ?XZ.decompress(e):e)
end