# swAlignViewTypes_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAlignViewTypes_e`

View alignments.
View alignments.

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

<System.Runtime.InteropServices.GuidAttribute("F07EBD5F-52D3-4492-BBC3-52E03E50DD4D")>
Public Enum swAlignViewTypes_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAlignViewTypes_e
```

```

[System.Runtime.InteropServices.Guid("F07EBD5F-52D3-4492-BBC3-52E03E50DD4D")]
public enum swAlignViewTypes_e : System.Enum 
```

```

public enum swAlignViewTypes_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F07EBD5F-52D3-4492-BBC3-52E03E50DD4D")
public enum swAlignViewTypes_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F07EBD5F-52D3-4492-BBC3-52E03E50DD4D")]
__value public enum swAlignViewTypes_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F07EBD5F-52D3-4492-BBC3-52E03E50DD4D")]
public enum class swAlignViewTypes_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAlignViewHorizontalCenter** | 2 = Align this view horizontally with the center of BaseView |
| **swAlignViewHorizontalOrigin** | 4 = Align this view horizontally with the origin of BaseView |
| **swAlignViewVerticalCenter** | 3 = Align this view vertically with BaseView |
| **swAlignViewVerticalOrigin** | 5 = Align this view vertically with the origin of BaseView |
| **swDefaultViewAlignment** | 1 = Set the alignment of this view to its default |
| **swNoViewAlignment** | 0 = Remove the alignment restriction on this view |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAlignViewTypes\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
