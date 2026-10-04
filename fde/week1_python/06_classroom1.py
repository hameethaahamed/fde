invoice_amount = 1000

if invoice_amount <= 1000:
    print("amount  1000 -> Approved by Supervisor")
elif invoice_amount > 25000:
    print("amount > 25000 -> Approved by Manager")
elif invoice_amount > 50000:
    print("amount > 50000 -> Approved by Manager and Director")

match invoice_amount:
    case amount if amount <= 1000:   
        print("amount  1000 -> Approved by Supervisor")                
    case amount if amount > 25000:   
        print("amount > 25000 -> Approved by Manager")
    case amount if amount > 50000:   
        print("amount > 50000 -> Approved by Manager and Director")
    case _:   
        print("amount does not match any criteria")



employees = [
    [101, "Alice", 200000],
    [102, "John", 300000],
    [103, "Hameetha", 180000],
    [104, "David", 240000],
    [105, "Priya", 120000]
]

for emp_id, name, salary in employees:
    if len(name) > 6 and salary < 250000:
        print(name, "is a senior employee with ID", emp_id, "and salary", salary)


