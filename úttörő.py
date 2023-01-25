import datetime as DT

jelszo = input("jelszó:")
hossz = len(jelszo)
vb_szamjegy = szamjegy(jelszo)
vb_kisbetu = kisbetu(jelszo)
vb_nagybetu = nagybetu(jelszo)
def kisbetu(jsz) :
    s = 0 
    chs ="aábccsddzdzseéfggyhiíjkllymnnyoóöőpqrsszttyuúüűvwxyzzs"
    for c in jsz:
        s+=chs.count(c)
        return(s>0)
def nagybetu(jsz) :
    s = 0
    chs ="AÁBCCSDDZDZSEÉFGGYHIÍJKLLYMNNYOÓÖŐPQRSSZTTYUÚÜŰVWXYZZS"
    for c in jsz:
        s+=chs.count(c)
        return(s>0)
def meres(db) :
    e1 = 0
    e2 = 10 ** db
    kezd = DT.datetime.now()
    for i in range (e1 , e2) :
        s=str(i)
        x=(s==s)
    zar = DT.datetime.now
    d = zar - kezd
    return(d.microseconds/1000)
def szamjegy(jsz) :
    s = 0
    chs ="0123456789"
    for c in jsz:
        s+=chs.count(c)
        return(s>0)
print(f"a jelszó mérete : {hossz()} karakter")
print(f"a jelszóban lévő számjegyek{vb_szamjegy()}száma")
print(f"a jelszóban {vb_kisbetu()}")

