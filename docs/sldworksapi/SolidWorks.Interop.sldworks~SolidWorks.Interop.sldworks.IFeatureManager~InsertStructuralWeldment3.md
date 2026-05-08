# InsertStructuralWeldment3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3`

Obsolete. Superseded by IFeatureManager::InsertStructuralWeldment4.
Obsolete. Superseded by [IFeatureManager::InsertStructuralWeldment4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertStructuralWeldment3( _
   ByVal Path As System.String, _
   ByVal EndCond As System.Integer, _
   ByVal Angle As System.Double, _
   ByVal Merge As System.Boolean, _
   ByVal Groups As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Path As System.String
Dim EndCond As System.Integer
Dim Angle As System.Double
Dim Merge As System.Boolean
Dim Groups As System.Object
Dim value As Feature
 
value = instance.InsertStructuralWeldment3(Path, EndCond, Angle, Merge, Groups)
```

```

Feature InsertStructuralWeldment3( 
   System.string Path,
   System.int EndCond,
   System.double Angle,
   System.bool Merge,
   System.object Groups
)
```

```

Feature^ InsertStructuralWeldment3( 
   System.String^ Path,
   System.int EndCond,
   System.double Angle,
   System.bool Merge,
   System.Object^ Groups
) 
```

#### Parameters

*Path*
:   Path, filename, and name of the type of structural member to insert

*EndCond*
:   End condition as defined in [swSOLIDWORKSWeldmentEndCondOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)

*Angle*
:   Angle of rotation of the sketch about the sketch segment

*Merge*
:   True to merge the bodies of the arc segments to the adjacent bodies, false to not

*Groups*
:   :   Array of [IStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Use [IFeatureManager::CreateStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.md), [IStructuralMemberFeatureData::Groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.md), or [IStructuralMemberFeatureData::IGetGroups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.md) to populate the *Groups* parameter.

Example

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)  
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)  
[Create Structural-Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)  
[Create Structural-Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)  
[Create Structural-Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)  
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)
