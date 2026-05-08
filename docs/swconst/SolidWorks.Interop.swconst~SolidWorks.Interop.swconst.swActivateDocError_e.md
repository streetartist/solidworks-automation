# swActivateDocError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swActivateDocError_e`

Document activation errors. Bitmask.
Document activation errors. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("EE87D60C-0BC8-4AF6-8DE6-A25F9CDC45FE")>
Public Enum swActivateDocError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swActivateDocError_e
```

```

[System.Runtime.InteropServices.Guid("EE87D60C-0BC8-4AF6-8DE6-A25F9CDC45FE")]
public enum swActivateDocError_e : System.Enum 
```

```

public enum swActivateDocError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("EE87D60C-0BC8-4AF6-8DE6-A25F9CDC45FE")
public enum swActivateDocError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("EE87D60C-0BC8-4AF6-8DE6-A25F9CDC45FE")]
__value public enum swActivateDocError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("EE87D60C-0BC8-4AF6-8DE6-A25F9CDC45FE")]
public enum class swActivateDocError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDocNeedsRebuildWarning** | 2 or 0x2; The document that was activated needs to be rebuilt (your application can use EditRebuild on the PartDoc, AssemblyDoc, or DrawingDoc to perform the rebuild). |
| **swGenericActivateError** | 1 or 0x1; An unspecified error was encountered, and the document was not activated. |

Remarks

Bitmask

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swActivateDocError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
