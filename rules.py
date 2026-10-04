RULES = [
    ("DQ001", "Missing member ID", "SELECT COUNT(*) FROM warehouse_claims WHERE member_id IS NULL OR TRIM(member_id) = ''", 0),
    ("DQ002", "Duplicate claim ID", "SELECT COUNT(*) FROM (SELECT claim_id FROM warehouse_claims GROUP BY claim_id HAVING COUNT(*) > 1)", 0),
    ("DQ003", "Negative paid amount", "SELECT COUNT(*) FROM warehouse_claims WHERE paid_amount < 0", 0),
    ("DQ004", "Invalid claim status", "SELECT COUNT(*) FROM warehouse_claims WHERE claim_status NOT IN ('PAID','DENIED','PENDING')", 0),
    ("DQ005", "Submitted before service", "SELECT COUNT(*) FROM warehouse_claims WHERE date(submitted_date) < date(service_date)", 0),
    ("DQ006", "Paid exceeds charge", "SELECT COUNT(*) FROM warehouse_claims WHERE paid_amount > charge_amount", 0),
    ("DQ007", "Source-to-target row count", "SELECT ABS((SELECT COUNT(*) FROM source_claims) - (SELECT COUNT(*) FROM warehouse_claims))", 0),
    ("DQ008", "Null claim ID", "SELECT COUNT(*) FROM warehouse_claims WHERE claim_id IS NULL OR TRIM(claim_id) = ''", 0),
]
