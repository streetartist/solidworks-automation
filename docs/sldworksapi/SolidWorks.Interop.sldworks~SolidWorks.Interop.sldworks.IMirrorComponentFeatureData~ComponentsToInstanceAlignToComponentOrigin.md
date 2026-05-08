# ComponentsToInstanceAlignToComponentOrigin Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin`

Gets or sets the array of components whose orientation axes align to origins.
Gets or sets the array of components whose orientation axes align to origins.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ComponentsToInstanceAlignToComponentOrigin As System.Object
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Object
 
instance.ComponentsToInstanceAlignToComponentOrigin = value
 
value = instance.ComponentsToInstanceAlignToComponentOrigin
```

```

System.object ComponentsToInstanceAlignToComponentOrigin {get; set;}
```

```

property System.Object^ ComponentsToInstanceAlignToComponentOrigin {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

This property is valid only for components for which you are *not* creating opposite-hand versions. Use [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.md) to specify components for which you are creating opposite-hand versions.

Use [IMirrorComponentFeatureData::ComponentOrientationsAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToComponentOrigin.md) to specify the orientation of each component in this array.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
