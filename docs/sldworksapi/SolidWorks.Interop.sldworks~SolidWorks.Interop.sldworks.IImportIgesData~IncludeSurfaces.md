# IncludeSurfaces Property (IImportIgesData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeSurfaces`

Gets or sets whether to import surfaces.
Gets or sets whether to import surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeSurfaces As System.Boolean
```

```

Dim instance As IImportIgesData
Dim value As System.Boolean
 
instance.IncludeSurfaces = value
 
value = instance.IncludeSurfaces
```

```

System.bool IncludeSurfaces {get; set;}
```

```

property System.bool IncludeSurfaces {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import surfaces, false to not

Remarks

To import curves, use [IImportIgesData::IncludeCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeCurves.md) and [IImportIgesData::CurvesAsSketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~CurvesAsSketches.md).

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
[IImportIgesData::ProcessByLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.md)
