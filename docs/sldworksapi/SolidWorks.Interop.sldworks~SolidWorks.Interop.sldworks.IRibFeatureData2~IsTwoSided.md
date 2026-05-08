# IsTwoSided Property (IRibFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~IsTwoSided`

Gets or sets whether the rib is created on two sides of the midplane or in a single direction (see IRibFeatureData2::ReverseThicknessDir).
Gets or sets whether the rib is created on two sides of the midplane or in a single direction (see [IRibFeatureData2::ReverseThicknessDir](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ReverseThicknessDir.md)).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsTwoSided As System.Boolean
```

```

Dim instance As IRibFeatureData2
Dim value As System.Boolean
 
instance.IsTwoSided = value
 
value = instance.IsTwoSided
```

```

System.bool IsTwoSided {get; set;}
```

```

property System.bool IsTwoSided {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the rib is extruded either side of the midplane, false if it is single-sided

Remarks

Changing the value of this property does not affect geometry until [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) is called.

Example

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)
