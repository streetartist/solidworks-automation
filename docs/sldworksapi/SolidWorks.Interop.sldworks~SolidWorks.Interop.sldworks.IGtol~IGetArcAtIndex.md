# IGetArcAtIndex Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArcAtIndex`

Gets information for the specified arc.
Gets information for the specified arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetArcAtIndex(Index)
```

```

System.double IGetArcAtIndex( 
   System.int Index
)
```

```

System.double IGetArcAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based index of the arc

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles:

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

where:

|  |  |
| --- | --- |
| lineType | [Line type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |
| startPt[3] | XYZ arc start point |
| endPt[3] | XYZ arc end point |
| centerPt[3] | XYZ arc center point |
| rotationDir | Boolean returned as a double and represents the rotation direction, where CCW returns True and CW returns false |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArcAtIndex.md)  
[IGtol::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArcCount.md)
