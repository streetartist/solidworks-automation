# InsertStructuralWeldment5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment5`

Inserts a structural weldment feature.
Inserts a structural weldment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertStructuralWeldment5( _
   ByVal Path As System.String, _
   ByVal ConnectedSegmentsOption As System.Integer, _
   ByVal AllowProtrusion As System.Boolean, _
   ByVal Groups As System.Object, _
   ByVal ConfigurationName As System.String _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Path As System.String
Dim ConnectedSegmentsOption As System.Integer
Dim AllowProtrusion As System.Boolean
Dim Groups As System.Object
Dim ConfigurationName As System.String
Dim value As Feature
 
value = instance.InsertStructuralWeldment5(Path, ConnectedSegmentsOption, AllowProtrusion, Groups, ConfigurationName)
```

```

Feature InsertStructuralWeldment5( 
   System.string Path,
   System.int ConnectedSegmentsOption,
   System.bool AllowProtrusion,
   System.object Groups,
   System.string ConfigurationName
)
```

```

Feature^ InsertStructuralWeldment5( 
   System.String^ Path,
   System.int ConnectedSegmentsOption,
   System.bool AllowProtrusion,
   System.Object^ Groups,
   System.String^ ConfigurationName
) 
```

#### Parameters

*Path*
:   Path and file name of the type of structural member (see **Remarks**)

*ConnectedSegmentsOption*
:   Option as defined in [swConnectedSegmentsOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConnectedSegmentsOption_e.html)

*AllowProtrusion*
:   True to allow protrusion, false to not

*Groups*
:   Array of [IStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md) objects

*ConfigurationName*
:   Name of the configuration in a custom weldment profile or an empty string (see **Remarks**)

#### Return Value

Structural weldment [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Specify Path using either:

- SOLIDWORKS-supplied weldment profile (\*.**sldlfp**) from *install\_dir*\**lang**\*lang*\**weldment profiles  
  -** or -
- custom weldment profile (\*.**sldlfp**); see the SOLIDWORKS Help for details about custom weldment profiles

| If using... | Then specify ConfigurationName as... |
| --- | --- |
| SOLIDWORKS-supplied weldment profile | Empty string |
| Custom weldment profile | Name of the configuration in the custom weldment profile |

Use [IFeatureManager::CreateStructuralMemberGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.md), [IStructuralMemberFeatureData::Groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.md), or [IStructuralMemberFeatureData::IGetGroups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.md) to populate the Groups parameter.

Example

[Insert Structural Weldments Using Custom Weldment Profile (C#)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_CSharp.htm)  
[Insert Structural Weldments Using Custom Weldment Profile (VB.NET)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VBNET.htm)  
[Insert Structural Weldments Using Custom Weldment Profile (VBA)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberFeatureData::ConfigurationName Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConfigurationName.md)
