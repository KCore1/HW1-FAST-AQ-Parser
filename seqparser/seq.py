# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    if len(set(seq) - set(ALLOWED_NUC)) > 0:
        raise ValueError("Invalid nucleotide in sequence.")
    if reverse:
        return reverse_transcribe(seq)
    return "".join([TRANSCRIPTION_MAPPING[nuc] for nuc in seq])

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    pass