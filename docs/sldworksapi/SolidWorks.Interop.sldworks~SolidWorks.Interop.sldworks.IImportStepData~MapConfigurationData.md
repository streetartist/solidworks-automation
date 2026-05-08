# MapConfigurationData Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData~MapConfigurationData`

Gets or sets whether to import the STEP file configuration data plus geometric data or geometric data only.
Gets or sets whether to import the STEP file configuration data plus geometric data or geometric data only.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MapConfigurationData As System.Boolean
```

```

Dim instance As IImportStepData
Dim value As System.Boolean
 
instance.MapConfigurationData = value
 
value = instance.MapConfigurationData
```

```

System.bool MapConfigurationData {get; set;}
```

```

property System.bool MapConfigurationData {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import the STEP file configuration data plus geometric data, false to import geometric data only

Remarks

If this property is not set, then the current default environment setting, [swImportStepConfigData](ms-help://SolidWorks.Interop.swconst/SolidWorks/FileOpenOptionsGeneral.htm), is used. If this property is set, its setting overrides the swImportStepConfigData setting for this import only.

Example

[Import STEP File (C#)](Import_STEP_File_Example_CSharp.htm)  
[Import STEP File (VB.NET)](Import_STEP_File_Example_VBNET.htm)  
[Import STEP File (VBA)](Import_STEP_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportStepData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData.md)  
[IImportStepData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData_members.md)
