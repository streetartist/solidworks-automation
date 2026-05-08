# IImportStepData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData`

Allows you to specify values when importing STEP data.
Allows you to specify values when importing STEP data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IImportStepData 
```

```

Dim instance As IImportStepData
```

```

public interface IImportStepData 
```

```

public interface class IImportStepData 
```

Remarks

1. Use [ISldWorks::GetImportFileData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExportFileData.md) to get an IImportStepData interface pointer.
2. Use [IImportStepData::MapConfigurationData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData~MapConfigurationData.md) to specify how to map configuration data.
3. Use [ISldWorks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md) to load the file.

When IImportStepData is initialized, the current default environment setting, [swImportStepConfigData](ms-help://SolidWorks.Interop.swconst/SolidWorks/FileOpenOptionsGeneral.htm), initializes IImportStepData::MapConfigurationData unless you explicitly set IImportStepData::MapConfigurationData. Then the IImportStepData::MapConfigurationData setting overrides swImportStepConfigData for this import only.

Example

[Import STEP File (C#)](Import_STEP_File_Example_CSharp.htm)  
[Import STEP File (VB.NET)](Import_STEP_File_Example_VBNET.htm)  
[Import STEP File (VBA)](Import_STEP_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportStepData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
