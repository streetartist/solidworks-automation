# ISetProfiles Method (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetProfiles`

Sets the profiles for this loft feature.
Sets the profiles for this loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetProfiles( _
   ByVal Count As System.Short, _
   ByRef PDisp As System.Object _
) 
```

```

Dim instance As ILoftFeatureData
Dim Count As System.Short
Dim PDisp As System.Object
 
instance.ISetProfiles(Count, PDisp)
```

```

void ISetProfiles( 
   System.short Count,
   ref System.object PDisp
)
```

```

void ISetProfiles( 
   System.short Count,
   System.Object^% PDisp
) 
```

#### Parameters

*Count*
:   Number of profiles

*PDisp*
:   - in-process, unmanaged C++: Pointer to an array of profiles of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Each profile is an [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object that contains a [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)  
[ILoftFeatureData::GetProfileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetProfileCount.md)  
[ILoftFeatureData::IGetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetProfiles.md)  
[ILoftFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Profiles.md)
