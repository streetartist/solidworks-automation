# DraftAngle Property (IRibFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftAngle`

Gets or sets the draft angle for the rib.
Gets or sets the draft angle for the rib.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DraftAngle As System.Double
```

```

Dim instance As IRibFeatureData2
Dim value As System.Double
 
instance.DraftAngle = value
 
value = instance.DraftAngle
```

```

System.double DraftAngle {get; set;}
```

```

property System.double DraftAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle for the draft

Remarks

Changing the value of this property does not affect geometry until [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) is called.

This property is valid only when [IRibFeatureData2::EnableDraft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~EnableDraft.md) is set to true.

Example

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)  
[IRibFeatureData2::RefSketchIndex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~RefSketchIndex.md)
