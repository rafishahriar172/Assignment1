def validate_input(prompt, expected_type):
    while True:
        value = input(prompt)
        try:
            if expected_type == int:
                value = int(value)
            elif expected_type == str:
                if not value.isalpha():
                    raise ValueError("Name must contain only letters.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
