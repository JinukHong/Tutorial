# getter setter 대신 property를 사용
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

# __ -> private 메서드
# _ -> protected 메서드

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
    
    @property # 속성을 정의할 때 사용.
    def voltage(self):
        print("hi")
        return self._voltage


    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms
        

r = VoltageResistance(1e3)
print(r.voltage)
print(f"이전: {r.current}")
r.voltage = 10
print(f"이후: {r.current}")
