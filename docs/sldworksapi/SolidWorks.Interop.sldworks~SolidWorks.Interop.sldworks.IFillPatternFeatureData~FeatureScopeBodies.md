# FeatureScopeBodies Property (IFillPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeatureScopeBodies`

Gets or sets the solid bodies that the fill pattern feature affects in a multibody part.
Gets or sets the solid bodies that the fill pattern feature affects in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FeatureScopeBodies As System.Object
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Object
 
instance.FeatureScopeBodies = value
 
value = instance.FeatureScopeBodies
```

```

System.object FeatureScopeBodies {get; set;}
```

```

property System.Object^ FeatureScopeBodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that the fill pattern feature affects

Remarks

This property is valid only if:

- [IFillPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~GeometryPattern.md) is true,
- [IFillPatternFeatureData::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeatureScope.md) is true,

    - and -

- [IFillPatternFeatureData::AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~AutoSelect.md) is false.

You cannot edit this property to null or Nothing after the feature is created with feature scope bodies. If you try, [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) returns true but this property does not change.

For more information, see the **Fill Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)
