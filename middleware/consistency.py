# middleware/consistency.py
import time
import logging
from middleware.utils import log_operation, get_last_op_for_user
from middleware.odg import check_user_generated_dependency

def handle_stcc_logic(op: dict):
    """
    Determine which STCC consistency guarantees should be applied based on the operation type and context.
    Returns a dictionary containing the activated consistency checks.
    """
    op_type = op.get("operation", "").upper()
    user_id = op.get("user_id", "")
    y_id = op.get("y_id", "")

    if not op_type or not user_id or not y_id:
        raise ValueError("Invalid operation. Must include 'operation', 'user_id', and 'y_id'.")

    timestamp = int(time.time() * 1000)
    op["timestamp"] = timestamp
    log_operation(user_id, op)

    consistency_enforced = {
        "monotonic_read": False,
        "monotonic_write": False,
        "read_your_write": False,
        "write_follow_read": False,
        "user_generated_dependency": False
    }

    last_op = get_last_op_for_user(user_id)

    # === Local Client-Side Checks ===
    if op_type == "READ":
        if last_op:
            if last_op["operation"] == "READ" and op["timestamp"] >= last_op["timestamp"]:
                consistency_enforced["monotonic_read"] = True
            if last_op["operation"] in ["INSERT", "UPDATE", "DELETE"]:
                consistency_enforced["read_your_write"] = True

    elif op_type in ("INSERT", "UPDATE", "DELETE"):
        if last_op:
            if last_op["operation"] in ("INSERT", "UPDATE", "DELETE") and op["timestamp"] >= last_op["timestamp"]:
                consistency_enforced["monotonic_write"] = True
            if last_op["operation"] == "READ":
                consistency_enforced["write_follow_read"] = True

    # === Cross-User Dependencies (UGD) ===
    if check_user_generated_dependency(op):
        consistency_enforced["user_generated_dependency"] = True

    logging.info(f"[STCC] Operation: {op_type}, User: {user_id}, y_id: {y_id}, Enforced: {consistency_enforced}")

    return {
        "operation": op,
        "consistency_applied": consistency_enforced
    }
