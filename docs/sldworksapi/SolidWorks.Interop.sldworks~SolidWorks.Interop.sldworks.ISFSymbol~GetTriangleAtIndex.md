# GetTriangleAtIndex Method (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTriangleAtIndex`

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

Dim instance As ISFSymbol
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

Call [ISFSymbol::GetTriangleCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTriangleCount.md) before calling this method to get the number of triangles in this surface finish symbol.

The return value is the following array of doubles :

[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]

where:

|  |  |
| --- | --- |
| vertexPt1[3] | = First XYZ vertex point |
| vertexPt2[3] | = Second XYZ vertex point |
| vertexPt3[3] | = Third XYZ vertex point |
| isFilled | = BOOLEAN returned as a double; True if triangle is filled, false if not |
| lineType | = Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)  
[ISFSymbol::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetTriangleAtIndex.md)
