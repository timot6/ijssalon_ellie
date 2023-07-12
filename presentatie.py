def presenteer(number_dict, totaal):
    for item, prijs in number_dict.items():
        print(f"{item} : {prijs} euro")
    
    print(26 * "=")
    print(f"Totaal : {totaal} euro")
    