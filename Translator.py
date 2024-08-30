class Translator:
    def __init__(self, wrist, thumb_cmc, thumb_mcp, thumb_ip, thumb_tip, index_mcp, index_pip, index_dip, index_tip, middle_mcp, middle_pip, middle_dip, middle_tip, ring_mcp, ring_pip, ring_dip, ring_tip, pinky_mcp, pinky_pip, pinky_dip, pinky_tip):
        self.wrist = wrist 
        self.thumb_cmc = thumb_cmc
        self.thumb_mcp = thumb_mcp
        self.thumb_ip = thumb_ip
        self.thumb_tip = thumb_tip
        self.index_pip = index_pip
        self.index_dip = index_dip
        self.index_tip = index_tip
        self.index_mcp = index_mcp
        self.middle_mcp = middle_mcp
        self.middle_pip = middle_pip
        self.middle_dip = middle_dip
        self.middle_tip = middle_tip
        self.ring_mcp = ring_mcp
        self.ring_pip = ring_pip
        self.ring_dip = ring_dip
        self.ring_tip = ring_tip
        self.pinky_mcp = pinky_mcp
        self.pinky_pip = pinky_pip
        self.pinky_dip = pinky_dip
        self.pinky_tip = pinky_tip

    # y is smaller in value when higher onscreen and greater in value when lower onscren
    # x is higher in value when right onscreen and lower in value when left on screen 

    def isDelete(self):
      if (abs(self.index_tip.y - self.thumb_tip.y) < 0.03 and self.index_tip.y > self.index_pip.y
          and self.ring_tip.y < self.pinky_tip.y and abs(self.middle_tip.x - self.ring_tip.x) > 0.05
          and abs(self.ring_tip.x - self.pinky_tip.x) > 0.06):
          return True
      return False  

    def isSpace(self):
        if (abs(self.index_tip.y - self.index_dip.y) < 0.03 and abs(self.index_tip.y - self.index_pip.y) < 0.03
            and abs(self.middle_tip.y - self.middle_dip.y) < 0.03 and abs(self.middle_tip.y - self.middle_pip.y) < 0.03
            and abs(self.ring_tip.y - self.ring_dip.y) < 0.03 and abs(self.ring_tip.y - self.ring_pip.y) < 0.03
            and abs(self.pinky_tip.y - self.pinky_dip.y) < 0.03 and abs(self.pinky_tip.y - self.pinky_pip.y) < 0.03):
            return True
        return False


    def isA(self):
       if (self.ring_tip.y > self.index_tip.y and self.ring_tip.y > self.middle_tip.y 
           and self.middle_tip.y > self.middle_dip.y and self.middle_tip.y > self.middle_pip.y
           and self.index_tip.y > self.index_dip.y and self.index_tip.y > self.index_pip.y
           and self.ring_tip.y > self.ring_dip.y and self.ring_tip.y > self.ring_pip.y
           and self.pinky_tip.y > self.pinky_dip.y and self.pinky_tip.y > self.pinky_pip.y
           and self.thumb_tip.y < self.index_dip.y and self.thumb_tip.y < self.middle_dip.y 
           and self.thumb_tip.y < self.ring_dip.y and self.thumb_tip.y < self.pinky_dip.y
           and abs(self.thumb_tip.x - self.index_pip.x) < 0.05):
           return True
       
       return False 
           
