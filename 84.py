# the following's the beginning of a function that might need to be recurred until the values stabilize
roll_p = 1.0 / 40.0
# TODO: set all squares to the roll_p initially
three_doubles_p = 1.0 / 64.0
roll_probabilities = {
    'trivial' : (1.0 - three_doubles_p) * roll_p,
    'jail' : roll_p + three_double_p
}
ch_stay_p = 6.0 / 16.0
roll_probabilities['ch'] = roll_probabilities['trivial'] * ch_stay_p
ch_leave_share = roll_probabilities['trivial'] / 16.0
roll_probabilities['go'] = roll_probabilities['trivial'] + ch_leave_share
roll_probabilities['jail'] += ch_leave_share
roll_probabilities['c1'] = roll_probabilities['trivial'] + ch_leave_share
roll_probabilities['e3'] = roll_probabilities['trivial'] + ch_leave_share
roll_probabilities['h2'] = roll_probabilities['trivial'] + ch_leave_share
roll_probabilities['r1'] = roll_probabilities['trivial'] + 3 * ch_leave_share
roll_probabilities['r2'] = roll_probabilities['trivial'] + 2 * ch_leave_share
roll_probabilities['r3'] = roll_probabilities['trivial'] + 2 * ch_leave_share
roll_probabilities['u1'] = roll_probabilities['trivial'] + 2 * ch_leave_share
roll_probabilities['u2'] = roll_probabilities['trivial'] + ch_leave_share
roll_probabilities['t1'] = roll_probabilities['trivial'] + ch_leave_share
roll_probabilities['d3'] = roll_probabilities['trivial'] + ch_leave_share
roll_probabilities['cc3'] = roll_probabilities['trivial'] + ch_leave_share

cc_stay_p = 7.0 / 8.0

roll_probabilities['cc1'] = roll_probabilities['trivial'] * cc_stay_p
roll_probabilities['cc2'] = roll_probabilities['trivial'] * cc_stay_p
roll_probabilities['cc3'] *= roll_probabilities * cc_stay_p

roll_probabilities['_all_cc'] = roll_probabilities['cc1'] + roll_probabilities['cc2'] + roll_probabilities['cc3']

# at the end, using the new probabilities, calculate the new roll probabilities
# recur?