# CreateDerivedConfigurations Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations`

Gets or sets whether to create a derived configuration of the opposite-hand components in the original assembly.
Gets or sets whether to create a derived configuration of the opposite-hand components in the original assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CreateDerivedConfigurations As System.Boolean
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean
 
instance.CreateDerivedConfigurations = value
 
value = instance.CreateDerivedConfigurations
```

```

System.bool CreateDerivedConfigurations {get; set;}
```

```

property System.bool CreateDerivedConfigurations {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to create a derived configuration of the opposite-hand components in the original assembly, false (default) to create new part files

Remarks

This property is valid only:

- If [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.md) is not Nothing or null.
- At creation time. You cannot edit this property after it is set.

| If this property is... | And [IMirrorComponentFeatureData::NameModifierType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType.md) is... | Then use... |
| --- | --- | --- |
| True | - swMirrorComponentName\_Prefix       - or -   - swMirrorComponentName\_Suffix | [IMirrorComponentFeatureData::NameModifier](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifier.md) to prepend a prefix or append a suffix to the configuration name of the original component to create a derived configuration name for the new opposite-hand versions. |
| True | swMirrorComponentName\_Custom | [IMirrorComponentFeatureData::MirroredComponentFilenames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.md) to specify the derived configuration name. |
| False | - swMirrorComponentName\_Prefix       - or -   - swMirrorComponentName\_Suffix | IMirrorComponentFeatureData::NameModifier to prepend a prefix or append a suffix to the orginal component file name to create a new opposite-hand version file name. |
| False | swMirrorComponentName\_Custom | IMirrorComponentFeatureData::MirroredComponentFilenames to specify the opposite-hand version file names. |

If you set this property to false, you can also specify the following import features:

- [IMirrorComponentFeatureData::BreakLinksToOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart.md) (if set to false, you can also set [IMirrorComponentFeatureData::DimXpertScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~DimXpertScheme.md) and/or [IMirrorComponentFeatureData::MirrorTransferOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorTransferOptions.md))
- [IMirrorComponentFeatureData::PreserveZAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PreserveZAxis.md)
- [IMirrorComponentFeatureData::PropagateFromOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PropagateFromOriginalPart.md)

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
