def power(base,exp):
    if exp == 1:
        return base
    else:
        return(base * power(base,exp-1))

base = 2
exp = 3
print(f"Base is {base} Power is {exp} = ",power(base,exp))