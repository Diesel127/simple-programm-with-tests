def get_evens_positive(n: int) -> list:
    result = list(filter(lambda x: x % 2 == 0, range(0, n + 1)))
    return result

def get_evens_negative(n: int) -> list:
    result = [i for i in range(n, 0) if i % 2 == 0]
    return result

def main() -> None:
    while True:
        try:
            user_input = int(input("Enter integer: "))
        except Exception as e:
            print(f"Error occured: {e}, please enter integer(example: 10, -10")
        else:
            if user_input == 0:
                print("0")
            elif user_input > 0:
                print(get_evens_positive(user_input))
            else:
                print(get_evens_negative(user_input))
if __name__ == "__main__":
    main()