# CreateStructuralMemberGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup`

Creates a weldment structural-member group.
Creates a weldment structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateStructuralMemberGroup() As StructuralMemberGroup
```

```

Dim instance As IFeatureManager
Dim value As StructuralMemberGroup
 
value = instance.CreateStructuralMemberGroup()
```

```

StructuralMemberGroup CreateStructuralMemberGroup()
```

```

StructuralMemberGroup^ CreateStructuralMemberGroup(); 
```

#### Return Value

[Structural-member group](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)

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

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IStructuralMemberFeatureData::ISetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups.md)  
[IFeatureManager::InsertStructuralWeldment3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.md)
