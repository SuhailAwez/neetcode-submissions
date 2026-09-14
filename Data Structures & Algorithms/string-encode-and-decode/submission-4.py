class Solution:
    KEY = 'A1B2C3'
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#EMPTY#"
        return self.KEY.join(strs)


    def decode(self, s: str) -> List[str]:
        if s=="#EMPTY#":
            return []
        else:
            return s.split(self.KEY)