# IGetEllipseAtIndex2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetEllipseAtIndex2`

Gets information for the specified ellipse.
Gets information for the specified ellipse.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEllipseAtIndex2( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetEllipseAtIndex2(Index)
```

```

System.double IGetEllipseAtIndex2( 
   System.int Index
)
```

```

System.double IGetEllipseAtIndex2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired ellipse where the index begins at zero

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles:

**[** color, lineType, Unused, Unused, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3], **]**

where:

|  |  |
| --- | --- |
| color | COLORREF returned as an integer. Return value could be 0 or -1 for default color. |
| LineType | Line type as defined in[swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). |
| StartPt[3] | Array of 3 doubles (X,Y,Z) describing the ellipse start point. |
| EndPt[3] | Array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, then this will be the same point as the StartPt. |
| CenterPt[3] | Array of 3 doubles (X,Y,Z) describing the ellipse center point. |
| MajorPt[3] | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and the major axis. |
| MinorPt[3] | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and the minor axis. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetEllipseAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetEllipseAtIndex2.md)  
[IDisplayData::GetEllipseCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetEllipseCount.md)
