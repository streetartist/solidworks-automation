# NameModifier Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifier`

Gets or sets the prefix or suffix to add to the file or configuration names of the components to be mirrored.
Gets or sets the prefix or suffix to add to the file or configuration names of the components to be mirrored.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NameModifier As System.String
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.String
 
instance.NameModifier = value
 
value = instance.NameModifier
```

```

System.string NameModifier {get; set;}
```

```

property System.String^ NameModifier {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Prefix or suffix text; "Mirror" by default

Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::NameModifierType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType.md) is either [swMirrorComponentNameModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentNameModifier_e.html).swMirrorComponentName\_Prefix or swMirrorComponentNameModifier\_e.swMirrorComponentNameName\_Suffix,

    - and -

- [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.md) is not Nothing or null,

    - and -

- [IMirrorComponentFeatureData::MirroredComponentFilenames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.md) is not Nothing or null.

If [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.md) is:

- True, then this property prepends a prefix or appends a suffix to the configuration name of the original component to create new opposite-hand version configuration names.
- False, then this property prepends a prefix or appends a suffix to the orginal component file name to create new opposite-hand version file names.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
