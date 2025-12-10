from typing import Dict, List

def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def get_char_count(text: str) -> Dict[str, int]:
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_sorted_char_count(char_count: Dict[str, int]):
    sorted_count = []
    for char, count in char_count.items():
        sorted_count.append({"name": char, "num": count})
    sorted_count.sort(key=lambda x: x["num"], reverse=True)
    return sorted_count
