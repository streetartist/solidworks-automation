# NameModifierType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType`

Gets or sets the type of modifier to apply to the opposite-hand version file name.
Gets or sets the type of modifier to apply to the opposite-hand version file name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NameModifierType As System.Integer
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Integer
 
instance.NameModifierType = value
 
value = instance.NameModifierType
```

```

System.int NameModifierType {get; set;}
```

```

property System.int NameModifierType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of file name modifier as defined in [swMirrorComponentNameModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentNameModifier_e.html)

Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.md) is not Nothing or null,

    - and -

- [IMirrorComponentFeatureData::MirroredComponentFilenames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.md) is not Nothing or null.

If this property is not set, then it defaults to swMirrorComponentNameModifier\_e.swMirrorComponentName\_Prefix.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)  
[IMirrorComponentFeatureData::NameModifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifier.md)
