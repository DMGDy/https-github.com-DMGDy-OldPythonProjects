males = float(input("How many males are in the class? "))
females = float(input("How many females are in the class? "))
mp = (males / (males + females) * 100)
fp = (females / (males + females) * 100)
print("The class is " + str(mp) + "% male and " + str(fp) + "% female")
