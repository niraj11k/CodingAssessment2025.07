from codeToRefactor import PersonFactory

if __name__ == "__main__":
    # Create instance without seed for random names
    pf = PersonFactory()

    #Generate 5 random people
    people = pf.create_and_add_people(5)
    print("Generated People:")
    for p in people:
        print(f" - {p.name}, DOB: {p.date_of_birth.date()}")


    # Get all Bobs older than 30
    bobs_over_30 = pf._get_bobs_older_than(older_than_30=True)
    print("\nBobs older than 30:")
    for b in bobs_over_30:
        print(f" - {b.name}, DOB: {b.date_of_birth.date()}")

    #Show married name
    if people:
        married_name = pf.get_married_name(people[0], "Parker")
        print(f"\n Married name for {people[0].name}: {married_name}")
