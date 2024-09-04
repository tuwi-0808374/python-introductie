connection_type_a = "4g"
connection_type_b = "5g"
connection_type_c = "wifi open"

connection_str = input(f"Welke verbinding heeft u? Keuze {connection_type_a}, {connection_type_b} en {connection_type_c} \n")
print(f"{connection_str}\n")
if connection_str == connection_type_c:
    print(f"U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    awnser = input(f"Wil u nog steeds verbinden? ja of nee \n")
    if awnser == "ja":
        print(f"U bent verbonden met {connection_type_c}")
    else:
        print("U bent niet verbonden")
elif connection_str == connection_type_b:
    print(f"U bent verbonden met {connection_type_b}")
elif connection_str == connection_type_a:
    print(f"U bent verbonden met {connection_type_a}")
else:
    print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")