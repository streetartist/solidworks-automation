# GetReferencePointType Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetReferencePointType`

Gets whether the table-driven pattern's reference point is a closed curve, a sketch point, or a vertex.
Gets whether the table-driven pattern's reference point is a closed curve, a sketch point, or a vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferencePointType() As System.Integer
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Integer
 
value = instance.GetReferencePointType()
```

```

System.int GetReferencePointType()
```

```

System.int GetReferencePointType(); 
```

#### Return Value

Type of reference point:

- 0 = closed curve
- 1 = sketch point
- 2 = vertex

Example

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::ReferencePoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint.md)
