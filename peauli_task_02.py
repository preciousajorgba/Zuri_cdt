class cascading_palindrome:
    # Initialize the class attribute and validate the input string
    def __init__(self, palindrome):
        if not (isinstance(palindrome, str) and all(
            word.isalnum() or word.isnumeric() or word.isspace() for word in palindrome.split()
        )):
            raise ValueError("Input must be a string containing only space-separated words, numbers, or a mixture of both")

        self.palindrome = palindrome

    # Extract and join single palindromes to form a palindromic string
    def palindrome_string(self):
        the_string = self.palindrome.split()
        
        # I used agenerator here
        palindromes = (x for x in the_string if x == x[::-1])

        # Join them
        return " ".join(palindromes)

# Examples 
if __name__ == "__main__":
    try:
        pali_01= cascading_palindrome("philip samas chidi civic 164404461  ade 8839779388 kelek")
        palidromic_string_01= pali_01.palindrome_string()
        print(palidromic_string_01)

        pali_02= cascading_palindrome("padi 384919483 degged 32156 adinida 4759669574 sememes")
        palidromic_string_02= pali_02.palindrome_string()
        print(palidromic_string_02)

        pali_03= cascading_palindrome("kaiak 61 3628448263 dewed 0 succus 294492 117i")
        palidromic_string_03= pali_03.palindrome_string()
        print(palidromic_string_03)

        pali_04= cascading_palindrome("62 malayalam 67899 divid")
        palidromic_string_04= pali_04.palindrome_string()
        print(palidromic_string_04)

        pali_05= cascading_palindrome("0112 rever 4461661644")
        palidromic_string_05= pali_05.palindrome_string()
        print(palidromic_string_05)

        pali_06= cascading_palindrome("solos 44616 7282")
        palidromic_string_06= pali_06.palindrome_string()
        print(palidromic_string_06)

        pali_07= cascading_palindrome("kinnikinnik 78888 641515146")
        palidromic_string_07= pali_07.palindrome_string()
        print(palidromic_string_07)

        pali_08= cascading_palindrome("tirrit 947000 ada one")
        palidromic_string_08= pali_08.palindrome_string()
        print(palidromic_string_08)

        pali_09= cascading_palindrome("malam 234252432")
        palidromic_string_09= pali_09.palindrome_string()
        print(palidromic_string_09)

        pali_10= cascading_palindrome("hallah  wahala 419 peeweep")
        palidromic_string_10= pali_10.palindrome_string()
        print(palidromic_string_10)
        
    except ValueError as e:
        print(f"Error: {e}")
