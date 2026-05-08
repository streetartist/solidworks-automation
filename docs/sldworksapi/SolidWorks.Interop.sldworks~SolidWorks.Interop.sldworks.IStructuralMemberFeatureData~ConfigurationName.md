# ConfigurationName Property (IStructuralMemberFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConfigurationName`

Gets or sets the name of the configuration in the custom weldment profile for this structural member.
Gets or sets the name of the configuration in the custom weldment profile for this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConfigurationName As System.String
```

```

Dim instance As IStructuralMemberFeatureData
Dim value As System.String
 
instance.ConfigurationName = value
 
value = instance.ConfigurationName
```

```

System.string ConfigurationName {get; set;}
```

```

property System.String^ ConfigurationName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the configuration in the custom weldment profile or an empty string (see **Remarks**)

Remarks

An empty string indicates that a configuration in a custom weldment profile was not used for this structural member.

See:

- [IFeatureManager::InsertStructuralWeldment5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment5.md) for details about inserting a structural member using a configuration in a custom weldment profile.
- SOLIDWORKS Help for details about custom weldment profiles.

Example

[Insert Structural Weldments Using Custom Weldment Profile (C#)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_CSharp.htm)  
[Insert Structural Weldments Using Custom Weldment Profile (VB.NET)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VBNET.htm)  
[Insert Structural Weldments Using Custom Weldment Profile (VBA)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)
