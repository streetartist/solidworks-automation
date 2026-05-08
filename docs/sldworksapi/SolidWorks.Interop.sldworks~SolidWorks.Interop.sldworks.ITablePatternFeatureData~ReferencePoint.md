# ReferencePoint Property (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint`

Gets or sets the reference point for pattern instances of this table-driven pattern feature.
Gets or sets the reference point for pattern instances of this table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencePoint As System.Object
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Object
 
instance.ReferencePoint = value
 
value = instance.ReferencePoint
```

```

System.object ReferencePoint {get; set;}
```

```

property System.Object^ ReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Reference point of this table-driven pattern feature

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::GetReferencePointType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetReferencePointType.md)  
[ITablePatternFeatureData::UseCentroid Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~UseCentroid.md)
