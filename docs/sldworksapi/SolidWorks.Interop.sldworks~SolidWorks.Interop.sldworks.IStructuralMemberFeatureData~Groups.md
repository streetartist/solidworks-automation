# Groups Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups`

Gets or sets the groups to use in this structural member.
Gets or sets the groups to use in this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Groups As System.Object
```

```

Dim instance As IStructuralMemberFeatureData
Dim value As System.Object
 
instance.Groups = value
 
value = instance.Groups
```

```

System.object Groups {get; set;}
```

```

property System.Object^ Groups {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md) objects

Remarks

This method works only for features that support groups. A feature supports groups only if [IStructuralMemberFeatureData::GetGroupsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetGroupsCount.md) > 0.

Call [IFeatureManager::CreateStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.md) to create groups.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)  
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)  
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)  
[Create Structural-Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)  
[Create Structural-Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)  
[Create Structural-Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)  
[IStructuralMemberFeatureData::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.md)  
[IStructuralMemberFeatureData::ISetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups.md)  
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)
