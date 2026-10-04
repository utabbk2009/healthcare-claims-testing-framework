-- Missing required member IDs
SELECT * FROM warehouse_claims
WHERE member_id IS NULL OR TRIM(member_id) = '';

-- Duplicate claim IDs
SELECT claim_id, COUNT(*) AS duplicate_count
FROM warehouse_claims
GROUP BY claim_id
HAVING COUNT(*) > 1;

-- Invalid financial values
SELECT * FROM warehouse_claims
WHERE paid_amount < 0 OR paid_amount > charge_amount;

-- Invalid workflow values
SELECT * FROM warehouse_claims
WHERE claim_status NOT IN ('PAID', 'DENIED', 'PENDING');

-- Service/submission sequence errors
SELECT * FROM warehouse_claims
WHERE date(submitted_date) < date(service_date);
