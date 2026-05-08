# GetTriangleAtIndex Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTriangleAtIndex`

Gets the triangle at the specified index.
Gets the triangle at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTriangleAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As INote
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetTriangleAtIndex(Index)
```

```

System.object GetTriangleAtIndex( 
   System.int Index
)
```

```

System.Object^ GetTriangleAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the triangle where the index begins at 0

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles :

[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]

  where:

|  |  |
| --- | --- |
| vertexPt1[3] | = first XYZ vertex point |
| vertexPt2[3] | = second XYZ vertex point |
| vertexPt3[3] | = third XYZ vertex point |
| isFilled | = BOOLEAN returned as a double and is True if the triangle is filled, false otherwise |
| lineType | = line type; see [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTriangleCount.md)  
[INote::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTriangleAtIndex.md)
