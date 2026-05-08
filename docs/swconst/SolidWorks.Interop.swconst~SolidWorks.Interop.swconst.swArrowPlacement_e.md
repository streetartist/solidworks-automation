# swArrowPlacement_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swArrowPlacement_e`

Smart arrow placement.
Smart arrow placement.

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

<System.Runtime.InteropServices.GuidAttribute("695DFC34-E252-4E30-960E-F311959E0719")>
Public Enum swArrowPlacement_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swArrowPlacement_e
```

```

[System.Runtime.InteropServices.Guid("695DFC34-E252-4E30-960E-F311959E0719")]
public enum swArrowPlacement_e : System.Enum 
```

```

public enum swArrowPlacement_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("695DFC34-E252-4E30-960E-F311959E0719")
public enum swArrowPlacement_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("695DFC34-E252-4E30-960E-F311959E0719")]
__value public enum swArrowPlacement_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("695DFC34-E252-4E30-960E-F311959E0719")]
public enum class swArrowPlacement_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swArrowPlacementLegacy** | 0 = Vary Smart arrow placement as in SOLIDWORKS 2012 and earlier (see **Remarks**) |
| **swArrowPlacementSmartArrowFollowText** | 1 |
| **swArrowPlacementSmartArrowRemainAttachedToArc** | 2 |

Remarks

In SOLIDWORKS 2012 and earlier, Smart arrows sometimes:

- Remained on the far side of an arc when moved to its other side.
- Were attached to an extension line.
- Pointed out to space.
- Were placed on the part.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swArrowPlacement\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
