#!/bin/env python3

import json

# Total DEC airdropped
DEC = 10000

# IBC DEC Token on Sentinel
IBCDEC   = 'ibc/B1C0DDB14F25279A2026BC8794E12B259F8BDA546A3C5132CCAEE4431CE36783'

# Load file of MathNodes Delegators
with open('delegators.json', 'r') as delegator_file:
    delegators = json.load(delegator_file)

total_delegated = 0
    
for d in delegators['delegation_responses']:
    # Skip team's delegation
    if "sent1vv8kmwrs24j5emzw8dp7k8satgea62l7knegd7" in d['delegation']['delegator_address']:
        continue
    else:
        total_delegated += int(d['balance']['amount'])
        

# Total Delegated DVPN minus team's delegation
total_delegated_dvpn = int(total_delegated / 1000000)
total_delegated_dvpn


# Transparency Files
delegation_pct_file    = open("address_pct.csv", 'w')
delegation_dec_file    = open("address_dec.csv", 'w')
delegation_mudec_file  = open("address_mudec.csv", 'w')
delegation_ibcdec_file = open("address_ibcdec.csv", 'w')

# Housekeeping
dec_amt_summed = 0 
k = 0

for d in delegators['delegation_responses']:
    delegator = d['delegation']['delegator_address']
    # Skip team's delegation
    if "sent1vv8kmwrs24j5emzw8dp7k8satgea62l7knegd7" in d['delegation']['delegator_address']:
        continue
    else:
        # Delegation percent of total delegated by delegator
        dec_pct  = round(float(int(float(int(d['balance']['amount']) / 1000000)) / total_delegated_dvpn),12)
        dec_amt  = round(float(DEC*dec_pct),6)
        
        # Write transparency files
        delegation_pct_file.write("%s,%s\n" % (delegator,dec_pct))
        delegation_dec_file.write("%s,%s\n" % (delegator, dec_amt))
        delegation_mudec_file.write("%s,%d\n" % (delegator,int(dec_amt*1000000)))
        delegation_ibcdec_file.write("%s,%d%s\n" % (delegator, int(dec_amt*1000000),IBCDEC))
        
        # Compute total dec summed
        dec_amt_summed += dec_amt
        print("%s,%d" % (delegator,int(dec_amt*1000000)))
    k += 1
    
print("Total Delegators: %d" % k)
print(dec_amt_summed)
delegation_pct_file.flush()
delegation_dec_file.flush()
delegation_mudec_file.flush()
delegation_ibcdec_file.flush()
delegation_pct_file.close()
delegation_dec_file.close()
delegation_mudec_file.close()
delegation_ibcdec_file.close()
    