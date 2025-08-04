# middleware/odg.py
import sqlite3
from typing import Dict

DB_PATH = "logs/ops_log.db"

def check_user_generated_dependency(current_op: Dict) -> bool:
    """
    Check whether the current operation has any user-generated dependency (UGD)
    based on previous operations in the system.
    This is a simplified placeholder based on temporal and key-based analysis.
    """
    user_id = current_op.get("user_id")
    y_id = current_op.get("y_id")
    timestamp = current_op.get("timestamp")

    if not (user_id and y_id and timestamp):
        return False

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Check if other users accessed the same key (y_id) before this operation
        query = """
            SELECT user_id, operation, timestamp
            FROM logs
            WHERE y_id = ? AND user_id != ? AND timestamp <= ?
        """
        cursor.execute(query, (y_id, user_id, timestamp))
        results = cursor.fetchall()

        conn.close()

        if results:
            return True
        return False

    except Exception as e:
        print(f"[ODG] Error checking UGD: {e}")
        return False
