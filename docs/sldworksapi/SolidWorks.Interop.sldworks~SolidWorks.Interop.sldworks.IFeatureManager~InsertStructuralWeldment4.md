# InsertStructuralWeldment4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment4`

Obsolete. Superseded by IFeatureManager::InsertStructuralWeldment5.
Obsolete. Superseded by [IFeatureManager::InsertStructuralWeldment5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertStructuralWeldment4( _
   ByVal Path As System.String, _
   ByVal ConnectedSegmentsOption As System.Integer, _
   ByVal AllowProtrusion As System.Boolean, _
   ByVal Groups As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Path As System.String
Dim ConnectedSegmentsOption As System.Integer
Dim AllowProtrusion As System.Boolean
Dim Groups As System.Object
Dim value As Feature
 
value = instance.InsertStructuralWeldment4(Path, ConnectedSegmentsOption, AllowProtrusion, Groups)
```

```

Feature InsertStructuralWeldment4( 
   System.string Path,
   System.int ConnectedSegmentsOption,
   System.bool AllowProtrusion,
   System.object Groups
)
```

```

Feature^ InsertStructuralWeldment4( 
   System.String^ Path,
   System.int ConnectedSegmentsOption,
   System.bool AllowProtrusion,
   System.Object^ Groups
) 
```

#### Parameters

*Path*
:   Full path name of the type of structural member (see **Remarks**)

*ConnectedSegmentsOption*
:   Option as defined in [swConnectedSegmentsOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConnectedSegmentsOption_e.html)

*AllowProtrusion*
:   True to allow protrusion, false to not

*Groups*
:   Array of [IStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Populate Path using a weldment profile (\*.**sldlfp**) from *install\_dir*\**lang**\*lang*\**weldment profiles**.

Use [IFeatureManager::CreateStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.md), [IStructuralMemberFeatureData::Groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.md), or [IStructuralMemberFeatureData::IGetGroups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.md) to populate the Groups parameter.

Example

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)  
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)  
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)
