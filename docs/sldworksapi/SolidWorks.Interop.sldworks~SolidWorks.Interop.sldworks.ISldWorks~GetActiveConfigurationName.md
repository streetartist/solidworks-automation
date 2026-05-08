# GetActiveConfigurationName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveConfigurationName`

Gets the name of the active configuration in the specified SOLIDWORKS document.
Gets the name of the active configuration in the specified SOLIDWORKS document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetActiveConfigurationName( _
   ByVal FilePathName As System.String _
) As System.String
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim value As System.String
 
value = instance.GetActiveConfigurationName(FilePathName)
```

```

System.string GetActiveConfigurationName( 
   System.string FilePathName
)
```

```

System.String^ GetActiveConfigurationName( 
   System.String^ FilePathName
) 
```

#### Parameters

*FilePathName*
:   Path for the SOLIDWORKS document

#### Return Value

Name of the active configuration

Remarks

The SOLIDWORKS document does not need to be open. The configuration that was active when the SOLIDWORKS document was closed is returned. If the SOLIDWORKS document is open, then the name of the active configuration is returned.

Example

[Get Name of Active Configuration (VBA)](Get_Name_of_Active_Configuration_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationCount.md)  
[ISldWorks::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationNames.md)  
[ISldWorks::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetConfigurationNames.md)  
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.md)  
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.md)  
[IConfiguration::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.md)
