# IGetLineAtIndex2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetLineAtIndex2`

Obsolete. Superseded by IDisplayData::IGetLineAtIndex3.
Obsolete. Superseded by [IDisplayData::IGetLineAtIndex3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetLineAtIndex3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLineAtIndex2( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetLineAtIndex2(Index)
```

```

System.double IGetLineAtIndex2( 
   System.int Index
)
```

```

System.double IGetLineAtIndex2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired line where the index begins at zero

#### Return Value

Pointer to an array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

[ color, lineType, Unused, Unused, startPt[3], endPt[3] ]

where:

|  |  |
| --- | --- |
| color | COLORREF returned as an integer; return value can be 0 or -1 for default color |
| lineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |
| startPt[3] | x, y, z  line start point |
| endPt[3] | x, y, z line end point |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineCount.md)  
[IDisplayData::GetLineAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineAtIndex2.md)
