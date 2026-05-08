# swPMContainer_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMContainer_e`

Docking states of PropertyManager page.
Docking states of PropertyManager page.

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

<System.Runtime.InteropServices.GuidAttribute("36CB73BE-F184-4D8B-B823-3CCE9A8DE141")>
Public Enum swPMContainer_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPMContainer_e
```

```

[System.Runtime.InteropServices.Guid("36CB73BE-F184-4D8B-B823-3CCE9A8DE141")]
public enum swPMContainer_e : System.Enum 
```

```

public enum swPMContainer_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("36CB73BE-F184-4D8B-B823-3CCE9A8DE141")
public enum swPMContainer_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("36CB73BE-F184-4D8B-B823-3CCE9A8DE141")]
__value public enum swPMContainer_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("36CB73BE-F184-4D8B-B823-3CCE9A8DE141")]
public enum class swPMContainer_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPMFloating** | 3 = True floating state where PropertyManager page lives inside new docking pane; a single floating window owns all PropertyManager pages of all open documents |
| **swPMInTabsWithFM** | 0 = Old-style PropertyManager page embedded in tabs at top |
| **swPMPinnedAboveFM** | 1 = Quasi floating state where PropertyManager page automatically displays, resizes itself in the lower-left corner of model frame window, and covers the FeatureManager design tree; one window for each open document |
| **swPMPinnedLowerRight** | 4 = Quasi floating state where PropertyManager page automatically displays, resizes itself in the lower-right corner of the model frame window, covers the graphic area, and has full height;  one window for each open document |
| **swPMPinnedNextToFM** | 2 = Quasi floating state where PropertyManager page automatically displays, resizes itself to the right of the FeatureManager design tree, covers the graphics area, and has full height.; one window for each open document |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPMContainer\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
