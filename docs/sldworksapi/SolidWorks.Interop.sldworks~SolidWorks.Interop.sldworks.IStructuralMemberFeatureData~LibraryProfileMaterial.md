# LibraryProfileMaterial Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LibraryProfileMaterial`

Gets the name of the material for the library profile for this structural member.
Gets the name of the material for the library profile for this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property LibraryProfileMaterial As System.String
```

```

Dim instance As IStructuralMemberFeatureData
Dim value As System.String
 
value = instance.LibraryProfileMaterial
```

```

System.string LibraryProfileMaterial {get;}
```

```

property System.String^ LibraryProfileMaterial {
   System.String^ get();
}
```

#### Property Value

Name of the material for this library profile

Remarks

You can [transfer material properties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~TransferMaterial.md) of a library profile:

- when you use it as a structural member.
- that has a configuration-specific material.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

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
[IStructuralMemberFeatureData::ConfigurationName Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConfigurationName.md)
