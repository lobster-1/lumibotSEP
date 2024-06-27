import warnings
from decimal import Decimal


def check_numeric(
    input, type, error_message, positive=True, strict=False, nullable=False, ratio=False
):
    if nullable and input is None:
        return None

    error = ValueError(error_message)

    if isinstance(input, str) or (type == Decimal and not isinstance(input, Decimal)):
        try:
            input = type(input)
        except:
            raise error

    if positive:
        if strict:
            if input <= 0:
                raise error
        else:
            if input < 0:
                raise error

    if ratio:
        if input >= 0:
            if input > 1:
                raise error
        else:
            if input < -1:
                raise error

    return input


branch_coverage = {
    "check_positive_1": False,  # strict branch
    "check_positive_2": False,  # non-strict branch
    "check_positive_3": False,  # custom message branch
    "check_positive_4": False,  # no custom message branch
    "check_quantity_1": False,  # custom message branch
    "check_quantity_2": False,  # no custom message branch
}

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

# Print coverage
print("\nCoverage results:")
print_coverage()
# Initialize coverage tracking global variable
