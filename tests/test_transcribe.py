# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)
import pytest


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Unit test for transcribe function
    """
    assert transcribe("AAA") == "UUU"
    assert transcribe("GGG") == "CCC"
    assert transcribe("CCC") == "GGG"
    assert transcribe("TTT") == "AAA"
    assert transcribe("AAATTTCCTGAA") == "UUUAAAGGACUU"
    assert transcribe("AAATTTCCTGAA", reverse=True) == "UUCAGGAAAUUU"
    with pytest.raises(ValueError):
        transcribe("SAXOPHONE")



def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert reverse_transcribe("AAA") == "UUU"
    assert reverse_transcribe("GAATTC") == "GAAUUC"
