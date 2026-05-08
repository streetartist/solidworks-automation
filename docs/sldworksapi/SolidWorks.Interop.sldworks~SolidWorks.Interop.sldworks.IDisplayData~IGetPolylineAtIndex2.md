# IGetPolylineAtIndex2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolylineAtIndex2`

Gets information for the specified polyline.
Gets information for the specified polyline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPolylineAtIndex2( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetPolylineAtIndex2(Index)
```

```

System.double IGetPolylineAtIndex2( 
   System.int Index
)
```

```

System.double IGetPolylineAtIndex2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired polyline where the index begins at zero

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Format of return values is an array of doubles with the format:

> [ polyLineType, DataSize, Color, LineFont, Unused, Unused, NumPolyPoints, [x,y,z] ]

where:

|  |  |
| --- | --- |
| polyLineType | Underlying geometry type:     - 0 - Polyline type - 1 - Arc or Circle type |
| DataSize | Number of elements in the GeomData array. For Type = 0, this argument is 0. |
| Color | Polyline color. |
| LineFont | Polyline font information. You can use his value with [IDrawingDoc::GetLineFontInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.md) and [IDrawingDoc::GetLineFontName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.md). This value is valid only if LineStyle is -1. |
| NumPolyPoints | Number of XYZ points found in the [x,y,z] return value. |
| [x,y,z] | Array of points used to describe the polyline. This array has NumPolyPoints points. This method returns an array for every polyline regardless of its type. |

Use [IDisplayData::GetPolyLineSizeAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolylineSizeAtIndex2.md) to determine the number of elements returned in this array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetPolylineAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolylineAtIndex2.md)  
[IDisplayData::GetPolyLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolyLineCount.md)  
[IDisplayData::GetPolygonSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.md)
