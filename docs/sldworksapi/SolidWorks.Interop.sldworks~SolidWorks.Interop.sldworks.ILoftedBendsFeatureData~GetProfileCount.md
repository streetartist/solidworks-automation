# GetProfileCount Method (ILoftedBendsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~GetProfileCount`

Gets the number of profiles in this lofted bends feature.
Gets the number of profiles in this lofted bends feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProfileCount() As System.Integer
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Integer
 
value = instance.GetProfileCount()
```

```

System.int GetProfileCount()
```

```

System.int GetProfileCount(); 
```

#### Return Value

Number of profiles

Remarks

Call this method before calling [ILoftedBendsFeatureData::IGetProfiles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~IGetProfiles.md) to determine the size of the array for that method.

Example

See examples for [ILoftedBendsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::ISetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ISetProfiles.md)  
[ILoftedBendsFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~Profiles.md)
