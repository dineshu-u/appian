import streamlit as st
from ingestion.document_loader import load_policy_documents
from mapping.policy_mapping_layer import attach_policies_to_case

st.set_page_config(page_title="Case-Aware Policy Attachment System")

st.title("Case-Aware Policy Attachment System")
st.caption("Relevant policy rules automatically attached to the case")

claim_type = st.text_input("Claim Type", "Flood")
state = st.text_input("State", "Florida")

if st.button("Attach Relevant Policies"):
    case = {
        "claim_type": claim_type,
        "state": state
    }

    policy_chunks = load_policy_documents("data/policies")
    results = attach_policies_to_case(case, policy_chunks)

    if results:
        st.subheader("Relevant Policy Clauses")
        for item in results:
            st.markdown(f"**Document:** {item['document']}")
            st.markdown(f"**Page:** {item['page']}")
            st.write(item["text"])
            st.markdown("---")
    else:
        st.warning("No matching policy clauses found.")
