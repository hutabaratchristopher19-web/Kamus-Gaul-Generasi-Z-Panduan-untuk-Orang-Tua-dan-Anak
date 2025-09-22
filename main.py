meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    
    
            }

while True:
    word = input("Ketika ada kata yang tidak kamu ngerti(Gunakan huruf kapital semua): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("kata-kata tersebut tidak ada dalam kamus")
