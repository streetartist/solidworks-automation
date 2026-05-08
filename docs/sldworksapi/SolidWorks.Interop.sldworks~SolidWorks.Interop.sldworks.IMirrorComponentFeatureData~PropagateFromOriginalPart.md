# PropagateFromOriginalPart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PropagateFromOriginalPart`

Gets or sets whether to propagate visual properties from the orginal part to the opposite-hand versions.
Gets or sets whether to propagate visual properties from the orginal part to the opposite-hand versions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateFromOriginalPart As System.Boolean
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean
 
instance.PropagateFromOriginalPart = value
 
value = instance.PropagateFromOriginalPart
```

```

System.bool PropagateFromOriginalPart {get; set;}
```

```

property System.bool PropagateFromOriginalPart {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to propagate visual properties from the original part, false to not

Remarks

This property is valid only if [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.md) is false.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
