# IGetTriangleAtIndex Method (IDisplayData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetTriangleAtIndex`

Gets the triangle at the specified index.
Gets the triangle at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTriangleAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetTriangleAtIndex(Index)
```

```

System.double IGetTriangleAtIndex( 
   System.int Index
)
```

```

System.double IGetTriangleAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired triangle where the index begins at zero

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks)**

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles :

**[** color, lineType, Unused, Unused, startPt[3], endPt[3], centerPt[3], arcNormal[3], rotationDir **]**

where:

|  |  |
| --- | --- |
| color | COLORREF returned as an integer; return value can be 0 or -1 for default color |
| LineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |
| startPt[3] | XYZ arc start point |
| endPt[3] | XYZ arc end point |
| centerPt[3] | XYZ arc center point |
| arcNormal[3] | XYZ arc normal vector |
| rotationDir | Boolean returned as a double that represents the rotation direction, where CCW = True and CW = false |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTriangleAtIndex.md)  
[IDisplayData::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTriangleCount.md)
