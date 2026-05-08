# GetConfigurationCount Method (ILibraryFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetConfigurationCount`

Gets the number of library feature configurations.
Gets the number of library feature configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConfigurationCount() As System.Integer
```

```

Dim instance As ILibraryFeatureData
Dim value As System.Integer
 
value = instance.GetConfigurationCount()
```

```

System.int GetConfigurationCount()
```

```

System.int GetConfigurationCount(); 
```

#### Return Value

Number of library feature configurations

Remarks

Call this method before calling [ILibraryFeatureData::IGetAllConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetAllConfigurationNames.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::GetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetAllConfigurationNames.md)  
[ILibraryFeatureData::IGetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetAllConfigurationNames.md)  
[ILibraryFeatureData::ConfigurationName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ConfigurationName.md)
