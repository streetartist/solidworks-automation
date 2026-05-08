# swAutodimScheme_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimScheme_e`

Dimensioning schemes for ISketch::AutoDimension2 and IDrawingDoc::AutoDimension.
Dimensioning schemes for [ISketch::AutoDimension2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html) and [IDrawingDoc::AutoDimension](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IDrawingDoc~AutoDimension.html).

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

<System.Runtime.InteropServices.GuidAttribute("FD74DF59-8C51-4A95-8CC5-11BCA4543006")>
Public Enum swAutodimScheme_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAutodimScheme_e
```

```

[System.Runtime.InteropServices.Guid("FD74DF59-8C51-4A95-8CC5-11BCA4543006")]
public enum swAutodimScheme_e : System.Enum 
```

```

public enum swAutodimScheme_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("FD74DF59-8C51-4A95-8CC5-11BCA4543006")
public enum swAutodimScheme_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("FD74DF59-8C51-4A95-8CC5-11BCA4543006")]
__value public enum swAutodimScheme_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("FD74DF59-8C51-4A95-8CC5-11BCA4543006")]
public enum class swAutodimScheme_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAutodimSchemeBaseline** | 1 = Use a baseline dimensioning scheme |
| **swAutodimSchemeCenterline** | 4 = Not supported in sketches or drawings; do not use |
| **swAutodimSchemeChain** | 3 = Use a chain dimensioning scheme |
| **swAutodimSchemeOrdinate** | 2 = Use an ordinate dimensioning scheme |

Remarks

The horizontal and vertical dimension placements are specified independently using the HorizontalPlacement and VerticalPlacement parameters in the methods.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAutodimScheme\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
