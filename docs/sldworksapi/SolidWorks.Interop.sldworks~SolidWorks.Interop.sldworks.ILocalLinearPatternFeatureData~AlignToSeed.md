# AlignToSeed Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~AlignToSeed`

Gets or sets whether to align each instance to match the original alignment of the seed component in this linear component pattern feature.
Gets or sets whether to align each instance to match the original alignment of the seed component in this linear component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AlignToSeed As System.Boolean
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean
 
instance.AlignToSeed = value
 
value = instance.AlignToSeed
```

```

System.bool AlignToSeed {get; set;}
```

```

property System.bool AlignToSeed {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to align each instance to the seed component, false to not

Remarks

This property is valid only if:

- [ILocalLinearPatternFeatureData::RotateInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.md) is true,

     - and -

- [ILocalLinearPatternFeatureData::FixedAxisOfRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~FixedAxisOfRotation.md) is true.

If this property is set to true, you can specify how to align pattern instances to the seed component using [ILocalLinearPatternFeatureData::SeedAlignmentReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SeedAlignmentReferencePoint.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)
