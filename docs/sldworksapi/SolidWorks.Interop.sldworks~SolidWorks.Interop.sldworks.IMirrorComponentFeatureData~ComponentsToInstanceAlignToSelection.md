# ComponentsToInstanceAlignToSelection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToSelection`

Gets or sets the array of components whose orientation axes align to selected references.
Gets or sets the array of components whose orientation axes align to selected references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ComponentsToInstanceAlignToSelection As System.Object
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Object
 
instance.ComponentsToInstanceAlignToSelection = value
 
value = instance.ComponentsToInstanceAlignToSelection
```

```

System.object ComponentsToInstanceAlignToSelection {get; set;}
```

```

property System.Object^ ComponentsToInstanceAlignToSelection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

This property is valid only for components for which you are *not* creating opposite-hand versions. Use [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.md) to specify components for which you are creating opposite-hand versions.

Use [IMirrorComponentFeatureData::ComponentOrientationsAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToSelection.md) to specify the orientation of each component in this property's array. There is a one-to-one mapping between this property's array and IMirrorComponentFeatureData::ComponentOrientationsAlignToSelection.

Use [IMirrorComponentFeatureData::AlignmentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~AlignmentReferences.md) to specify alignment references. There is a one-to-one mapping between this property's array and IMirrorComponentFeatureData::AlignmentReferences. If this property's array contains more elements than IMirrorComponentFeatureData::AlignmentReferences, then the feature will fail to be created.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
