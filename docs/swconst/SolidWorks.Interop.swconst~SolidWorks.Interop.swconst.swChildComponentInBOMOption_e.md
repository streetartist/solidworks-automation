# swChildComponentInBOMOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChildComponentInBOMOption_e`

Child component display options in Bills of Materials (BOM) for assemblies and for parts that have weldment/sheet metal cut lists.
Child component display options in Bills of Materials (BOM) for assemblies and for parts that have weldment/sheet metal cut lists.

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

<System.Runtime.InteropServices.GuidAttribute("DBEE519A-90B9-4599-8E76-BEAB609C2A1F")>
Public Enum swChildComponentInBOMOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swChildComponentInBOMOption_e
```

```

[System.Runtime.InteropServices.Guid("DBEE519A-90B9-4599-8E76-BEAB609C2A1F")]
public enum swChildComponentInBOMOption_e : System.Enum 
```

```

public enum swChildComponentInBOMOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("DBEE519A-90B9-4599-8E76-BEAB609C2A1F")
public enum swChildComponentInBOMOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("DBEE519A-90B9-4599-8E76-BEAB609C2A1F")]
__value public enum swChildComponentInBOMOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("DBEE519A-90B9-4599-8E76-BEAB609C2A1F")]
public enum class swChildComponentInBOMOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swChildComponent\_Hide** | 1 = Child components might be listed individually, depending on the properties that you selected when you created the BOM |
| **swChildComponent\_Promote** | 3 = The model's configuration dissolves when it appears in a BOM; all of its child components are promoted one level |
| **swChildComponent\_Show** | 2 = Child components appear as single items in the BOM |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swChildComponentInBOMOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
