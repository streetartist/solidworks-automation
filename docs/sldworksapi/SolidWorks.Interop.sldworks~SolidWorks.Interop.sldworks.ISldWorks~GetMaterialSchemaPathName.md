# GetMaterialSchemaPathName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialSchemaPathName`

Gets the path for the XML material schema file.
Gets the path for the XML material schema file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterialSchemaPathName() As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
value = instance.GetMaterialSchemaPathName()
```

```

System.string GetMaterialSchemaPathName()
```

```

System.String^ GetMaterialSchemaPathName(); 
```

#### Return Value

Path for the XML material schema file

Example

[Get Material Database and XML Schema File Names (VBA)](Get_Material_Database_and_XML_Schema_File_Names_Example_VB.htm)  
[Set Material (C#)](Set_Material_Example_CSharp.htm)  
[Set Material (VB.NET)](Set_Material_Example_VBNET.htm)  
[Set Material (VBA)](Set_Material_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IGetMaterialDatabases Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMaterialDatabases.md)  
[ISldWorks::GetMaterialDatabases Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabases.md)  
[ISldWorks::GetMaterialDatabaseCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabaseCount.md)
