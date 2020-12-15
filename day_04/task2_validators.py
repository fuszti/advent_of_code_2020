def get_validators_for_task2():
    def byr_valid(value):
        if len(value) != 4:
            return False
        for c in value:
            if not (int("0") <= int(c) <= int("9")):
                return False
        if int("1920") <= int(value) <= int("2002"):
            return True
        return False
    
    def iyr_valid(value):
        if len(value) != 4:
            return False
        for c in value:
            if not (int("0") <= int(c) <= int("9")):
                return False
        if int("2010") <= int(value) <= int("2020"):
            return True
        return False
    
    def eyr_valid(value):
        if len(value) != 4:
            return False
        for c in value:
            if not (int("0") <= int(c) <= int("9")):
                return False
        if int("2020") <= int(value) <= int("2030"):
            return True
        return False
    
    def hgt_valid(value):
        if len(value) < 4:
            return False
        if value[-2:] == "cm":
            if len(value) != 3+2:
                return False
            for c in value[:3]:
                if not (int("0") <= int(c) <= int("9")):
                    return False
            if int("150") <= int(value[:3]) <= int("193"):
                return True
        elif value[-2:] == "in":
            if len(value) != 2+2:
                return False
            for c in value[:2]:
                if not (int("0") <= int(c) <= int("9")):
                    return False
            if int("59") <= int(value[:2]) <= int("76"):
                return True
        return False
    
    def hcl_valid(value):
        if len(value) != 7:
            return False
        if value[0] != "#":
            return False
        for c in value[1:]:
            if not ("0" <= c <= "9" or "a" <= c <= "f"):
                return False
        return True
    
    def ecl_valid(value):
        valid_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return value in valid_values
    
    def pid_valid(value):
        if len(value) != 9:
            return False
        return "0"*9 <= value <= "9"*9
    
    def cid_valid(value):
        return True
    
    validators = {
    "byr": byr_valid,
    "iyr": iyr_valid,
    "eyr": eyr_valid,
    "hgt": hgt_valid,
    "hcl": hcl_valid, 
    "ecl": ecl_valid,
    "pid": pid_valid, 
    "cid": cid_valid
    }
    return validators