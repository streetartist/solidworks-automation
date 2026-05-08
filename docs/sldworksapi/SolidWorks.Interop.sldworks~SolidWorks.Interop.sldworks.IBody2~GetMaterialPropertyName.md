# GetMaterialPropertyName Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName`

Gets the names of the material database and the material for the specified configuration.
Gets the names of the material database and the material for the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterialPropertyName( _
   ByVal ConfigName As System.String, _
   ByRef Database As System.String _
) As System.String
```

```

Dim instance As IBody2
Dim ConfigName As System.String
Dim Database As System.String
Dim value As System.String
 
value = instance.GetMaterialPropertyName(ConfigName, Database)
```

```

System.string GetMaterialPropertyName( 
   System.string ConfigName,
   out System.string Database
)
```

```

System.String^ GetMaterialPropertyName( 
   System.String^ ConfigName,
   [Out] System.String^ Database
) 
```

#### Parameters

*ConfigName*
:   :   Name of configuration (see **Remarks**)

*Database*
:   Name of material database

#### Return Value

Name of material

Remarks

This method gets the name of the material database and an entry in the material database that you need for the XML lookup. Open the database as an XML stream and work with the XML API to get the data.

|  |  |
| --- | --- |
| **If...** | **Then...** |
| Only the Default configuration exists for the part | Use "" for ConfigName |
| A material was not applied to the configuration | Database name and return value are blank |

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
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.md)  
[IBody2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.md)  
[IBody2::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.md)  
[IBody2::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.md)  
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.md)  
[IBody2::SetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.md)  
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.md)  
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.md)  
[IBody2::SetMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.md)  
[IBody2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HasMaterialPropertyValues.md)
