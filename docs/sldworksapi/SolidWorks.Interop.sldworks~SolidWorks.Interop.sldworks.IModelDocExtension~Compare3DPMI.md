# Compare3DPMI Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Compare3DPMI`

Compare DimXpert annotations, reference dimensions, and other annotations between different versions of the same part document.
Compare DimXpert annotations, reference dimensions, and other annotations between different versions of the same part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Compare3DPMI( _
   ByVal ReferenceDocument As System.String, _
   ByVal ModifiedDocument As System.String, _
   ByVal ReportName As System.String, _
   ByVal ReportFolderPath As System.String, _
   ByVal ReportSaveOptions As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim ReferenceDocument As System.String
Dim ModifiedDocument As System.String
Dim ReportName As System.String
Dim ReportFolderPath As System.String
Dim ReportSaveOptions As System.Integer
Dim value As System.Boolean
 
value = instance.Compare3DPMI(ReferenceDocument, ModifiedDocument, ReportName, ReportFolderPath, ReportSaveOptions)
```

```

System.bool Compare3DPMI( 
   System.string ReferenceDocument,
   System.string ModifiedDocument,
   System.string ReportName,
   System.string ReportFolderPath,
   System.int ReportSaveOptions
)
```

```

System.bool Compare3DPMI( 
   System.String^ ReferenceDocument,
   System.String^ ModifiedDocument,
   System.String^ ReportName,
   System.String^ ReportFolderPath,
   System.int ReportSaveOptions
) 
```

#### Parameters

*ReferenceDocument*
:   Path and file name of the open part document

*ModifiedDocument*
:   Path and file name of a different and open version of ReferenceDocument

*ReportName*
:   Name for the report and name of the folder to which to save the report and bitmap image files

*ReportFolderPath*
:   Path to the folder specified in ReportName in which to save the report and bitmap image files

*ReportSaveOptions*
:   Save options for the report as defined in [sw3DPMISaveOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DPMISaveOptions_e.html)

#### Return Value

True if the method executed, false if not

Example

[Compare DimXpert Annotations in Different Versions of Same Part (C#)](Compare_DimXpert_Annotations_in_Different_Versions_of_Same_Part_Example_CSharp.htm)  
[Compare DimXpert Annotations in Different Versions of Same Part (VB.NET)](Compare_DimXpert_Annotations_in_Different_Versions_of_Same_Part_Example_VBNET.htm)  
[Compare DimXpert Annotations in Different Versions of Same Part (VBA)](Compare_DimXpert_Annotations_in_Different_Versions_of_Same_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
