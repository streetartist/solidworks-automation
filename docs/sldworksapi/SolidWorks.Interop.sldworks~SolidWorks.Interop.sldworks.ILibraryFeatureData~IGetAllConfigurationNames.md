# IGetAllConfigurationNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetAllConfigurationNames`

Gets the names of the library feature configurations.
Gets the names of the library feature configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAllConfigurationNames( _
   ByVal Count As System.Integer _
) As System.String
```

```

Dim instance As ILibraryFeatureData
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetAllConfigurationNames(Count)
```

```

System.string IGetAllConfigurationNames( 
   System.int Count
)
```

```

System.String^ IGetAllConfigurationNames( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of library configurations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the library feature configurations

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ILibraryFeatureData::GetConfigurationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetConfigurationCount.md) to determine the size of the array.

If the library feature part document is not open or the library feature is not linked to the library feature part, then only the name of the active library feature configuration is returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::GetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetAllConfigurationNames.md)  
[ILibraryFeatureData::ConfigurationName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ConfigurationName.md)
