# EnableDraft Property (IRibFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~EnableDraft`

Gets or sets whether the rib has an associated draft.
Gets or sets whether the rib has an associated draft.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableDraft As System.Boolean
```

```

Dim instance As IRibFeatureData2
Dim value As System.Boolean
 
instance.EnableDraft = value
 
value = instance.EnableDraft
```

```

System.bool EnableDraft {get; set;}
```

```

property System.bool EnableDraft {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the rib has a draft, false if not

Remarks

Changing the value of this property does not affect geometry until [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) is called.

Use [IRibFeatureData2::DraftOutward](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftOutward.md) and [IRibFeatureData2::DraftAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftAngle.md) for additional draft control.

Example

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)  
[IRibFeatureData2::RefSketchIndex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~RefSketchIndex.md)
