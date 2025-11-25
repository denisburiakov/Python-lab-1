V = float(input("Enter V(m^3): "))
P = float(input("Enter P(Pa): "))
T = float(input("Enter T(K(C + 241)): "))

R = 8.314
n = (P * V) / (R * T)
print(f"Amount of substance: {n:.4f} moles")