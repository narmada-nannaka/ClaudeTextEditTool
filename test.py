import math
from main import calculate_pi


def test_calculate_pi():
    """Test that calculate_pi returns pi accurate to 5 decimal places."""
    calculated_pi = calculate_pi()
    actual_pi = math.pi
    
    # Test accuracy to 5 decimal places (3.14159)
    print(f"Calculated pi: {calculated_pi}")
    print(f"Math.pi value: {actual_pi}")
    print(f"Difference: {abs(calculated_pi - actual_pi)}")
    
    # Round both to 5 decimal places and compare
    calculated_rounded = round(calculated_pi, 5)
    actual_rounded = round(actual_pi, 5)
    
    print(f"\nCalculated pi (5 decimals): {calculated_rounded}")
    print(f"Actual pi (5 decimals): {actual_rounded}")
    
    assert calculated_rounded == actual_rounded, \
        f"Pi calculation not accurate to 5 decimal places. Got {calculated_rounded}, expected {actual_rounded}"
    
    # Also verify the value is close to expected 3.14159
    assert abs(calculated_pi - 3.14159) < 0.000001, \
        f"Pi should be approximately 3.14159, got {calculated_pi}"
    
    print("\n✓ All tests passed! Pi calculated correctly to 5 decimal places.")


def test_pi_range():
    """Test that calculated pi is in a reasonable range."""
    calculated_pi = calculate_pi()
    
    assert 3.14 < calculated_pi < 3.15, \
        f"Pi should be between 3.14 and 3.15, got {calculated_pi}"
    
    print("✓ Pi is in the expected range.")


def test_pi_first_five_digits():
    """Test that the first 5 decimal digits are correct (3.14159)."""
    calculated_pi = calculate_pi()
    
    # Extract first 5 decimal digits
    pi_string = f"{calculated_pi:.5f}"
    
    print(f"Pi to 5 decimal places: {pi_string}")
    
    assert pi_string == "3.14159", \
        f"Expected '3.14159', got '{pi_string}'"
    
    print("✓ First 5 decimal digits are correct: 3.14159")


if __name__ == "__main__":
    print("Running tests for calculate_pi()...\n")
    print("=" * 60)
    
    try:
        test_calculate_pi()
        print("\n" + "=" * 60)
        test_pi_range()
        print("\n" + "=" * 60)
        test_pi_first_five_digits()
        print("\n" + "=" * 60)
        print("\n🎉 All tests passed successfully!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
