# Use-Case Flow Specification

## Use Case: Grant Time-Bound Consent

**Primary Actor:** Patient

**Supporting Actor:** Clinic Administrator

### Preconditions

1. The patient is registered and authenticated in the system.
2. The patient has access to their health records.
3. The healthcare provider is registered and can be verified by the system.

### Postconditions

1. A consent permission is created for the selected healthcare provider.
2. The selected diagnostic records are accessible only for the specified consent period.
3. The consent automatically becomes inactive when the expiry time is reached.
4. The consent grant event is recorded in the audit trail.

### Main Success Scenario

1. The patient logs into the Patient Health Record Consent Management System.
2. The patient selects the diagnostic records they want to share.
3. The patient selects the healthcare provider who should receive access.
4. The patient specifies the duration or expiry time for the consent.
5. The system verifies the selected healthcare provider.
6. The system displays the selected records, provider, and consent duration for confirmation.
7. The patient confirms the consent.
8. The system creates the time-bound consent permission.
9. The system records the consent grant event in the audit trail.
10. The system confirms that the consent has been successfully granted.

### Alternate Flow

**A1. Healthcare provider cannot be verified**

1. At Step 5, if the selected healthcare provider cannot be verified, the system rejects the consent request.
2. The system informs the patient that the provider could not be verified.
3. No consent permission is created.
4. The patient may select another verified healthcare provider and restart the consent process.
