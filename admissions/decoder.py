"""
Course-code decoder for GM University WhatsApp Admissions bot.
Supports the new official GMU maroon and gold brand palette,
converting old/alternate lowercase and positional codes to clean canonical labels.
"""

LEVEL = {
    "A": "UG",
    "B": "PG",
}

FACULTY = {
    # UG (A)
    "AA": "Faculty of Engineering and Technology",
    "AB": "Faculty of Commerce and Management",
    "AC": "GM School of Law",
    "AD": "Faculty of Basic and Applied Sciences",
    "AE": "Faculty of Computing and IT",
    "AF": "Research Programs (PhD)",
    "AG": "B.Voc",
    # PG (B)
    "BA": "GM School of Advanced Studies",
    "BB": "Faculty of Basic & Applied Sciences",
    "BC": "Faculty of Computing & IT",
    "BD": "Faculty of Commerce & Management",
    "BF": "GM Business School",
    "BG": "Post Graduate Diploma (PgD)",
}

SCHOOL = {
    # UG FET (AA)
    "AAA": "School of Computer Science and Technology",
    "AAB": "School of Engineering",
    # UG FCM (AB)
    "ABA": "School of Commerce",
    "ABB": "School of Management",
    # UG Law (AC)
    "ACA": "LL.B.",
    "ACB": "B.B.A., LL.B. (Integrated)",
    "ACC": "B.Com., LL.B. (Integrated)",
    # UG FBAS (AD)
    "ADA": "School of Mathematical and Physical Sciences",
    "ADB": "School of Chemical and Biological Sciences",
    "ADC": "School of Applied Sciences",
    # UG FCIT (AE)
    "AEA": "School of Computer Application",
    "AEB": "School of Computer Science",
    # UG Research (AF)
    "AFa": "Research Programs (PhD)",
    # UG B.Voc (AG)
    "AGa": "B.Voc Programs",
    
    # PG Advanced Studies (BA)
    "BAA": "M.Tech",
    # PG Basic Sciences (BB)
    "BBA": "M.Sc",
    # PG Computing (BC)
    "BCA": "MCA",
    "BCa": "M.Sc (New Age Programs)",
    # PG Commerce & Management (BD)
    "BDA": "M.Com",
    # PG GM Business School (BF)
    "BFA": "MBA",
    # PG Post Graduate Diploma (BG)
    "BGA": "Post Graduate Diploma Programs",
}

