# UseDefaultBendRadius Property (ISketchedBendFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseDefaultBendRadius`

Gets or sets whether to use the default bend radius of this sketched bend.
Gets or sets whether to use the default bend radius of this sketched bend.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDefaultBendRadius As System.Boolean
```

```

Dim instance As ISketchedBendFeatureData
Dim value As System.Boolean
 
instance.UseDefaultBendRadius = value
 
value = instance.UseDefaultBendRadius
```

```

System.bool UseDefaultBendRadius {get; set;}
```

```

property System.bool UseDefaultBendRadius {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the default bend radius, false to specify another bend radius

Remarks

This property takes precedence over [ISketchedBendFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseGaugeTable.md). If this property is set to true, then ISketchedBendFeatureData::UseGaugeTable is set to false and cannot be changed.

Example

See [ISketchedBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md) examples.

Example

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md)  
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.md)  
[ISketchedBendFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~BendRadius.md)
