# ISetProfiles Method (ILoftedBendsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ISetProfiles`

Sets the profiles for this lofted bends feature.
Sets the profiles for this lofted bends feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetProfiles( _
   ByVal Count As System.Integer, _
   ByRef PDisp As System.Object _
) 
```

```

Dim instance As ILoftedBendsFeatureData
Dim Count As System.Integer
Dim PDisp As System.Object
 
instance.ISetProfiles(Count, PDisp)
```

```

void ISetProfiles( 
   System.int Count,
   ref System.object PDisp
)
```

```

void ISetProfiles( 
   System.int Count,
   System.Object^% PDisp
) 
```

#### Parameters

*Count*
:   Number of profiles

*PDisp*
:   in-process, unmanaged C++: Pointer to an array of profiles of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::GetProfileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~GetProfileCount.md)  
[ILoftedBendsFeatureData::IGetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~IGetProfiles.md)  
[ILoftedBendsFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~Profiles.md)
