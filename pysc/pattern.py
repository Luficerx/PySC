
PySCOpenDelims = {'{', '(', '['}
PySCCloseDelims = {'}', ')', ']'}

# PySCComposedComment = r"\s*<#>.*(?=\n|$)"
PySCEmbbedComment = r"\s*<#.*?#>\s*"
PySCSimpleComment = r"\s*#.*"

PySCOpenComment = r"\s*<#(?!>)(.*)"
PySCCloseComment = r"(.*)(?<!<)#>\s*"

PySCInvalidOpenComment = r"^\s*(\S.*?)<#(?!>)"
PySCInvalidCloseComment = r"(.*)(?<!<)#>\s*(\S.*?)"

PySCHead = r"(^\$\s*[a-zA-Z]+[a-zA-Z0-9]*\s+****\s*:)|(^****\s*:)"
PySCHeadExpr = r"^\$\s*([a-zA-Z]+[a-zA-Z0-9]*)\s+(****\s*):|^(****)\s*:"
PySCList = r""
PySCDict = r""
PySCTuple = r""
PySCSet = r""