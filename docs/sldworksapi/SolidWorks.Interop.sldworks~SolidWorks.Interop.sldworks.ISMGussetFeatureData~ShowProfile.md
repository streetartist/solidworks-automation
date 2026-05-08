# ShowProfile Property (ISMGussetFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ShowProfile`

Gets or sets whether to display the profile of the gusset in its flattened state.
Gets or sets whether to display the profile of the gusset in its flattened state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowProfile As System.Boolean
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Boolean
 
instance.ShowProfile = value
 
value = instance.ShowProfile
```

```

System.bool ShowProfile {get; set;}
```

```

property System.bool ShowProfile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the profile of the flattened gusset, false to not

Remarks

This property is valid only if [ISMGussetFeatureData::OverrideDocSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OverrideDocSettings.md) is true.

Example

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[ISMGussetFeatureData::ShowCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ShowCenter.md)
