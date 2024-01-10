# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence

    Parameters:
    seq (str): DNA sequence (or RNA sequence if reverse is True)
    reverse (bool): if True, will do reverse transcription from RNA to DNA

    Returns:
    str: RNA sequence (or DNA sequence if reverse is True)
    """

    if len(set(seq) - set(ALLOWED_NUC)) > 0:
        raise ValueError("Invalid nucleotide in sequence.")
    if reverse:
        rev_mapping = {v: k for k, v in TRANSCRIPTION_MAPPING.items()}
        return "".join([rev_mapping[nuc] for nuc in seq])
    return "".join([TRANSCRIPTION_MAPPING[nuc] for nuc in seq])

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq)[::-1]