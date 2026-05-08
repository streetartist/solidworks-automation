# GetMaterialPropertyName2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2`

Gets the names of the material database and the material for the specified configuration.
Gets the names of the material database and the material for the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterialPropertyName2( _
   ByVal ConfigName As System.String, _
   ByRef Database As System.String _
) As System.String
```

```

Dim instance As IPartDoc
Dim ConfigName As System.String
Dim Database As System.String
Dim value As System.String
 
value = instance.GetMaterialPropertyName2(ConfigName, Database)
```

```

System.string GetMaterialPropertyName2( 
   System.string ConfigName,
   out System.string Database
)
```

```

System.String^ GetMaterialPropertyName2( 
   System.String^ ConfigName,
   [Out] System.String^ Database
) 
```

#### Parameters

*ConfigName*
:   Name of configuration  (see **Remarks**)

*Database*
:   Name of material database

#### Return Value

Name of material

Remarks

This method gets the name of the material database and an entry in the material database that you need for the XML lookup. Open the database as an XML stream and work with the XML API to get the data.

|  |  |
| --- | --- |
| **If...** | **Then...** |
| Only the default configuration exists for the part | Use "" for ConfigName |
| A material was not applied to the configuration | Database name and return value are blank |

Example

[Get Material Database Paths of Document (VBA)](Get_Material_Database_Paths_of_Document_Example_VB.htm)  
[Get Material (VBA)](Get_Material_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.md)  
[IPartDoc::SetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.md)  
[IPartDoc::SetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.md)  
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.md)  
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.md)  
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.md)  
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.md)
