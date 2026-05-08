# SetMaterialPropertyName2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2`

Sets the name of the material property for the specified configuration.
Sets the name of the material property for the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetMaterialPropertyName2( _
   ByVal ConfigName As System.String, _
   ByVal Database As System.String, _
   ByVal Name As System.String _
) 
```

```

Dim instance As IPartDoc
Dim ConfigName As System.String
Dim Database As System.String
Dim Name As System.String
 
instance.SetMaterialPropertyName2(ConfigName, Database, Name)
```

```

void SetMaterialPropertyName2( 
   System.string ConfigName,
   System.string Database,
   System.string Name
)
```

```

void SetMaterialPropertyName2( 
   System.String^ ConfigName,
   System.String^ Database,
   System.String^ Name
) 
```

#### Parameters

*ConfigName*
:   Name of configuration

*Database*
:   Name of the material database (see **Remarks**)

*Name*
:   Name of material (see **Remarks**)

Remarks

This method only supports parts.

Click **Tools > Options > System Options > File Locations > Material Databases** to verify that a folder for Database is specified.

If Database is an empty string, then the default sldmaterials is used. Otherwise, specify the material database file name with the .sldmat filename extension. For example:

PartDoc.SetMaterialPropertyName2 "AddHoles", "solidworks materials.sldmat", "Alloy Steel"

- or -

PartDoc.SetMaterialPropertyName2 "AddHoles", "c:\Program Files\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Alloy Steel"

To remove a material, pass an empty string to Name.

Example

[Get and Set Material Visual Properties (VBA)](Get_and_Set_Material_Visual_Properties_Example_VB.htm)  
[Get and Set Material Visual Properties (VB.NET)](Get_and_Set_Material_Visual_Properties_Example_VBNET.htm)  
[Get and Set Material Visual Properties (C#)](Get_and_Set_Material_Visual_Properties_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.md)  
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.md)  
[IPartDoc::SetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.md)  
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.md)  
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.md)  
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.md)  
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.md)
