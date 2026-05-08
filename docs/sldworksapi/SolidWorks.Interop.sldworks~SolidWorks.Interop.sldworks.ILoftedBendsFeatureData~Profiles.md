# Profiles Property (ILoftedBendsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~Profiles`

Gets or sets the profiles for this lofted bends feature.
Gets or sets the profiles for this lofted bends feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Profiles As System.Object
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Object
 
instance.Profiles = value
 
value = instance.Profiles
```

```

System.object Profiles {get; set;}
```

```

property System.Object^ Profiles {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of profiles for this lofted bends feature

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::GetProfileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~GetProfileCount.md)  
[ILoftedBendsFeatureData::IGetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~IGetProfiles.md)  
[ILoftedBendsFeatureData::ISetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ISetProfiles.md)
