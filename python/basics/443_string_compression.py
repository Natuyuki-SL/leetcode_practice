def compress(chars: list) -> int:
        if len(chars) == 1:
            return 1
        current_letter = chars[0]
        position = 1
        letter_count = 1

        for i in range(1, len(chars)):
            if chars[i] == current_letter:
                letter_count +=1
            
            # When we encounter a new letter
            else: 
                # Append the letter count if >1
                if letter_count >1:
                    letter_count = str(letter_count)
                    for num in letter_count:
                        chars[position] = num
                        position +=1
                letter_count = 1
                # Modify the current letter and append it to the correct position
                current_letter = chars[i]
                chars[position] = current_letter
                position +=1
        
        # To compensate for the final print if needed
        if 1 < letter_count:
            letter_count = str(letter_count)
            for num in letter_count:
                chars[position] = num
                position +=1
        return position

testcases = [["a","a","b","b","c","c","c"],
             ["a"],
             ["a","b","b","b","b","b","b","b","b","b","b","b","b"],
             ["a","b","c"],
             ["a","a","a","a","a","b"],
             ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a",
              "a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a",
              "a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a",
              "a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a",
              "a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a",
              "a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]]

for chars in testcases:
    pos = compress(chars)
    print(chars[:pos])
