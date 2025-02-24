import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_identical_strings():
    """Test when input strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_partial_match():
    """Test strings with partial match"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_input_type_errors():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", [1, 2, 3])

def test_none_input():
    """Test error handling for None inputs"""
    with pytest.raises(ValueError):
        longest_common_subsequence(None, "ABC")
    with pytest.raises(ValueError):
        longest_common_subsequence("XYZ", None)

def test_single_character_match():
    """Test scenarios with single character match"""
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_repeated_characters():
    """Test LCS with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAA") == "AAAA"
    assert longest_common_subsequence("ABCDEFG", "BCDGK") == "BCDG"