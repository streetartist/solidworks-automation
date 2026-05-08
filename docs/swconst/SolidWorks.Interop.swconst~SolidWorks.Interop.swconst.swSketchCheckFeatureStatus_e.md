# swSketchCheckFeatureStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSketchCheckFeatureStatus_e`

Statuses after checking to see if this sketch is valid for use in creating the specified feature
Statuses after checking to see if this sketch is valid for use in creating the specified feature

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

<System.Runtime.InteropServices.GuidAttribute("4D8E745A-BA95-4C65-B342-97F4E6768E3E")>
Public Enum swSketchCheckFeatureStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSketchCheckFeatureStatus_e
```

```

[System.Runtime.InteropServices.Guid("4D8E745A-BA95-4C65-B342-97F4E6768E3E")]
public enum swSketchCheckFeatureStatus_e : System.Enum 
```

```

public enum swSketchCheckFeatureStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("4D8E745A-BA95-4C65-B342-97F4E6768E3E")
public enum swSketchCheckFeatureStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("4D8E745A-BA95-4C65-B342-97F4E6768E3E")]
__value public enum swSketchCheckFeatureStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("4D8E745A-BA95-4C65-B342-97F4E6768E3E")]
public enum class swSketchCheckFeatureStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSketchCheckFeatureStatus\_ClosedWantOpen** | 15 = The contour is closed |
| **swSketchCheckFeatureStatus\_ContourIntersectsCenterLine** | 23 = The revolution contour cannot cross the centerline or touch it in an isolated point |
| **swSketchCheckFeatureStatus\_CturXCtur** | 12 = The sketch has intersecting contours |
| **swSketchCheckFeatureStatus\_DisjCturs** | 13 = The sketch contains disjoint contours |
| **swSketchCheckFeatureStatus\_DoubleContainment** | 16 = The sketch contains a doubly nested contour |
| **swSketchCheckFeatureStatus\_EmptySketch** | 5 |
| **swSketchCheckFeatureStatus\_EntUnspecBad** | 3 = The sketch contains a self-intersecting entity |
| **swSketchCheckFeatureStatus\_EntXEnt** | 1 = The sketch contains a self-intersecting contour |
| **swSketchCheckFeatureStatus\_EntXSelf** | 2 = The sketch contains a self-intersecting entity |
| **swSketchCheckFeatureStatus\_ManyOpen** | 9 = The sketch has more than one open contour |
| **swSketchCheckFeatureStatus\_MixedContours** | 11 = The sketch has both open and closed contours |
| **swSketchCheckFeatureStatus\_MoreThanOneContour** | 17 = The sketch contains more than one contour |
| **swSketchCheckFeatureStatus\_NeedsAxis** | 21 = The sketch should contain a centerline |
| **swSketchCheckFeatureStatus\_NoOpen** | 10 = The sketch has no more open contours |
| **swSketchCheckFeatureStatus\_OK** | 0 = No problems found, the sketch can be used to create the specified feature. |
| **swSketchCheckFeatureStatus\_OneClosedContourExpected** | 19 = The sketch should contain a single closed contour |
| **swSketchCheckFeatureStatus\_OneOpenContourExpected** | 18 = The sketch should contain a single open contour |
| **swSketchCheckFeatureStatus\_OpenOrUnclear** | 22 = Selected contours are open or ambiguous |
| **swSketchCheckFeatureStatus\_OpenWantClosed** | 14 = The contour is open |
| **swSketchCheckFeatureStatus\_ThreeEnts** | 4 = The sketch cannot be used for a feature because an endpoint is wrongly shared by multiple entities |
| **swSketchCheckFeatureStatus\_UnknownError** | -1 = Unknown error |
| **swSketchCheckFeatureStatus\_WantSingleOpenOrMultiClosedDisjoint** | 20 = The sketch should contain either one open contour or multiple closed disjoint contours |
| **swSketchCheckFeatureStatus\_WrongManyContours** | 7 = The sketch has more than one contour |
| **swSketchCheckFeatureStatus\_WrongOpen** | 6 = The sketch contains an open contour |
| **swSketchCheckFeatureStatus\_ZeroLengthEnt** | 8 = The sketch contains a zero-length entity |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSketchCheckFeatureStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
