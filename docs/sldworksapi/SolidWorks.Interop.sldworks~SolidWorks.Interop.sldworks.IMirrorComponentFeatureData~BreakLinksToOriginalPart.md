# BreakLinksToOriginalPart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart`

Gets or sets whether to break links between opposite-hand components and original components.
Gets or sets whether to break links between opposite-hand components and original components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BreakLinksToOriginalPart As System.Boolean
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean
 
instance.BreakLinksToOriginalPart = value
 
value = instance.BreakLinksToOriginalPart
```

```

System.bool BreakLinksToOriginalPart {get; set;}
```

```

property System.bool BreakLinksToOriginalPart {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to break links, false (default) to not

Remarks

This property is valid only if [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.md) is false.

If you set this property to true, then changes made to the original component do not propagate to the opposite-hand version.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
