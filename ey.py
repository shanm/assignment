transactions = [
 {"txn_id": "T1", "amount": 100},
 {"txn_id": "T2", "amount": 200},
 {"txn_id": "T1", "amount": 100},
 {"txn_id": "T3", "amount": 300},
 {"txn_id": "T2", "amount": 250},
 ]

#tnxn = list({tnxn["txn_id"]: tnxn for tnxn in transactions}.values())

seen = set()
result = []

for transaction in transactions:
    #print(transaction["txn_id"])
    if transaction["txn_id"] not in seen:
        seen.add(transaction["txn_id"])
        result.append(transaction)

print(seen)
print(result)