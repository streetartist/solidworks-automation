# GetArcAtIndex2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArcAtIndex2`

Gets information for the specified arc.
Gets information for the specified arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcAtIndex2( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetArcAtIndex2(Index)
```

```

System.object GetArcAtIndex2( 
   System.int Index
)
```

```

System.Object^ GetArcAtIndex2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired arc where the index begins at zero

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles :

[ color, lineType, Unused, Unused, startPt[3], endPt[3], centerPt[3], arcNormal[3], rotationDir ]

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
[IDisplayData::IGetLineAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetLineAtIndex2.md)  
[IDisplayData::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArcCount.md)
