# swRebuildOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRebuildOptions_e`

Rebuild options. Bitmask.
Rebuild options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("39021C27-A128-467E-BB84-71A0C3C5A8D6")>
Public Enum swRebuildOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRebuildOptions_e
```

```

[System.Runtime.InteropServices.Guid("39021C27-A128-467E-BB84-71A0C3C5A8D6")]
public enum swRebuildOptions_e : System.Enum 
```

```

public enum swRebuildOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("39021C27-A128-467E-BB84-71A0C3C5A8D6")
public enum swRebuildOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("39021C27-A128-467E-BB84-71A0C3C5A8D6")]
__value public enum swRebuildOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("39021C27-A128-467E-BB84-71A0C3C5A8D6")]
public enum class swRebuildOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCurrentSheetDisp** | 8 or 0x8; Drawing only; only rebuilds the display of the views on the current drawing sheet |
| **swForceRebuildAll** | 2 or 0x2; Assembly or drawing; Forces a rebuild of all geometry |
| **swRebuildAll** | 1 or 0x1; Assembly or drawing; rebuilds geometry that has not been regenerated |
| **swUpdateDirtyOnly** | 16 or 0x10; Drawing only; only rebuilds drawing views that are dirty when OR'd with swCurrentSheetDisp option |
| **swUpdateMates** | 4 or 0x4; Assembly only; only rebuilds mates, which is much faster than rebuilding the geometry. Especially useful for [IComponent2::Transform2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRebuildOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
