class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        time = 0
        old_position = 0
        new_position = 0
        for i in word:
            old_position = new_position
            new_position = keyboard.index(i)
            time += abs(new_position - old_position)
        return time
