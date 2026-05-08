# swCheckSpellingOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckSpellingOptions_e`

Spell check options. Bitmask.
Spell check options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("68F4EFBC-5A91-437B-8F79-5CEFB7F99D45")>
Public Enum swCheckSpellingOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCheckSpellingOptions_e
```

```

[System.Runtime.InteropServices.Guid("68F4EFBC-5A91-437B-8F79-5CEFB7F99D45")]
public enum swCheckSpellingOptions_e : System.Enum 
```

```

public enum swCheckSpellingOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("68F4EFBC-5A91-437B-8F79-5CEFB7F99D45")
public enum swCheckSpellingOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("68F4EFBC-5A91-437B-8F79-5CEFB7F99D45")]
__value public enum swCheckSpellingOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("68F4EFBC-5A91-437B-8F79-5CEFB7F99D45")]
public enum class swCheckSpellingOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSpellingIgnoreCapitalizedWords** | 8 or 0x8; Capitalized words are not checked |
| **swSpellingIgnoreInternetAndFiles** | 16 or 0x10; Words containing a web address are not checked |
| **swSpellingIgnoreMixedCase** | 2 or 0x2; Words that are mixed-case (upper case and lowercase, e.g., eDrawings) are not checked |
| **swSpellingIgnoreUpperCase** | 1 or 0x1; Words that are all uppercase are not checked |
| **swSpellingIgnoreWordsWithNumbers** | 4 or 0x4; Words containing both letters and numbers are not checked |
| **swSpellingLeaveEngineRunning** | 32 or 0x20; Do not stop Microsoft Word, which is the spell-check engine, after checking the first and any subsequent annotations if you have a significant number of annotations to spell check; however, on the last use of [IAnnotation::CheckSpelling](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~CheckSpelling.html), you must disable this flag so that Microsoft Word is shut down after that call |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCheckSpellingOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
