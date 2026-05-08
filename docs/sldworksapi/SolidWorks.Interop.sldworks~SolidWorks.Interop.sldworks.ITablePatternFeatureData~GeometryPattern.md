# GeometryPattern Property (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GeometryPattern`

Gets or sets whether to create the pattern using only the geometry (faces and edges) of the features for the table-driven pattern feature.
Gets or sets whether to create the pattern using only the geometry (faces and edges) of the features for the table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GeometryPattern As System.Boolean
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Boolean
 
instance.GeometryPattern = value
 
value = instance.GeometryPattern
```

```

System.bool GeometryPattern {get; set;}
```

```

property System.bool GeometryPattern {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to pattern using only geometry of the features; false to pattern and solve entire features

Remarks

This property is valid with [ITablePatternFeatureData::PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFaceArray.md) or [ITablePatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFeatureArray.md) and is invalid with [ITablePatternFeatureData::PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternBodyArray.md).

Example

See the [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)
