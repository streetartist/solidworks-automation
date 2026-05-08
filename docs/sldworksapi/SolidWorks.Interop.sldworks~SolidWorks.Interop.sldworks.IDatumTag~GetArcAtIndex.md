# GetArcAtIndex Method (IDatumTag)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArcAtIndex`

Gets information for the specified arc for this datum tag.
Gets information for the specified arc for this datum tag.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IDatumTag
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetArcAtIndex(Index)
```

```

System.object GetArcAtIndex( 
   System.int Index
)
```

```

System.Object^ GetArcAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the arc; index begins at 0

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

where:

|  |  |
| --- | --- |
| lineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |
| startPt[3] | XYZ arc start point |
| endPt[3] | XYZ arc end point |
| centerPt[3] | XYZ arc center point |
| rotationDir | Boolean returned as a double that represents the rotation direction, where CCW = True and CW = false |

Before calling this method, call [IDatumTag::GetArcCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArcCount.md) to find out the number of arcs in this datum tag.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::IGetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetArcAtIndex.md)  
[IDatumTag::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArcCount.md)
