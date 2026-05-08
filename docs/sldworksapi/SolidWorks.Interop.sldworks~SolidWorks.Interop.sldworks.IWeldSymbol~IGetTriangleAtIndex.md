# IGetTriangleAtIndex Method (IWeldSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetTriangleAtIndex`

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

Dim instance As IWeldSymbol
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
:   Index of the triangle where the index begins at 0

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see Remarks)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles :

[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]

where:

|  |  |
| --- | --- |
| vertexPt1[3] | = first XYZ vertex point |
| vertexPt2[3] | = second XYZ vertex point |
| vertexPt3[3] | = third XYZ vertex point |
| isFilled | = Boolean returned as a double; 1.0 if the triangle is filled, 0.0 if not |
| lineType | = line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)  
[IWeldSymbol::GetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTriangleAtIndex.md)  
[IWeldSymbol::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTriangleCount.md)
