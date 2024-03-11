from blockchain import blockexplorer

addr = blockexplorer.get_address('') # hash address of a Wallet

layer_p1 = []
layer_n1 = []
for trans in addr.transactions:                             ## for all transaction of my address(addr)
    if trans.inputs[0].address == addr.address:             ## this if check deposit transaction or received transaction
        # Deposit
        for out in trans.outputs:                           ## this for loop for find address of outputs  
            if (out.address != addr.address) and (out.address not in layer_p1):             ## and this if check deposit transaction and check duplicate address in list
                layer_p1.append(out.address)                ## finally append address to a list
    else:                                                   ### this else for received transaction 
        # Received
        for inp in trans.inputs:                            ### this for loop for find address of inputs
            if (inp.address != addr.address) and (inp.address not in layer_n1):             ### ## and this if check received transaction and check duplicate address in list
                layer_n1.append(inp.address)                ### finally append address to a list

print('the addresses of layer +1 are: ',layer_p1)
print()
print('the addresses of layer -1 are: ',layer_n1)

layer_p2 = []
for address_p1 in layer_p1:                                 ## for each address in layer_p1
    addr_p1 = blockexplorer.get_address(address_p1)         ## get address of each address in layer_p1
    for trans in addr_p1.transactions:                      ##### other sections are same with above section ####
        if trans.inputs[0].address == address_p1:
        # Deposit
            for out in trans.outputs:
                if (out.address != address_p1) and (out.address not in layer_p2):
                    layer_p2.append(out.address)

layer_n2 = []
for address_n1 in layer_n1:                                 ## for each address in layer_n1
    addr_n1 = blockexplorer.get_address(address_n1)         ## get address of each address in layer_p1
    for trans in addr_n1.transactions:                      ##### other sections are same with above section ####
        if trans.inputs[0].address != address_n1:
        # Received
            for inp in trans.inputs:
                if (inp.address != address_n1) and (inp.address not in layer_n2):
                    layer_n2.append(inp.address)


# print('the addresses of layer +2 are: ',layer_p2)
# print()
# print('the addresses of layer -2 are: ',layer_n2)


layer_p3 = []
for address_p2 in layer_p2:
    addr_p2 = blockexplorer.get_address(address_p2)
    for trans in addr_p2.transactions:
        if trans.inputs[0].address == address_p2:
        # Deposit
            for out in trans.outputs:
                if (out.address != address_p2) and (out.address not in layer_p3):
                    layer_p3.append(out.address)

layer_n3 = []
for address_n2 in layer_n2:
    addr_n2 = blockexplorer.get_address(address_n2)
    for trans in addr_n2.transactions:
        if trans.inputs[0].address != address_n2:
        # Received
            for inp in trans.inputs:
                if (inp.address != address_n2) and (inp.address not in layer_n3):
                    layer_n3.append(inp.address)

# print('the addresses of layer +3 are: ',layer_p3)
# print()
# print('the addresses of layer -3 are: ',layer_n3)



layer_p4 = []
for address_p3 in layer_p3:
    addr_p3 = blockexplorer.get_address(address_p3)
    for trans in addr_p3.transactions:
        if trans.inputs[0].address == address_p3:
        # Deposit
            for out in trans.outputs:
                if (out.address != address_p3) and (out.address not in layer_p3):
                    layer_p3.append(out.address)

layer_n4 = []
for address_n3 in layer_n3:
    addr_n3 = blockexplorer.get_address(address_n3)
    for trans in addr_n3.transactions:
        if trans.inputs[0].address != address_n3:
        # Received
            for inp in trans.inputs:
                if (inp.address != address_n3) and (inp.address not in layer_n4):
                    layer_n4.append(inp.address)


# print('the addresses of layer +4 are: ',layer_p4)
# print()
# print('the addresses of layer -4 are: ',layer_n4)