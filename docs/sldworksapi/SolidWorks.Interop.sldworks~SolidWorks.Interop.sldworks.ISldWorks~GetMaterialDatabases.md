# GetMaterialDatabases Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabases`

Gets the names of the material databases.
Gets the names of the material databases.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterialDatabases() As System.Object
```

```

Dim instance As ISldWorks
Dim value As System.Object
 
value = instance.GetMaterialDatabases()
```

```

System.object GetMaterialDatabases()
```

```

System.Object^ GetMaterialDatabases(); 
```

#### Return Value

Array of strings of the names of the material databases

Remarks

Material database names must be unique. Do not re-use the name of a material database.

Example

[Get Material Database and XML Schema File Names (VBA)](Get_Material_Database_and_XML_Schema_File_Names_Example_VB.htm)  
[Get Material Database Paths of Document (VBA)](Get_Material_Database_Paths_of_Document_Example_VB.htm)  
[Set Material (C#)](Set_Material_Example_CSharp.htm)  
[Set Material (VB.NET)](Set_Material_Example_VBNET.htm)  
[Set Material (VBA)](Set_Material_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetMaterialDatabaseCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabaseCount.md)  
[ISldWorks::IGetMaterialDatabases Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMaterialDatabases.md)  
[ISldWorks::GetMaterialSchemaPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialSchemaPathName.md)
