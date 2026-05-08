# IGetConfigurationNames Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetConfigurationNames`

Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed.
Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConfigurationNames( _
   ByVal FilePathName As System.String, _
   ByVal Count As System.Integer _
) As System.String
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetConfigurationNames(FilePathName, Count)
```

```

System.string IGetConfigurationNames( 
   System.string FilePathName,
   System.int Count
)
```

```

System.String^ IGetConfigurationNames( 
   System.String^ FilePathName,
   System.int Count
) 
```

#### Parameters

*FilePathName*
:   Path and file name for the SOLIDWORKS document

*Count*
:   Number of configurations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings containing the names of the configurations in this SOLIDWORKS document

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISldWorks::GetConfigurationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationCount.md) to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetActiveConfigurationName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveConfigurationName.md)  
[ISldWorks::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationNames.md)  
[IModelDoc2::GetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.md)  
[IModelDoc2::IGetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.md)  
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)
