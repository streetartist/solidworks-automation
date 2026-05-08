# GetPointAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPointAtIndex`

Gets information about the specified point.
Gets information about the specified point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPointAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetPointAtIndex(Index)
```

```

System.object GetPointAtIndex( 
   System.int Index
)
```

```

System.Object^ GetPointAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the point

#### Return Value

Array (see **Remarks**)

Remarks

The return values are in an array of 7 doubles:

[ Color, LineType, LineStyleIndex, PointStyle, CircleFilled, X, Y, Z ]

where:

|  |  |
| --- | --- |
| Color | COLORREF returned as an integer; return value can be 0 or -1 for the default color |
| LineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |
| PointStyle | Point style as defined in [swPointStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPointStyle_e.html) |
| *CircleFilled* | 0 if the circle is filled, 1 if not |
| *X* | X coordinate of the specified point |
| *Y* | Y coordinate of the specified point |
| *Z* | Z coordiante of the specified point |

Use [IDisplayData::GetPointCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPointCount.md) to determine the number of points.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::IGetPointAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPointAtIndex.md)
