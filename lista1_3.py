area = int(input("Digite a área, em m², do seu terreno."))

if area < 100:
    print ("Seu terreno é um TERRENO POPULAR.")
elif area >= 100 or area <= 500:
    print ("Seu terreno é um TERRENO MASTER.")
else:
    print ("Seu terreno é um TERRENO VIP.")
