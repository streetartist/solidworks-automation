# ReplaceFileLocations Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ReplaceFileLocations`

Gets or sets the file locations of existing files that are to be replaced with new opposite-hand versions.
Gets or sets the file locations of existing files that are to be replaced with new opposite-hand versions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReplaceFileLocations As System.Object
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Object
 
instance.ReplaceFileLocations = value
 
value = instance.ReplaceFileLocations
```

```

System.object ReplaceFileLocations {get; set;}
```

```

property System.Object^ ReplaceFileLocations {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of existing file paths

Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.md) is false,

    - and -

- [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.md) is not Nothing or null. There is a one-to-one mapping between this property's array and IMirrorComponentFeatureData::OppositeHandComponents.

If this property is not set, it defaults to the current assembly's folder.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
