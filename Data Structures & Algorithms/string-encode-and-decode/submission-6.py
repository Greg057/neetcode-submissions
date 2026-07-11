class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        if not s: return []
        res = []
        count = ""
        add_word = False
        word = ""

        for c in s:
            if add_word:
                if count > 0:
                    word += c
                    count -= 1
                else:
                    add_word = False
                    count = c
                    res.append(word)
                    word = ""
            elif c != "#":
                count += c
            else:
                count = int(count)
                add_word = True
        res.append(word)
        return res
            


