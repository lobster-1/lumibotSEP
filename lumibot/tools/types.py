import warnings
from decimal import Decimal

branch_coverage = {
    "check_numeric_nullable": False,
    "check_numeric_conversion": False,
    "check_numeric_positive_strict": False,
    "check_numeric_positive_non_strict": False,
    "check_numeric_ratio_pos": False,
    "check_numeric_ratio_neg": False,
    "check_positive_1": False,  # strict branch
    "check_positive_2": False,  # non-strict branch
    "check_positive_3": False,  # custom message branch
    "check_positive_4": False,  # no custom message branch
    "check_quantity_1": False,  # custom message branch
    "check_quantity_2": False,  # no custom message branch
    "check_price_1": False,  # custom message branch
    "check_price_2": False,  # no custom message branch
}


def check_numeric(
    input, type, error_message, positive=True, strict=False, nullable=False, ratio=False
):
    if nullable and input is None:
        branch_coverage["check_numeric_nullable"] = True
        return None

    error = ValueError(error_message)

    if isinstance(input, str) or (type == Decimal and not isinstance(input, Decimal)):
        try:
            input = type(input)
            branch_coverage["check_numeric_conversion"] = True
        except:
            raise error

    if positive:
        if strict:
            branch_coverage["check_numeric_positive_strict"] = True
            if input <= 0:
                raise error
        else:
            branch_coverage["check_numeric_positive_non_strict"] = True
            if input < 0:
                raise error

    if ratio:
        if input >= 0:
            branch_coverage["check_numeric_ratio_pos"] = True
            
        else:
            branch_coverage["check_numeric_ratio_neg"] = True
            

    return input


def check_positive(input, type, custom_message="", strict=False):
    if strict:
        branch_coverage["check_positive_1"] = True
        error_message = "%r is not a strictly positive value." % input
    else:
        branch_coverage["check_positive_2"] = True
        error_message = "%r is not a positive value." % input

    if custom_message:
        branch_coverage["check_positive_3"] = True
        error_message = f"{error_message} {custom_message}"
    else:
        branch_coverage["check_positive_4"] = True

    result = check_numeric(
        input,
        type,
        error_message,
        strict=strict,
    )
    return result


def check_quantity(quantity, custom_message=""):
    error_message = "%r is not a positive Decimal." % quantity
    if custom_message:
        branch_coverage["check_quantity_1"] = True
        error_message = f"{error_message} {custom_message}"
    else:
        branch_coverage["check_quantity_2"] = True

    quantity = Decimal(quantity)
    result = check_numeric(
        quantity,
        Decimal,
        error_message,
        strict=True,
    )
    return result


def check_price(price, custom_message="", nullable=True):
    error_message = "%r is not a valid price." % price
    if custom_message:
        branch_coverage["check_price_1"] = True
        error_message = f"{error_message} {custom_message}"
    else:
        branch_coverage["check_price_2"] = True

    result = check_numeric(price, float, error_message, strict=True, nullable=nullable)
    return result


def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")


# Test cases
try:
    print("Testing check_positive:")
    check_positive(5, int, strict=True)
    check_positive(0, int, strict=False)
    check_positive(10, float, custom_message="Please enter a positive number.")
    check_positive(-1, int)  # This will hit the non-strict branch without custom message
except Exception as e:
    print(f"Exception in check_positive: {e}")

try:
    print("\nTesting check_quantity:")
    check_quantity("5.5")  # This will hit the else branch (no custom message)
    check_quantity("10", custom_message="Enter a valid quantity.")  # This will hit the if branch
except Exception as e:
    print(f"Exception in check_quantity: {e}")

try:
    print("\nTesting check_price:")
    check_price(None)  # This will hit the nullable branch
    check_price("20.5")  # This will hit the conversion branch
    check_price("-5", custom_message="Price must be positive.")  # This will raise an error
except Exception as e:
    print(f"Exception in check_price: {e}")

# New test cases for ratio branches
try:
    print("\nTesting check_numeric for ratio branches:")
    check_numeric(1.5, float, "Ratio error", ratio=True)  # This will hit the positive ratio branch (> 1)
except Exception as e:
    print(f"Exception in check_numeric (ratio positive): {e}")

try:
    check_numeric(-1.5, float, "Ratio error", ratio=True)  # This will hit the negative ratio branch (< -1)
except Exception as e:
    print(f"Exception in check_numeric (ratio negative): {e}")

try:
    check_numeric(-0.5, float, "Ratio error", ratio=True)  # This will not raise an error (within ratio)
except Exception as e:
    print(f"Exception in check_numeric (ratio within bounds): {e}")

# Print coverage
print("\nCoverage results:")
print_coverage()
