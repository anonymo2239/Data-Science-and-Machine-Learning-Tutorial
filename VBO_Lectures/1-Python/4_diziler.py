
alperen = ["ali", "veli", "alperen", "baturalp"]
print(alperen)

alperen[1] = "velinin babasi"
print(alperen)

alperen = alperen + ["velinin amcasi"] # yeniden atamaya gerek var
alperen.append("velinin amcasi") # yeniden atamaya gerek yok

print(alperen)

del alperen[4] # yeniden atamaya gerek yok
alperen.remove("velinin amcasi") # yeniden atamaya gerek yok

print(alperen)
