"""
=============================================
  String & Number Utilities Library
  Author: Python Developer
  Version: 1.0
=============================================
"""

import re
import unicodedata


# ============================================
#  STRING UTILITIES
# ============================================

def normalize_text(text: str, mode: str = "default") -> str:
    """
    Chuẩn hóa chuỗi văn bản.
    
    Modes:
      - "default" : Xóa khoảng trắng thừa, trim 2 đầu
      - "lower"   : default + chuyển về chữ thường
      - "upper"   : default + chuyển về chữ hoa
      - "unicode" : default + chuẩn hóa Unicode (NFC)
      - "clean"   : Xóa tất cả ký tự đặc biệt, chỉ giữ chữ cái và số
    
    >>> normalize_text("  Xin   chào   thế  giới  ")
    'Xin chào thế giới'
    >>> normalize_text("  HELLO   WORLD  ", mode="lower")
    'hello world'
    >>> normalize_text("H3ll0 W0rld!", mode="clean")
    'H3ll0 W0rld'
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    if mode == "unicode":
        text = unicodedata.normalize("NFC", text)

    if mode == "clean":
        text = re.sub(r'[^a-zA-Z0-9À-ỹ\s]', '', text)

    # Xóa khoảng trắng thừa (nhiều space -> 1 space)
    result = re.sub(r'\s+', ' ', text).strip()

    if mode == "lower":
        result = result.lower()
    elif mode == "upper":
        result = result.upper()

    return result


def count_words(text: str) -> dict:
    """
    Đếm số từ trong chuỗi. Trả về dict chi tiết.
    
    >>> count_words("Hello world hello")
    {'total': 3, 'unique': 2, 'frequency': {'hello': 2, 'world': 1}}
    >>> count_words("  Một   hai   ba  ")
    {'total': 3, 'unique': 3, 'frequency': {'Một': 1, 'hai': 1, 'ba': 1}}
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    words = text.split()
    total = len(words)

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return {
        "total": total,
        "unique": len(frequency),
        "frequency": frequency,
    }


def reverse_text(text: str, mode: str = "char") -> str:
    """
    Đảo ngược chuỗi.
    
    Modes:
      - "char"  : Đảo theo ký tự
      - "word"  : Đảo theo từ
      - "word_keep_order" : Đảo thứ tự từ nhưng giữ nguyên từ
    
    >>> reverse_text("Hello World")
    'dlroW olleH'
    >>> reverse_text("Hello World", mode="word")
    'World Hello'
    >>> reverse_text("Một hai ba", mode="char")
    'ab iah tóM'
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    if mode == "char":
        return text[::-1]
    elif mode == "word":
        words = text.split()
        return " ".join(reversed(words))
    else:
        raise ValueError(f"Unknown mode: '{mode}'. Use 'char' or 'word'.")


def is_palindrome(text: str, ignore_case: bool = True, 
                  ignore_spaces: bool = True, 
                  ignore_special: bool = True) -> dict:
    """
    Kiểm tra chuỗi có phải palindrome (xuôi ngược giống nhau) không.
    
    Args:
        text             : Chuỗi cần kiểm tra
        ignore_case      : Bỏ qua phân biệt hoa/thường
        ignore_spaces    : Bỏ qua khoảng trắng
        ignore_special   : Bỏ qua ký tự đặc biệt (chỉ giữ chữ + số)
    
    >>> is_palindrome("Race car")
    {'is_palindrome': True, 'original': 'Race car', 'processed': 'racecar', 'reversed': 'racecar'}
    >>> is_palindrome("Hello")
    {'is_palindrome': False, 'original': 'Hello', 'processed': 'hello', 'reversed': 'olleh'}
    >>> is_palindrome("A man, a plan, a canal: Panama")
    {'is_palindrome': True, 'original': 'A man, a plan, a canal: Panama', 'processed': 'amanaplanacanalpanama', 'reversed': 'amanaplanacanalpanama'}
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    processed = text

    if ignore_special:
        processed = re.sub(r'[^a-zA-Z0-9À-ỹ]', '', processed)

    if ignore_spaces:
        processed = processed.replace(" ", "")

    if ignore_case:
        processed = processed.lower()

    reversed_text = processed[::-1]
    result = (processed == reversed_text)

    return {
        "is_palindrome": result,
        "original": text,
        "processed": processed,
        "reversed": reversed_text,
    }


# ============================================
#  CHẠY TEST
# ============================================
if __name__ == "__main__":

    print("=" * 60)
    print("  📖 STRING UTILITIES - DEMO")
    print("=" * 60)

    # --- normalize_text ---
    print("\n🔧 normalize_text()")
    print("-" * 40)

    samples = [
        ("  Xin   chào   thế  giới  ", "default"),
        ("  HELLO   WORLD  ", "lower"),
        ("  hello   world  ", "upper"),
        ("H3ll0 W0rld! @#Test", "clean"),
    ]

    for text, mode in samples:
        result = normalize_text(text, mode=mode)
        print(f"  [{mode:>7}] '{text}' → '{result}'")

    # --- count_words ---
    print("\n🔢 count_words()")
    print("-" * 40)

    for text in ["Hello world hello", "  Một   hai   ba  ", "Python is great, Python is fun"]:
        result = count_words(text)
        print(f"  '{text}'")
        print(f"    → Total: {result['total']} | Unique: {result['unique']} | Freq: {result['frequency']}")

    # --- reverse_text ---
    print("\n🔄 reverse_text()")
    print("-" * 40)

    text = "Hello World"
    print(f"  [char] '{text}' → '{reverse_text(text, mode='char')}'")
    print(f"  [word] '{text}' → '{reverse_text(text, mode='word')}'")
    print(f"  [char] 'Một hai ba' → '{reverse_text('Một hai ba', mode='char')}'")
    print(f"  [word] 'Một hai ba' → '{reverse_text('Một hai ba', mode='word')}'")

    # --- is_palindrome ---
    print("\n🔍 is_palindrome()")
    print("-" * 40)

    test_cases = [
        "Race car",
        "Hello",
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "12321",
        "abc",
    ]

    for text in test_cases:
        result = is_palindrome(text)
        icon = "✅" if result["is_palindrome"] else "❌"
        print(f"  {icon} '{text}'")
        print(f"      processed: '{result['processed']}' | reversed: '{result['reversed']}'")

    print("\n" + "=" * 60)
    print("  ✅ Hoàn thành!")
    print("=" * 60)