# write tests for parsers
# NOTE: Must run pytest -v from the root directory of the project

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/blank.fa
    """
    parser = FastaParser("data/test.fa")
    assert parser.filename == "data/test.fa"
    ALLOWED_CHARS = set("ACGTU")

    for tup in parser:
        assert len(tup) == 2
        assert type(tup) == tuple
        assert type(tup[0]) == str
        assert type(tup[1]) == str
        assert len(tup[1]) > 0
        assert all(char in ALLOWED_CHARS for char in tup[1])

    with pytest.raises(ValueError):
        for tup in FastaParser("tests/bad.fa"):
            pass

    with pytest.raises(ValueError):
        for tup in FastaParser("tests/blank.fa"):
            pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in. If a fastq file is
    read, the first item is None
    """
    for tup in FastaParser("data/test.fq"):
        assert tup[0] is None # verifying expected behavior
        break
    for tup in FastaParser("data/test.fa"):
        assert tup[0] is not None
        break


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    parser = FastqParser("data/test.fq")
    assert parser.filename == "data/test.fq"
    ALLOWED_CHARS = set("ACGTU")
    ALLOWED_QUAL = set("\"!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~")

    for tup in parser:
        assert len(tup) == 3
        assert type(tup) == tuple
        assert type(tup[0]) == str
        assert type(tup[1]) == str
        assert type(tup[2]) == str
        assert len(tup[1]) > 0
        assert len(tup[2]) > 0
        assert all(char in ALLOWED_CHARS for char in tup[1])
        assert all(char in ALLOWED_QUAL for char in tup[2])

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    for tup in FastqParser("data/test.fa"):
        assert tup[0] is None # again, verifying expected behavior
        break
    for tup in FastqParser("data/test.fq"):
        assert tup[0] is not None
        break