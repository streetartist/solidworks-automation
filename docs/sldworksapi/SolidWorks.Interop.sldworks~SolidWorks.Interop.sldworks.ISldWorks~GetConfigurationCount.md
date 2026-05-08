# GetConfigurationCount Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationCount`

Gets the number of configurations in the SOLIDWORKS document, whether the document is opened or closed.
Gets the number of configurations in the SOLIDWORKS document, whether the document is opened or closed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConfigurationCount( _
   ByVal FilePathName As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim value As System.Integer
 
value = instance.GetConfigurationCount(FilePathName)
```

```

System.int GetConfigurationCount( 
   System.string FilePathName
)
```

```

System.int GetConfigurationCount( 
   System.String^ FilePathName
) 
```

#### Parameters

*FilePathName*
:   Path and file name for the SOLIDWORKS document

#### Return Value

Number of configurations in SOLIDWORKS document

Remarks

Call this method before calling [ISldWorks::IGetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetConfigurationNames.md) to get the size of the array for that method.

Example

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationNames.md)  
[ISldWorks::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetConfigurationNames.md)  
[ISldWorks::GetActiveConfigurationName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveConfigurationName.md)  
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)
