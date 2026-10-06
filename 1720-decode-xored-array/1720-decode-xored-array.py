class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr = [first]

        for i in range(len(encoded)):
            arr.append(arr[i] ^ encoded[i])

        return arr