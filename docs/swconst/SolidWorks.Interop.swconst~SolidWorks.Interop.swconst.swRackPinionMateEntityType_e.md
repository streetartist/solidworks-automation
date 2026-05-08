# swRackPinionMateEntityType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRackPinionMateEntityType_e`

Rack and pinion mate entity types.
Rack and pinion mate entity types.

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

<System.Runtime.InteropServices.GuidAttribute("9DF3A30E-9101-4CDC-854E-73F2AD6099EE")>
Public Enum swRackPinionMateEntityType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRackPinionMateEntityType_e
```

```

[System.Runtime.InteropServices.Guid("9DF3A30E-9101-4CDC-854E-73F2AD6099EE")]
public enum swRackPinionMateEntityType_e : System.Enum 
```

```

public enum swRackPinionMateEntityType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9DF3A30E-9101-4CDC-854E-73F2AD6099EE")
public enum swRackPinionMateEntityType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9DF3A30E-9101-4CDC-854E-73F2AD6099EE")]
__value public enum swRackPinionMateEntityType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9DF3A30E-9101-4CDC-854E-73F2AD6099EE")]
public enum class swRackPinionMateEntityType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRackPinionMateEntityType\_Pinion** | 1 = Select a cylindrical [face](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [arc](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html) or circular edge, sketch circle or arc, [axis](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), or revolved [surface](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html) |
| **swRackPinionMateEntityType\_Rack** | 0 = Select a linear [edge](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [sketch line](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), [centerline](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.html), axis, or cylindrical face |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRackPinionMateEntityType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
