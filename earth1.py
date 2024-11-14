import time

def quadratic_search_phrase(phrase, target_word):
    # Split the phrase into a list of words
    words = phrase.split()
    FIRST = 0
    LAST = len(words) - 1
    
    start_time = time.time()  # Start the timer

    while FIRST <= LAST:
        MID = (FIRST + LAST) // 2
        P1 = FIRST + (LAST - FIRST) // 4
        P2 = FIRST + (LAST - FIRST) * 3 // 4
        
        # Check if the target_word is at MID, P1, or P2
        if target_word == words[MID]:
            end_time = time.time()  # Stop the timer
            return f"Word found at index {MID}, Time taken: {end_time - start_time:.6f} seconds"
        elif target_word == words[P1]:
            end_time = time.time()  # Stop the timer
            return f"Word found at index {P1}, Time taken: {end_time - start_time:.6f} seconds"
        elif target_word == words[P2]:
            end_time = time.time()  # Stop the timer
            return f"Word found at index {P2}, Time taken: {end_time - start_time:.6f} seconds"
        
        # Condition 1: If target_word is lexicographically less than MID and P1
        if target_word < words[MID] and target_word < words[P1]:
            LAST = P1 - 1
        # Condition 2: If target_word is less than MID and greater than P1
        elif target_word < words[MID] and target_word > words[P1]:
            FIRST = P1 + 1
            LAST = MID - 1
        # Condition 3: If target_word is greater than MID and also greater than P2
        elif target_word > words[MID] and target_word > words[P2]:
            FIRST = P2 + 1
        # Condition 4: If target_word is greater than MID and less than P2
        elif target_word > words[MID] and target_word < words[P2]:
            FIRST = MID + 1
            LAST = P2 - 1

    end_time = time.time()  # Stop the timer
    return f"Word not found, Time taken: {end_time - start_time:.6f} seconds"

# Example usage
phrase = "world is a beautiful place"
target_word = "beautiful"
print(quadratic_search_phrase(phrase, target_word))
