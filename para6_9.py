import warnings

warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('error', ImportWarning)

warnings.warn("warnings, no code here", SyntaxWarning)
try:
    warnings.warn('warnings, module not import', ImportWarning )
except:
    print("warning processed")



