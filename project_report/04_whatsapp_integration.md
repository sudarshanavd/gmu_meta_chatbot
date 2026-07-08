# 04. WhatsApp API Integration & Interest Decoder

The platform interfaces with Meta's WhatsApp Cloud API using structured Pydantic models to construct valid JSON payloads. This guarantees type-safety and automatic data validation before sending requests out to Meta.

---

## ✉️ WhatsApp Interactive Payload Types

### 1. Interactive Button Templates (`button`)
Used for high-level options (up to 3 buttons). 
*   **Use Cases**: Choosing academic levels (UG vs PG), linking to the website, or requesting specific course actions (Fees, Program Details).
*   **Constraint**: Button titles must not exceed 20 characters.
*   **Structure**:
    ```json
    {
      "messaging_product": "whatsapp",
      "recipient_type": "individual",
      "to": "WA_ID",
      "type": "interactive",
      "interactive": {
        "type": "button",
        "header": { "type": "text", "text": "Header Text" },
        "body": { "text": "Body description copy..." },
        "footer": { "text": "Footer details..." },
        "action": {
          "buttons": [
            { "type": "reply", "reply": { "id": "btn_1_id", "title": "Button Title" } }
          ]
        }
      }
    }
    ```

### 2. Interactive List Menus (`list`)
Used for selecting items from lists containing multiple categories.
*   **Use Cases**: Displaying faculties, schools, or individual branch options (up to 10 choices).
*   **Constraint**: List row titles must not exceed 24 characters.
*   **Structure**:
    ```json
    {
      "messaging_product": "whatsapp",
      "recipient_type": "individual",
      "to": "WA_ID",
      "type": "interactive",
      "interactive": {
        "type": "list",
        "header": { "type": "text", "text": "Select School" },
        "body": { "text": "Please choose your desired school from the list:" },
        "footer": { "text": "GMU Admissions" },
        "action": {
          "button": "View Schools",
          "sections": [
            {
              "title": "Available Schools",
              "rows": [
                { "id": "aaa", "title": "School of CS & Tech", "description": "Engineering & IT programs" }
              ]
            }
          ]
        }
      }
    }
    ```

### 3. CTA URL Buttons (`cta_url`)
Used to open external web links directly within the WhatsApp application.
*   **Use Case**: Pointing students directly to the GMU admissions portal web pages.
*   **Payload structure** (defined in `payload/website.py`):
    ```json
    "action": {
      "name": "cta_url",
      "parameters": {
        "display_text": "🌐 Visit Website",
        "url": "https://gmu.ac.in/"
      }
    }
    ```

---

## 🧩 The Interest Decoder Engine (`admissions/decoder.py`)

To compress data payloads and bypass WhatsApp character-limit constraints on Button/List IDs, the platform uses a **hierarchical encoding engine**. All user choices send back a compressed alphanumeric ID which the system dynamically translates.

### 1. Hierarchy Mapping Code Structure
*   **Level (Length 1)**: `A` = UG, `B` = PG
*   **Faculty (Length 2)**: Level + Faculty Identifier (e.g. `AA` = UG Faculty of Engineering & Tech)
*   **School (Length 3)**: Faculty + School Identifier (e.g. `AAA` = School of Computer Science and Technology)
*   **Branch (Length 4)**: School + Branch Identifier (e.g. `AAAA` = Computer Science and Engineering)
*   **Action Suffix (Length 5 or Conditional Length 4)**: Represents the leaf node action chosen by the student:
    *   `a`: "Program Details"
    *   `b`: "Fee & Duration"
    *   `c`: "Website / More Info"

### 2. Smart Length Detection Algorithm
```python
if len(code_str) >= 5:
    action_char = code_str[4].lower()
    base_code = code_str[:4]
elif len(code_str) == 4:
    # If 4 characters but NOT a known branch, and prefix is a known school,
    # then the 4th character is actually the action suffix!
    if not is_known_branch and is_known_school:
        action_char = code_str[3].lower()
        base_code = code_str[:3]
```

### 3. Alias & Legacy Support (`ALIASES`)
The decoder supports seamless mapping of alternate button and legacy IDs. For instance:
*   Mixed-case exceptions like Research (`afa` -> `AFa`) and M.Sc New Age (`bca` -> `BCa`) are mapped.
*   Legacy codes resulting from button ID adjustments are normalized to canonical forms (e.g., `bbce` maps correctly to `BCaA` representing *M.Sc Data Science*).