BRANCH = {
    # SCST (AAA)
    "AAAA": "Computer Science and Engineering (CSE)",
    "AAAB": "Information Science and Engineering (ISE)",
    "AAAC": "Computer Science – AI & ML",
    "AAAD": "Computer Science – AI, Blockchain & Business Systems",
    "AAAE": "Computer Science – IoT with AI",
    "AAAF": "Computer Science – Data Science",
    "AAAG": "Computer Science – Cyber Security",
    "AAAH": "Computer Science – Cloud Computing",
    "AAAI": "Computer Science – Information Security",
    # SE (AAB)
    "AABA": "Electronics and Communication Engineering (E&CE)",
    "AABB": "Electrical and Electronics Engineering (EEE)",
    "AABC": "Robotics and Automation (RA)",
    "AABD": "Engineering Design (ED)",
    "AABE": "Civil Engineering (CE)",
    "AABF": "Biotechnology (BT)",
    "AABG": "Mechanical Engineering (ME)",
    "AABH": "Electrical & Electronics Engineering (Evening)",
    "AABI": "Civil Engineering (Evening)",
    # School of Commerce (ABA)
    "ABAA": "General",
    "ABAB": "Data Analytics and Business Intelligence",
    "ABAC": "AI and Business Analytics",
    "ABAD": "Accounting and Taxation",
    # School of Management (ABB)
    "ABBA": "General",
    "ABBB": "Blockchain and FinTech",
    "ABBC": "AI and Business Analytics",
    "ABBD": "Digital Marketing and E-Commerce",
    "ABBE": "Aviation Management",
    "ABBF": "Tourism, Hospitality and Event Management",
    "ABBG": "Healthcare Management",
    # School of Mathematical and Physical Sciences (ADA)
    "ADAA": "Physics, Mathematics",
    "ADAB": "Mathematics, Computer Science",
    "ADAC": "Statistics, Computer Science",
    # School of Chemical and Biological Sciences (ADB)
    "ADBA": "Physics, Chemistry",
    "ADBB": "Chemistry, Computer Science",
    "ADBC": "Chemistry, Zoology",
    "ADBD": "Chemistry, Botany",
    "ADBE": "Chemistry, Environmental Science",
    # School of Applied Sciences (ADC)
    "ADCA": "Food Science and Technology",
    "ADCB": "Biotechnology and Tissue Engineering",
    "ADCC": "Industrial Microbiology",
    # School of Computer Application (AEA)
    "AEAA": "General",
    # School of Computer Science (AEB)
    "AEBA": "Data Science",
    "AEBB": "Cyber Security",
    "AEBC": "AI and Data Analytics",
    # Research Programs (AFa)
    "AFaA": "Faculty of Engineering and Technology",
    "AFaB": "Faculty of Computing and IT",
    "AFaC": "Faculty of Basic and Applied Sciences",
    "AFaD": "Faculty of Commerce and Management",
    # B.Voc (AGa)
    "AGaA": "Electrical Vehicle Technology",
    "AGaB": "Fashion Design and Apparel Manufacture",
    "AGaC": "Drone Development and Application",
    "AGaD": "Airport Ground Services and Support",
    "AGaE": "E-Commerce and Digital Marketing",
    "AGaF": "Animation and Visual Effects",
    
    # PG Advanced Studies (BAA)
    "BAAA": "Deep Learning",
    "BAAB": "AI in Healthcare",
    "BAAC": "Data Engineering",
    "BAAD": "CASE",
    "BAAE": "Smart Electrical Systems",
    "BAAF": "Advanced Electronics",
    "BAAG": "Bioengineering",
    "BAAH": "Product Development",
    "BAAI": "Smart & Green Agriculture",
    "BAAJ": "Industrial IoT",
    "BAAK": "Semiconductor Technology",
    # M.Sc (BBA)
    "BBAA": "Physics",
    "BBAB": "Chemistry",
    "BBAC": "Mathematics",
    "BBAD": "Food Technology",
    # MCA (BCA)
    "BCAA": "General",
    "BCAB": "Data Science",
    "BCAC": "Cyber Security",
    "BCAD": "AI & Data Analytics",
    # M.Sc New Age (BCa)
    "BCaA": "Data Science",
    "BCaB": "AI & Data Analytics",
    "BCaC": "Cyber Security",
    # M.Com (BDA)
    "BDAA": "Applied Finance & Digital Business",
    "BDAB": "FinTech Analytics & Entrepreneurship",
    # MBA (BFA)
    "BFAA": "General",
    "BFAB": "Professional",
    "BFAC": "Advanced",
    "BFAD": "International",
    # PgD (BGA)
    "BGAA": "AI & IoT (with Intel)",
    "BGAB": "Embedded Systems (with Texas Instruments)",
    "BGAC": "Accounting & Finance (with Tally)",
}

# Mapping of old/alternate lowercase codes to new canonical uppercase/mixed-case codes.
# Only contains mappings that cannot be resolved by simple upper() conversion,
# or legacy non-colliding aliases.
ALIASES = {
    # Mixed-case schools
    "afa": "AFa",  # Research (PhD)
    "aga": "AGa",  # B.Voc
    "bca": "BCa",  # M.Sc (New Age Programs) - note: MCA is BCAA/BCAB/etc, while BCa is BCaA/BCaB/etc.

    # Mixed-case Research branches (AFaA - AFaD)
    "afaa": "AFaA",
    "afab": "AFaB",
    "afac": "AFaC",
    "afad": "AFaD",
    
    # Mixed-case B.Voc branches (AGaA - AGaF)
    "agaa": "AGaA",
    "agab": "AGaB",
    "agac": "AGaC",
    "agad": "AGaD",
    "agae": "AGaE",
    "agaf": "AGaF",
    
    # M.Sc New Age Programs unique button/legacy IDs
    "bcae": "BCaA",  # M.Sc Data Science
    "bcaf": "BCaB",  # M.Sc AI & Data Analytics
    "bcag": "BCaC",  # M.Sc Cyber Security
    "bbce": "BCaA",
    "bbcf": "BCaB",
    "bbcg": "BCaC",
    "abce": "BCaA",
    "abcf": "BCaB",
    "abcg": "BCaC",
}

