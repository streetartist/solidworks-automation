# swDetailingDimTrailingZero_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDetailingDimTrailingZero_e`

Detailing dimension trailing zero styles.
Detailing dimension trailing zero styles.

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("B47AA95E-547C-444C-8A0F-C0AA015B2716")>
Public Enum swDetailingDimTrailingZero_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDetailingDimTrailingZero_e
```

```

[System.Runtime.InteropServices.Guid("B47AA95E-547C-444C-8A0F-C0AA015B2716")]
public enum swDetailingDimTrailingZero_e : System.Enum 
```

```

public enum swDetailingDimTrailingZero_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("B47AA95E-547C-444C-8A0F-C0AA015B2716")
public enum swDetailingDimTrailingZero_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("B47AA95E-547C-444C-8A0F-C0AA015B2716")]
__value public enum swDetailingDimTrailingZero_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("B47AA95E-547C-444C-8A0F-C0AA015B2716")]
public enum class swDetailingDimTrailingZero_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDimRemoveOnlyOnZero** | 4 = Remove only on zero |
| **swDimRemoveTrailingZeroes** | 2 =  Trailing zeroes do not appear |
| **swDimSameAsDimension** | 8 = Use the dimension's trailing zeroes setting |
| **swDimSameAsDocumentDimension** | 6 = Use the document dimension's trailing zeroes setting |
| **swDimSameAsDocumentTolerance** | 7 = Use the document tolerance's trailing zeroes setting |
| **swDimSameAsSource** | 5 = Use the source's trailing zeroes setting |
| **swDimShowTrailingZeroes** | 1 = Trailing zeroes appear |
| **swDimSmartTrailingZeroes** | 0 = OBSOLETE; do not use to set document properties |
| **swDimStandardTrailingZeroes** | 3 = OBSOLETE; do not use to set document properties |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDetailingDimTrailingZero\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
