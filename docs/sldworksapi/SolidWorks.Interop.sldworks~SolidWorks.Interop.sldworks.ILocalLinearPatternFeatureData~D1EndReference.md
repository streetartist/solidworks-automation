# D1EndReference Property (ILocalLinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndReference`

Gets or sets the up-to reference entity in Direction 1 for this linear component pattern feature.
Gets or sets the up-to reference entity in Direction 1 for this linear component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1EndReference As System.Object
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Object
 
instance.D1EndReference = value
 
value = instance.D1EndReference
```

```

System.object D1EndReference {get; set;}
```

```

property System.Object^ D1EndReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pattern's up-to reference ([vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)) in Direction 1

Remarks

This property is valid only if [ILocalLinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndCondition.md) is set to [swPatternEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition\_UpToReference.

To pre-select, use selection Mark = 256.

During edit of this property, if you specify an invalid entity [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) returns false and the feature does not roll back. To roll back the feature, call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md) or move the rollback bar in the user interface to before and after the feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)  
[ILocalLinearPatternFeatureData::D1EndReferenceType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndReferenceType.md)
