# IGetMaterialDatabases Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMaterialDatabases`

Gets the names of the material databases.
Gets the names of the material databases.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMaterialDatabases( _
   ByVal Count As System.Integer _
) As System.String
```

```

Dim instance As ISldWorks
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetMaterialDatabases(Count)
```

```

System.string IGetMaterialDatabases( 
   System.int Count
)
```

```

System.String^ IGetMaterialDatabases( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of material databases

#### Return Value

- in-process, unmanaged C++: Pointer to the an array of the names of the material databases
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISldWorks::GetMaterialDatabaseCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabaseCount.md) to get the value for Count.

Material database names must be unique. Do not re-use the name of a material database.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetMaterialDatabases Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabases.md)
