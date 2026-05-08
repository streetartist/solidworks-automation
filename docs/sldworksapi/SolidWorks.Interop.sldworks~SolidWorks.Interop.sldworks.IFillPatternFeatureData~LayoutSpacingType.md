# LayoutSpacingType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~LayoutSpacingType`

Gets or sets the type of spacing between the instances in the layout of this fill pattern feature.
Gets or sets the type of spacing between the instances in the layout of this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LayoutSpacingType As System.Integer
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Integer
 
instance.LayoutSpacingType = value
 
value = instance.LayoutSpacingType
```

```

System.int LayoutSpacingType {get; set;}
```

```

property System.int LayoutSpacingType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Pattern layout spacing type as defined in [swPatternLayoutSpacingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutSpacingType_e.html)

Remarks

| If this property is set to... | Then also set... |
| --- | --- |
| swPatternLayoutSpacingType\_e.swPatternLayoutInstances | [IFillPatternFeatureData::NoOfInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~NoOfInstances.md); [IFillPatternFeatureData::InstanceSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~InstanceSpacing.md) is not valid |
| swPatternLayoutSpacingType\_e.swPatternLayoutTargetSpacing | IFillPatternFeatureData::InstanceSpacing; IFillPatternFeatureData::NoOfInstances is not valid |

Example

See the [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)  
[IFillPatternFeatureData::PatternLayoutType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.md)
