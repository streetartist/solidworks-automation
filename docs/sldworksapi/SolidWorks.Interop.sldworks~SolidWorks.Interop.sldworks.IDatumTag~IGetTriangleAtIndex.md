# IGetTriangleAtIndex Method (IDatumTag)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTriangleAtIndex`

Gets the triangle at the specified index of this datum tag.
Gets the triangle at the specified index of this datum tag.

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

Dim instance As IDatumTag
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
:   Index of triangle; index begins at 0

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]

where:

|  |  |
| --- | --- |
| vertexPt1[3] | First XYZ vertex point |
| vertexPt2[3] | Second XYZ vertex point |
| vertexPt3[3] | Third XYZ vertex point |
| isFilled | Boolean returned as a double that is True if the triangle is filled, false if it is not |
| lineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::GetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTriangleAtIndex.md)  
[IDatumTag::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTriangleCount.md)  
[IDatumTag::FilledTriangle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~FilledTriangle.md)
