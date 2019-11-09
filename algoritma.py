from pprint import pprint
def dijkstra(graph,start,target):
    inf = float('inf')
    for u in graph:
        for v ,w in graph[u]:
          inf = inf + w                     #menghitung panjang seluruh jarak antar vertex
    dist = dict([(u,inf) for u in graph])   #buat semua jarak antar vertex menjadi infinity/sama dengan jumlah seluruh jarak antar vertex
    prev = dict([(u,None) for u in graph])  #buat dictionary, semua titik vertex dan bernilai None
    q = list(graph)                         #buat List q, berisi semua Node
    dist[start] = 0                         #dist[start]=0, Deklarasi Asal dengan nilai 0
    #helper function
    def x(v):
        return dist[v]                      #untuk mengembalikan Node yang bernilai paling kecil
    #
    while q != []:                          #selama q tidak kosong!
        u = min(q, key=x)                   #mengambil node yang ada di q dengan jarak yang paling pendek
        q.remove(u)                         #Menghapus Node u
        for v,w in graph[u]:                #Node,Jarak yang ada di graph[u]
            alt = dist[u] + w               #Menyimpan jarak dari Node asal ke Node Selanjutnya
            if alt < dist[v]:               #Cek, apakah alt lebih kecil dari destination V
                dist[v] = alt               #Ubah nilai Distination B degan Alt
                prev[v] = u                 #Ganti Node Asal dari si Next(dist[v])/Menyimpan asal node sebelumnya yang terpendek
    #?way?
    trav = []                               #Array Travel
    jarak=[]
    temp = target                           #temp = tujuan
    while temp != start:                    #Selama temp tidak sama dengan Asal
        if prev[temp]==None:
            break
        trav.append(prev[temp])             #simpan Node sebelumnya dari temp
        jarak.append(dist[temp]-dist[prev[temp]])
        temp = prev[temp]                   #temp = Node sebelumnya,datang dari mana\
    trav.reverse()                          #balikkan List travel
    trav.append(target)                     #tambhkan Node Tujuan
    jarak.reverse()
    return trav,jarak,dist[target]

def PrintTravel(graph,start,end):
    node,jarak,total=dijkstra(graph,start,end)    #memanggil fungsi Dijkstra
    hasil=""                                      #deklarasi hasil
    if len(node)==1:                              #jika panjang dari node==1?,panjang node satu jika dari asal ke tujuan tidak ada jalan, maka yang di simpan hanya node tujuan
        hasil="Tidak ada rute dari {0} ke {1}".format(start,end)
    else:
        for i in range(0,len(node)):        #perulangan List node
            if i==0:                        #jika i==0
                hasil=hasil+node[i]         #hasil=hasil+node yang ke i
            else:
                hasil=hasil+" "+str(jarak[i-1])+"-> "+node[i]
    hasil=hasil+"  = "+str(total)
    return hasil

graph = {
    "A" : [('B', 5), ('C', 7), ('D', 12)],
    'B' : [('C', 1), ('E', 6)],
    'C' : [('E', 5), ('F', 10), ('D', 1)],
    'D' : [('F', 13)],
    'E' : [('F', 2), ('G', 7)],
    'F' : [('G', 3)],
    'G' : []
}

a=PrintTravel(graph,'A','G')
print(a)

graph2 = {
    "A" : [('B',20), ('D', 80), ('G', 90)],
    'B' : [('F', 60),('D', 70)],
    'C' : [('F', 50), ('H', 20)],
    'D' : [('G', 20), ('C', 10)],
    'E' : [('B', 50),('G', 30)],
    'F' : [('D', 40),('C', 30)],
    'G' : [('A', 20)],
    'H' : []
    }
print(PrintTravel(graph2,'A','D'))