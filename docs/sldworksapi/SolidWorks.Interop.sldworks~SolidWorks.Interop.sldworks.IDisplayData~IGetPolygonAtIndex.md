# IGetPolygonAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolygonAtIndex`

Gets information for the specified polygon.
Gets information for the specified polygon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPolygonAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetPolygonAtIndex(Index)
```

```

System.double IGetPolygonAtIndex( 
   System.int Index
)
```

```

System.double IGetPolygonAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired polygon where the index begins at zero

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Format of return values is an array of doubles with the format:

> **[** Color, LineType, Unused, Unused, NumPolyPoints, [x,y,z] **]**

where:

|  |  |
| --- | --- |
| Color | Polygon color |
| LineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). You can use this index value with [IDrawingDoc::GetLineFontInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.md) and [IDrawingDoc::GetLineFontName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.md) |
| NumPolyPoints | Number of XYZ points found in the [x,y,z] return value |
| [x,y,z] | Array of NumPolyPoints points used to describe the polygon |

Use [IDisplayData::GetPolygonSizeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.md) to determine the number of elements in this array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetPolygonAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonAtIndex.md)  
[IDisplayData::GetPolygonCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonCount.md)  
[IDisplayData::GetPolygonSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.md)
