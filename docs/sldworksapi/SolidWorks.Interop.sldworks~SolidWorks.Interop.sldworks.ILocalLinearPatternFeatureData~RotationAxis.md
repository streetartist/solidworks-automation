# RotationAxis Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotationAxis`

Gets or sets the axis of rotation of components in this linear component pattern feature.
Gets or sets the axis of rotation of components in this linear component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationAxis As System.Object
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Object
 
instance.RotationAxis = value
 
value = instance.RotationAxis
```

```

System.object RotationAxis {get; set;}
```

```

property System.Object^ RotationAxis {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) around which the pattern components rotate

Remarks

This property is valid only if [ILocalLinearPatternFeatureData::RotateInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.md) is true.

The rotation axis must be parallel to [ILocalLinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Axis.md).

Use:

- [ILocalLinearPatternFeatureData::FixedAxisOfRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~FixedAxisOfRotation.md) to specify whether all instances of components rotate about this rotation axis.

- [ILocalLinearPatternFeatureData::ReverseAxisOfRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ReverseAxisOfRotation.md) to reverse the direction of this rotation axis.

You cannot edit this property to null or Nothing after the feature is first created with a rotation axis. If you try, [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) returns false and the feature does not roll back. To roll back the feature, call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md) or move the rollback bar in the user interface to before and after the feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)
