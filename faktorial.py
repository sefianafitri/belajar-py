def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)
bilangan = 6
hasil_faktorial = faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah {hasil_faktorial}")
