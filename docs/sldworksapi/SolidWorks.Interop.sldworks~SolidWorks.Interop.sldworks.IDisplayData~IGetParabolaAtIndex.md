# IGetParabolaAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetParabolaAtIndex`

Gets the information for the specified parabola.
Gets the information for the specified parabola.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetParabolaAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetParabolaAtIndex(Index)
```

```

System.double IGetParabolaAtIndex( 
   System.int Index
)
```

```

System.double IGetParabolaAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   [GetPolygonCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonCount.md)Index of parabola

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return values are in an array of 16 doubles:

[ Color, LineType, LineStyleIndex, LineWeight, StartPt[3], EndPt[3], FocusPt[3], ApexPt[3] ]

where:

|  |  |
| --- | --- |
| Color | COLORREF returned as an integer; return value can be 0 or -1 for the default color |
| LineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |
| LineStyleIndex | Index location of this line style inside SOLIDWORKS Line Style Manager |
| LineWeight | Integer value defining the line weight |
| StartPt[3] | Array of 3 doubles (X,Y,Z) describing the parabola start point |
| EndPt[3] | Array of 3 doubles (X,Y,Z) describing the parabola end point |
| FocusPt[3] | Array of 3 doubles (X,Y,Z) describing the parabola focus point |
| ApexPt[3] | Array of 3 doubles (X,Y,Z) describing the parabola apex point |

This set of data repeats for each parabola in the view. The size of the array is (NumParabolas \* 16). Use [IDisplayData::GetParabolaCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetParabolaCount.md) to determine the number of parabolas.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetParabolaAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetParabolaAtIndex.md)  
[IDisplayData::GetParabolaCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetParabolaCount.md)
