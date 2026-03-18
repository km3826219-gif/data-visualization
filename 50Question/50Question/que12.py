check_vote = lambda age: "Eligible to vote" if age >= 18 else "Not eligible to vote"

age = int(input("Enter your age: "))
print(check_vote(age))