# InnerCornerFilletRadius Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~InnerCornerFilletRadius`

Gets or sets the fillet radius for the inner corners of this gusset.
Gets or sets the fillet radius for the inner corners of this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InnerCornerFilletRadius As System.Double
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Double
 
instance.InnerCornerFilletRadius = value
 
value = instance.InnerCornerFilletRadius
```

```

System.double InnerCornerFilletRadius {get; set;}
```

```

property System.double InnerCornerFilletRadius {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Inner corner fillet radius

Remarks

This property is valid only if [ISMGussetFeatureData::FilletInnerCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletInnerCorners.md) is true.

Example

See the examples for [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[ISMGussetFeatureData::OuterCornerFilletRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OuterCornerFilletRadius.md)
