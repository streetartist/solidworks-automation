# swAddToRecentDocumentList_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddToRecentDocumentList_e`

Recent Documents list actions for a document opened using ISldWorks::OpenDoc7 and IDocumentSpecification::AddToRecentDocumentList.
Recent Documents list actions for a document opened using [ISldWorks::OpenDoc7](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html) and [IDocumentSpecification::AddToRecentDocumentList](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AddToRecentDocumentList.html).

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

<System.Runtime.InteropServices.GuidAttribute("6402D6EB-C4DA-4DB4-9662-A1039149984D")>
Public Enum swAddToRecentDocumentList_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAddToRecentDocumentList_e
```

```

[System.Runtime.InteropServices.Guid("6402D6EB-C4DA-4DB4-9662-A1039149984D")]
public enum swAddToRecentDocumentList_e : System.Enum 
```

```

public enum swAddToRecentDocumentList_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6402D6EB-C4DA-4DB4-9662-A1039149984D")
public enum swAddToRecentDocumentList_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6402D6EB-C4DA-4DB4-9662-A1039149984D")]
__value public enum swAddToRecentDocumentList_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6402D6EB-C4DA-4DB4-9662-A1039149984D")]
public enum class swAddToRecentDocumentList_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAddToRecentDocumentList\_Add** | 1 |
| **swAddToRecentDocumentList\_Default** | 0 = Default OpenDoc7 action: if a configuration is specified, the document is not added to the Recent Documents list; if a configuration is not specified, the document is added |
| **swAddToRecentDocumentList\_DontAdd** | 2 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAddToRecentDocumentList\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
