# GetTriangleAtIndex Method (IDisplayData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTriangleAtIndex`

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

Dim instance As IDisplayData
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
:   Zero-based index of the desired triangle

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

**[** vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType **]**

where:

|  |  |
| --- | --- |
| vertexPt1[3] | First XYZ vertex point |
| vertexPt2[3] | Second XYZ vertex point |
| vertexPt3[3] | Third XYZ vertex point |
| isFilled | Boolean returned as a double that is True if the triangle is filled, false otherwise |
| lineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetTriangleAtIndex.md)  
[IDisplayData::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTriangleCount.md)
