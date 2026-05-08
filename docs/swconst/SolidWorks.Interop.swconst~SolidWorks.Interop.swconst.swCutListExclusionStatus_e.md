# swCutListExclusionStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCutListExclusionStatus_e`

Status of excluding the selected faces and features in the cut list sort exclusion list.
Status of excluding the selected faces and features in the cut list sort exclusion list.

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

<System.Runtime.InteropServices.GuidAttribute("9AC05BB7-117D-4D59-82F9-8EA1E80E11B3")>
Public Enum swCutListExclusionStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCutListExclusionStatus_e
```

```

[System.Runtime.InteropServices.Guid("9AC05BB7-117D-4D59-82F9-8EA1E80E11B3")]
public enum swCutListExclusionStatus_e : System.Enum 
```

```

public enum swCutListExclusionStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9AC05BB7-117D-4D59-82F9-8EA1E80E11B3")
public enum swCutListExclusionStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9AC05BB7-117D-4D59-82F9-8EA1E80E11B3")]
__value public enum swCutListExclusionStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9AC05BB7-117D-4D59-82F9-8EA1E80E11B3")]
public enum class swCutListExclusionStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCutListExclusionStatus\_InvalidEntities** | 1 = Selected faces and features are invalid because they are not of selection type BODYFEATURE or FACE. Other examples of face and features that are invalid for exclusion:   - Chamfers that remove an entire face. - Suppressed features. - Features that create new bodies from sketches, such as boss-extrude, revolve, and sweep. - Certain sheet metal features. |
| **swCutListExclusionStatus\_Success** | 0 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCutListExclusionStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
