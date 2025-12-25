def attach_policies_to_case(case, policy_chunks):
    matched_policies = []

    claim_type = case["claim_type"].lower()
    state = case["state"].lower()

    for chunk in policy_chunks:
        content = chunk["text"].lower()

        if claim_type in content and state in content:
            matched_policies.append(chunk)

    return matched_policies
