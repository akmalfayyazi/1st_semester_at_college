def valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

def cari_jalur(x, y, mall, dikunjungi, m, n, jalur, barang_tersisa):

    if not valid(x, y, m, n) or mall[x][y] == '1' or dikunjungi[x][y]:
        return False
    
    dikunjungi[x][y] = True
    jalur.append((x, y))
    
    if mall[x][y] == '2':
        barang_tersisa[0] -= 1
    
    if x == m - 1 and y == n - 1 and barang_tersisa[0] == 0:
        return True
    
    arah = [
        (1, 0),  
        (0, 1),  
        (0, -1), 
        (-1, 0)  
    ]
    
    for dx, dy in arah:
        if cari_jalur(x + dx, y + dy, mall, dikunjungi, m, n, jalur, barang_tersisa):
            return True

    dikunjungi[x][y] = False
    jalur.pop()
    if mall[x][y] == '2':
        barang_tersisa[0] += 1
    
    return False

def hitung_total_barang(mall, m, n):
    return sum(1 for i in range(m) for j in range(n) if mall[i][j] == '2')

def main():

    n, m = map(int, input().split())
    
    peta_mall = [list(input().strip()) for _ in range(m)]
    
    dikunjungi = [[False] * n for _ in range(m)]
    jalur = []
    barang_tersisa = [hitung_total_barang(peta_mall, m, n)]
    
    ditemukan = cari_jalur(0, 0, peta_mall, dikunjungi, m, n, jalur, barang_tersisa)
    
    if ditemukan:
        hasil = [row[:] for row in peta_mall]
        for x, y in jalur:
            if hasil[x][y] != '1':
                hasil[x][y] = '*'
        
        for row in hasil:
            print(''.join(row))
    else:
        print("Tidak ada jalur yang memenuhi syarat.")

if __name__ == "__main__":
    main()