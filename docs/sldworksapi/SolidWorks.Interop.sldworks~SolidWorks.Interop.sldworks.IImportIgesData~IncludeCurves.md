# IncludeCurves Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeCurves`

Gets or sets whether or not to import curves.
Gets or sets whether or not to import curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeCurves As System.Boolean
```

```

Dim instance As IImportIgesData
Dim value As System.Boolean
 
instance.IncludeCurves = value
 
value = instance.IncludeCurves
```

```

System.bool IncludeCurves {get; set;}
```

```

property System.bool IncludeCurves {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import curves, false to not

Remarks

If this property is True, then you can use [IImportIgesData::CurvesAsSketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~CurvesAsSketches.md) to specify whether to import curves as sketches or as reference curve features.

Use [IImportIgesData::IncludeSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeSurfaces.md) to indicate whether or not to import surfaces.

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
