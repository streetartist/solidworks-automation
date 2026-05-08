# GetPolygonAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonAtIndex`

Gets information for the specified polygon.
Gets information for the specified polygon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPolygonAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetPolygonAtIndex(Index)
```

```

System.object GetPolygonAtIndex( 
   System.int Index
)
```

```

System.Object^ GetPolygonAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired polygon where the index begins at zero

#### Return Value

Array of doubles (see **Remarks**)

Remarks

Format of return values is an array of doubles with the format:

**[** Color, LineType, Unused, Unused, NumPolyPoints, [x,y,z] **]**

where:

|  |  |
| --- | --- |
| Color | Polygon color |
| LineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). You can use this index value with [IDrawingDoc::GetLineFontInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.md) and [IDrawingDoc::GetLineFontName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.md) |
| NumPolyPoints | Number of XYZ points found in the [x,y,z] return value |
| [x,y,z] | Array of NumPolyPoints points used to describe the polygon |

Use [IDisplayData::GetPolygonSizeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.md) to determine the number of elements returned in this array.

Example

[Get Weld Bead Symbol Data (VBA)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VB.htm)  
[Get Weld Bead Symbol Data (VB.NET)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VBNET.htm)  
[Get Weld Bead Symbol Data (C#)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetPolygonCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonCount.md)  
[IDisplayData::IGetPolygonAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolygonAtIndex.md)  
[IDisplayData::GetPolygonSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.md)
