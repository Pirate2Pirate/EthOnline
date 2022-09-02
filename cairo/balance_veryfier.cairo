%builtins output range_check

from starkware.cairo.common.serialize import serialize_word
from starkware.cairo.common.math import assert_le

func main{output_ptr : felt*, range_check_ptr}():

    alloc_locals 

    local address: felt
    local amount: felt
    local balance: felt
    local tx_id: felt

    # There must be some security concerns
    %{
        ids.address = program_input['address']
        ids.amount = program_input['amount']
        ids.balance = program_input['balance']
        ids.tx_id = program_input['tx_id']
    %}

    assert_le(amount,balance)

    serialize_word(address)
    serialize_word(tx_id)
    return()
end
