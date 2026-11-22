def display_all_cars(makes: list[str], years: list[int], prices: list[int])-> None:
    """
    Input: there is lists inputted.
    Process: it evaluates and add all the valus from the lists
    Output: it would print what is necessary.
    """
    total=0
    index=0
    for characters in makes:
        print(f"${prices[index]}: A", makes[index], "made in", f"{years[index]}.")
        total += prices[index]
        index+=1
    print("----------------------------------------")
    print(f"Total value of all cars: ${total}")
def main():
    makes  = ['Maserati', 'Honda', 'Subaru', 'Fiat', 'Ford', 'Porsche', 'Mazda', 'Lotus']
    years  = [2004, 1989, 2002, 2016, 2008, 1989, 2023, 2011]
    prices = [18000, 2499, 6000, 8495, 15499, 33250, 34999, 63915]

    display_all_cars(makes, years, prices)
if __name__ == "__main__":
    main()