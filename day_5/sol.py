def get_data(test=False):
    filename = "input.txt" if not test else "test_input.txt"
    rules, to_produce_sequence = [
        part for part in open(filename).read().split("\n\n") if part != ""
    ]

    rules = [rule.split("|") for rule in rules.splitlines()]
    to_produce_sequence = [seq.split(",") for seq in to_produce_sequence.splitlines()]

    return rules, to_produce_sequence


def get_index(lst, val):
    try:
        return lst.index(val)
    except ValueError:
        return None


def get_part1_output(rules, to_produce_sequence, return_incorrect_seqs_for_part2=False):
    middle_vals = []
    for_part2_incorrect_seqs = []

    for seq in to_produce_sequence:
        rules_passed = []
        for rule_before, rule_after in rules:
            rule_bef_idx = get_index(seq, rule_before)
            rule_aft_idx = get_index(seq, rule_after)

            # continue if rule is not in it
            if None in (rule_bef_idx, rule_aft_idx):
                continue

            if rule_bef_idx < rule_aft_idx:
                rules_passed.append(True)
            else:  # skip if any rule fails
                rules_passed.append(False)
                break

        if all(rules_passed):  # Append here to avoid multiple same seq middle in it
            middle_vals.append(int(seq[len(seq) // 2]))
        else:
            for_part2_incorrect_seqs.append(seq)

    if return_incorrect_seqs_for_part2:
        return middle_vals, for_part2_incorrect_seqs
    print("middle_vals: ", middle_vals)
    return sum(middle_vals)


test_rules, test_to_produce_sequence = get_data(test=True)
rules, to_produce_sequence = get_data()

# Part 2
print("=== Part 1 ===")
TEST_OUT_SHOULD_BE = 143

print("=> Test <=")
out = get_part1_output(test_rules, test_to_produce_sequence)
print("Test passes: ", out == TEST_OUT_SHOULD_BE, " value: ", out)

print("=> Run <=")
out = get_part1_output(rules, to_produce_sequence)
print("Result: ", out)


# Part 2
def fix_seq(seq, rules):
    new_seq = seq.copy()
    for val in seq:
        curr_rules = [rule for rule in rules if rule[0] == val]
        for rule_before, rule_after in curr_rules:
            rule_bef_idx = get_index(new_seq, rule_before)  # same as index of "val"
            rule_aft_idx = get_index(new_seq, rule_after)

            if rule_aft_idx is not None and rule_bef_idx > rule_aft_idx:
                new_seq.remove(val)
                new_seq.insert(rule_aft_idx, val)

    return new_seq


def get_part2_output(rules, to_produce_sequence):
    out, incorrect_seqs = get_part1_output(
        rules, to_produce_sequence, return_incorrect_seqs_for_part2=True
    )

    new_fixed_seqs = []
    for seq in incorrect_seqs:
        new_seq = fix_seq(seq, rules)
        new_fixed_seqs.append(new_seq)

    if len(new_fixed_seqs) == 0:
        return None

    return get_part1_output(rules, new_fixed_seqs)


print("=== Part 2 ===")
PART2_TEST_OUT_SHOULD_BE = 123

print("=> Test <=")
out = get_part2_output(test_rules, test_to_produce_sequence)
print("Test passes: ", out == PART2_TEST_OUT_SHOULD_BE, " value: ", out)

print("=> Run <=")
out = get_part2_output(rules, to_produce_sequence)
print("Result: ", out)