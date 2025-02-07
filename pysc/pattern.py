
PySCOpenDelims = {'{', '(', '['}
PySCCloseDelims = {'}', ')', ']'}

PySCEmbbedComment = r"\s*<#.*?#>\s*"
PySCSimpleComment = r"\s*(?<!<)#(?!>).*"

PySCOpenComment = r"\s*<#(?!>)(.*)"
PySCCloseComment = r"((?!<#).)*(?<!<)#>\s*"
