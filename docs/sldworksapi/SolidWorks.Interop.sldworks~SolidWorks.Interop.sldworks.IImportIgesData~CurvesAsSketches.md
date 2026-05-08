# CurvesAsSketches Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~CurvesAsSketches`

Gets or sets whether the curves are imported as sketches or reference curve features.
Gets or sets whether the curves are imported as sketches or reference curve features.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurvesAsSketches As System.Boolean
```

```

Dim instance As IImportIgesData
Dim value As System.Boolean
 
instance.CurvesAsSketches = value
 
value = instance.CurvesAsSketches
```

```

System.bool CurvesAsSketches {get; set;}
```

```

property System.bool CurvesAsSketches {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import curves as sketches, false to import curves as reference curve features

Remarks

[IImportIgesData::IncludeCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeCurves.md) must be set to true for this property to have an effect.

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
