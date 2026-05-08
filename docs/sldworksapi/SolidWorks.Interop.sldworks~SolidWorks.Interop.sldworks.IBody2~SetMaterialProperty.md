# SetMaterialProperty Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty`

Sets the material for this body.
Sets the material for this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMaterialProperty( _
   ByVal ConfigName As System.String, _
   ByVal Database As System.String, _
   ByVal MaterialName As System.String _
) As System.Integer
```

```

Dim instance As IBody2
Dim ConfigName As System.String
Dim Database As System.String
Dim MaterialName As System.String
Dim value As System.Integer
 
value = instance.SetMaterialProperty(ConfigName, Database, MaterialName)
```

```

System.int SetMaterialProperty( 
   System.string ConfigName,
   System.string Database,
   System.string MaterialName
)
```

```

System.int SetMaterialProperty( 
   System.String^ ConfigName,
   System.String^ Database,
   System.String^ MaterialName
) 
```

#### Parameters

*ConfigName*
:   Name of configuration

*Database*
:   "solidworks material.sldmat" or **""** or "custom materials.sldmat" (see **Remarks**)

*MaterialName*
:   Name of the SOLIDWORKS material to apply to the body (see **Remarks**)

#### Return Value

Return status as defined by [swBodyMaterialApplicationError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyMaterialApplicationError_e.html)

Remarks

Click **Tools > Options > System Options > File Locations > Material Databases** to verify that a folder for Database is specified.

You can only use materials from a valid SOLIDWORKS materials database. You can specify either "solidworks materials.sldmat" or "" for the SOLIDWORKS Materials database or "custom materials.sldmat" for the Custom Materials database.

You can also find out the names of the materials in the materials database by opening the database as an XML stream and work with the XML API to get the data.

Example

[Set Material (C#)](Set_Material_Example_CSharp.htm)  
[Set Material (VB.NET)](Set_Material_Example_VBNET.htm)  
[Set Material (VBA)](Set_Material_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.md)  
[IBody2::GetMaterialPropertyName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.md)  
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.md)  
[IBody2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.md)  
[IBody2::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.md)  
[IBody2::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.md)  
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.md)  
[IBody2::SetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.md)  
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.md)  
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.md)  
[IBody2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HasMaterialPropertyValues.md)
