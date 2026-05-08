# OuterCornerFilletRadius Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OuterCornerFilletRadius`

Gets or sets the fillet radius for the outer corners of this gusset.
Gets or sets the fillet radius for the outer corners of this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OuterCornerFilletRadius As System.Double
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Double
 
instance.OuterCornerFilletRadius = value
 
value = instance.OuterCornerFilletRadius
```

```

System.double OuterCornerFilletRadius {get; set;}
```

```

property System.double OuterCornerFilletRadius {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Outer corner fillet radius

Remarks

This property is valid only if [ISMGussetFeatureData::FilletOuterCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletOuterCorners.md) is true.

Example

See the examples for [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[ISMGussetFeatureData::InnerCornerFilletRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~InnerCornerFilletRadius.md)
