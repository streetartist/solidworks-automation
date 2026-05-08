# ISetGroups Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups`

Sets the structural-member groups to use in this structural member.
Sets the structural-member groups to use in this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetGroups( _
   ByVal Count As System.Integer, _
   ByRef SegGroups As StructuralMemberGroup _
) 
```

```

Dim instance As IStructuralMemberFeatureData
Dim Count As System.Integer
Dim SegGroups As StructuralMemberGroup
 
instance.ISetGroups(Count, SegGroups)
```

```

void ISetGroups( 
   System.int Count,
   ref StructuralMemberGroup SegGroups
)
```

```

void ISetGroups( 
   System.int Count,
   StructuralMemberGroup^% SegGroups
) 
```

#### Parameters

*Count*
:   Number of structural-member groups

*SegGroups*
:   - in-process, unmanaged C++: Pointer to an array of [structural-member groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method works only for features that support groups. A feature supports groups only if [IStructuralMemberFeatureData::GetGroupsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetGroupsCount.md) > 0.

Call [IFeatureManager::CreateStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.md) to create groups.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)  
[IStructuralMemberFeatureData::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.md)  
[IStructuralMemberFeatureData::Groups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.md)  
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)
