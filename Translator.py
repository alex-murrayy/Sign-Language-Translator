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

    def isA(self):
       if self.ring_tip.y < self.index_tip.y and self.ring_tip.y < self.middle_tip.y:
           return False 
       
       return True 
           
