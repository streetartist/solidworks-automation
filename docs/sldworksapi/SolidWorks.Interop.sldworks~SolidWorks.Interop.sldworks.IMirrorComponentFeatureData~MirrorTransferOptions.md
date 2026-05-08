# MirrorTransferOptions Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorTransferOptions`

Gets or sets the items to transfer to the opposite-hand versions.
Gets or sets the items to transfer to the opposite-hand versions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MirrorTransferOptions As System.Integer
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Integer
 
instance.MirrorTransferOptions = value
 
value = instance.MirrorTransferOptions
```

```

System.int MirrorTransferOptions {get; set;}
```

```

property System.int MirrorTransferOptions {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Items to transfer as defined in [swMirrorPartOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorPartOptions_e.html)

Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.md) is false,

    - and -

- [IMirrorComponentFeatureData::BreakLinksToOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart.md) is false.

If not set, this property defaults to swMirrorPartOptions\_e.swMirrorPartoptions\_ImportSolids.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
