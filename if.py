tv_available = True
bank_balance = 400
withdraw = float(input ("Ausgabe:"))
bank_balance = bank_balance-withdraw

if bank_balance > 0:
    print ("Kontostand ist positiv")
else:
    print ("Du bist im minus")
