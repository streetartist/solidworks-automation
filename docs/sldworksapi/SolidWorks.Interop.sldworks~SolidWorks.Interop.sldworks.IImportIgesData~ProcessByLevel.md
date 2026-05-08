# ProcessByLevel Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel`

Gets or sets whether to process surfaces together.
Gets or sets whether to process surfaces together.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProcessByLevel As System.Boolean
```

```

Dim instance As IImportIgesData
Dim value As System.Boolean
 
instance.ProcessByLevel = value
 
value = instance.ProcessByLevel
```

```

System.bool ProcessByLevel {get; set;}
```

```

property System.bool ProcessByLevel {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to process surfaces on the same IGES level together in their own folder in the FeatureManager design tree, false to process surfaces to level 0 and not put them in their own folder in the FeatureManager design tree

Example

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.md)  
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.md)  
[IImportIgesData::SetLevels Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~SetLevels.md)  
[IImportIgesData::IncludeAllLevels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeAllLevels.md)  
[IImportIgesData::IncludeOnlyLevels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeOnlyLevels.md)  
[IImportIgesData::IncludeSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeSurfaces.md)