ACTION_SUFFIX = {
    "a": "Program Details",
    "b": "Fee & Duration",
    "c": "Website / More Info",
}

def decode_interest(code: str) -> dict:
    """
    Decode a WhatsApp button/list reply ID into human-readable program fields.
    Handles extra characters (e.g. bdcaa -> bdca + action a).
    Handles lowercase or case-insensitive inputs and maps to official codes.
    """
    if not code or not isinstance(code, str):
        return {
            "raw_code": code, "level": "Unknown", "faculty": "Unknown",
            "school": "Unknown", "branch": "Unknown", "action": None, "label": "Unknown"
        }

    code_str = code.strip()
    
    action_char = None
    base_code = code_str
    
    # Smart length detection:
    # 1. If length >= 5, 5th character is the action character, first 4 is the base code.
    if len(code_str) >= 5:
        action_char = code_str[4].lower()
        base_code = code_str[:4]
    elif len(code_str) == 4:
        # If length is 4, check if it's a known branch code.
        # If it is NOT a known branch, but the 3-character prefix is a known school/program,
        # then the 4th character is the action character!
        upper_code = code_str.upper()
        lower_code = code_str.lower()
        is_known_branch = (
            upper_code in BRANCH or 
            lower_code in ALIASES or 
            (lower_code in ALIASES and ALIASES[lower_code] in BRANCH)
        )
        if not is_known_branch:
            prefix_3 = code_str[:3]
            upper_prefix_3 = prefix_3.upper()
            lower_prefix_3 = prefix_3.lower()
            is_known_school = (
                upper_prefix_3 in SCHOOL or
                lower_prefix_3 in ALIASES or
                (lower_prefix_3 in ALIASES and ALIASES[lower_prefix_3] in SCHOOL)
            )
            if is_known_school:
                action_char = code_str[3].lower()
                base_code = code_str[:3]

    # 2. Canonicalize the base code using ALIASES or default to uppercase
    lower_base = base_code.lower()
    if lower_base in ALIASES:
        canon_code = ALIASES[lower_base]
    else:
        # For mixed-case codes, they are already mapped in ALIASES.
        # Anything else is safe to convert to uppercase.
        canon_code = base_code.upper()

    # 3. Decode components from canon_code
    result = {
        "raw_code": code,
        "level": "Unknown",
        "faculty": "Unknown",
        "school": "Unknown",
        "branch": "Unknown",
        "action": ACTION_SUFFIX.get(action_char),
        "label": "Unknown"
    }

    if len(canon_code) >= 1:
        result["level"] = LEVEL.get(canon_code[0], "Unknown")
        
    if len(canon_code) >= 2:
        result["faculty"] = FACULTY.get(canon_code[:2], "Unknown")
        
    if len(canon_code) >= 3:
        result["school"] = SCHOOL.get(canon_code[:3], "Unknown")
        
    if len(canon_code) == 4:
        result["branch"] = BRANCH.get(canon_code, "Unknown")

    # 4. Build clean human-readable label
    parts = []
    if result["level"] != "Unknown":
        parts.append(result["level"])
    if result["faculty"] != "Unknown":
        parts.append(result["faculty"])
    if result["school"] != "Unknown":
        parts.append(result["school"])
    if result["branch"] != "Unknown":
        parts.append(result["branch"])

    if parts:
        result["label"] = " › ".join(parts)
    else:
        result["label"] = f"Unknown Code ({code})"

    return result
