# Real Power Automate Flow Details

Trigger: When a HTTP request is received (POST)
Uncertain range: 0.45 - 0.55

Actions in the flow:
1. Parse JSON from FastAPI
2. Condition: probability between 0.45 and 0.55
3. Create item in SharePoint list "Prediction Reviews"
4. Send notification in Teams to reviewer
5. Wait for reviewer feedback
6. (Optional) Update back to database

This provides proper human-in-the-loop safety for uncertain predictions.
