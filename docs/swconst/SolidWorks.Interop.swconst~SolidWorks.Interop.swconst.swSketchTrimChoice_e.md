# swSketchTrimChoice_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSketchTrimChoice_e`

Sketch trim options.
Sketch trim options.

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

<System.Runtime.InteropServices.GuidAttribute("58ADBA30-B4A9-405B-8712-D0738042BFA2")>
Public Enum swSketchTrimChoice_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSketchTrimChoice_e
```

```

[System.Runtime.InteropServices.Guid("58ADBA30-B4A9-405B-8712-D0738042BFA2")]
public enum swSketchTrimChoice_e : System.Enum 
```

```

public enum swSketchTrimChoice_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("58ADBA30-B4A9-405B-8712-D0738042BFA2")
public enum swSketchTrimChoice_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("58ADBA30-B4A9-405B-8712-D0738042BFA2")]
__value public enum swSketchTrimChoice_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("58ADBA30-B4A9-405B-8712-D0738042BFA2")]
public enum class swSketchTrimChoice_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSketchTrimClosest** | 0 = Trim to closest. One and only one sketch segment must be selected before calling [ISketchManager::SketchTrim](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchTrim.html) using this option. |
| **swSketchTrimCorner** | 1 = Corner. Two and only two sketch segments must be selected before calling ISketchManager::SketchTrim using this option. |
| **swSketchTrimEntities** | 4 = Power trim. Before calling ISketchManager::SketchTrim using this option, use [IModelDocExtension::SelectByID2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Mark = 2 to select 1 or more sketch segments (up to total number of sketch segments in the model), specifying their pick points. The sketch segments are trimmed to the sketch segments nearest their pick points.  When you trim sketch segments using Power trim in the user interface, you drag your cursor across sketch segments, and the point at which the cursor crosses a sketch segment is where that sketch segment is trimmed. The API simulates this functionality by requiring you to select sketch segments by pick points, which are used as references when trimming the selected sketch segments. |
| **swSketchTrimEntityPoint** | 3 = Power trim. One and only one sketch segment must be selected before calling ISketchManager::SketchTrim using this option. Trims to a specific point on the sketch segment. Call this method, specifying non-zero X, Y, and Z, the point at which to trim the selected sketch segment. The specified point must lie on the sketch segment. |
| **swSketchTrimInside** | 6 = Trim away inside. Before calling ISketchManager::SketchTrim using this option, select at least three sketch segments: two to create the boundary, and one or more that intersect both sketch segments in the boundary. All selected sketch segments that intersect the boundary are trimmed inside the boundary segments. |
| **swSketchTrimOutside** | 5 = Trim away outside. Before calling ISketchManager::SketchTrim using this option, select at least three sketch segments: two to create the trim boundary, and one or more that intersect both sketch segments in the boundary. All selected sketch segments that intersect the boundary are trimmed outside the boundary segments. |
| **swSketchTrimTwoEntities** | 2 = Power trim. Before calling ISketchManager::SketchTrim using this option, use IModelDocExtension::SelectByID2 with Mark = 0 to select two intersecting sketch segments, specifying their pick points. Trims the first selected sketch segment to the second intersecting sketch segment. The order in which the sketch segments are selected determines which one is trimmed. The first selected sketch segment will be trimmed on its pick point side to the second selected sketch segment. |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSketchTrimChoice\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
