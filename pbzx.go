package main
import("bytes"
"os"
"encoding/binary"
"xi2.org/x/xz")
func main(){a:=os.Args
f,_:=os.Open(a[1])
g,_:=os.Create(a[2])
f.Seek(12,0)
u:=binary.BigEndian.Uint64
R:=f.Read
b:=make([]byte,8)
for{n,_:=R(b)
if n<8{break}
l:=u(b)
R(b)
m:=u(b)
c:=make([]byte,m)
R(c)
if l>m{r,_:=xz.NewReader(bytes.NewReader(c),0)
c=make([]byte,l)
r.Read(c)}
g.Write(c)}}