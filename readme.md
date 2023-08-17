# Vendor Payment Enhancement Module for Odoo Version 16 Enterprise

---

### **1. Introduction:**

This SRS document describes the functional requirements and test conditions for the Vendor Payment Enhancement module for Odoo V16 Enterprise, which aims to simplify and automate the vendor payment process for the finance department.

---

### **2. Functional Requirements:**

#### **2.1. Vendor Bill Inspection:**

- **2.1.1.** Vendors can send bills to Odoo via email.
- **2.1.2.** Junior accountants can inspect received vendor bills on Odoo to verify their accuracy.

#### **2.2. Bill Discrepancy Identification and Notification:**

- **2.2.1.** If the junior accountant determines a discrepancy in the bill, they can select specific reasons from a pre-defined list.
  
**Reasons for discrepancies:**

  1. Company address is false
  2. Not correct VAT ID
  3. The invoice should have a 0% VAT rate, reversed charge
  4. The invoice should have a 19% VAT rate
  5. Wrong invoice amount
  6. The invoice must be made out in euros
  7. Proof of delivery is false
  8. Proof of delivery is not readable
  9. Proof of delivery is missing

- The reasons are available in an Odoo list-view under the vendor bill management menu, and can be edited directly on the list view.
- The list is multi-lingual compatible.
- After selecting the discrepancy reason(s), the accountant can launch an email wizard, which incorporates these reasons into a predefined mail template.
- Once the discrepancy email is sent to the vendor, Odoo automatically marks the respective vendor bill as "to be verified."

#### **2.3. SEPA XML Transfer File Generation:**

- All vendor bills ready for payment are listed under a favorite named "bills payable this week."
- A senior accountant can select multiple bills from this list view.
- Upon selection, the senior accountant can generate a single SEPA XML transfer file via the Action menu.
- This file can be directly uploaded to the company's online banking portal to initiate payments after necessary bank authentication.

Implement the SEPA XML payment method modularly in a separate class-file. There will be other payment modes possible in future, ex. finapi.io etc.

---

### **3. Test Conditions:**

1. A bill sent by a vendor via email should be accessible to the junior accountant for inspection.
2. Discrepancy reasons can be edited and saved successfully in the Odoo list view.
3. Selecting a discrepancy reason should integrate it into the mail template correctly.
4. After sending the discrepancy email, the respective vendor bill status should update to "to be verified."
5. The favorite "bills payable this week" should correctly display all vendor bills eligible for payment.
6. The SEPA XML transfer file generation should complete without errors and should be in the correct format for bank uploads.
7. The module should be compatible with Odoo Version 16 Enterprise without causing any conflicts with existing functionality.

---

**Note:** This SRS provides a high-level overview of the functionality and expected behavior of the Vendor Payment Enhancement module for Odoo. 
It serves as a guideline for development, and further detailed specifications can be provided as needed during the development phase.
