# ImportDiagnosis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ImportDiagnosis`

Diagnoses and repairs any gaps or bad faces on imported features.
Diagnoses and repairs any gaps or bad faces on imported features.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ImportDiagnosis( _
   ByVal CloseAllGaps As System.Boolean, _
   ByVal RemoveFaces As System.Boolean, _
   ByVal FixFaces As System.Boolean, _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As IPartDoc
Dim CloseAllGaps As System.Boolean
Dim RemoveFaces As System.Boolean
Dim FixFaces As System.Boolean
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.ImportDiagnosis(CloseAllGaps, RemoveFaces, FixFaces, Options)
```

```

System.int ImportDiagnosis( 
   System.bool CloseAllGaps,
   System.bool RemoveFaces,
   System.bool FixFaces,
   System.int Options
)
```

```

System.int ImportDiagnosis( 
   System.bool CloseAllGaps,
   System.bool RemoveFaces,
   System.bool FixFaces,
   System.int Options
) 
```

#### Parameters

*CloseAllGaps*
:   True to repair any gaps, false to not

*RemoveFaces*
:   True to remove any bad faces and create gaps in the feature, false to not

*FixFaces*
:   True to fix the bad faces, false to not

*Options*
:   Not used

#### Return Value

>= 0 if import diagnosis is successful, -1 if an error occurred

Remarks

Use this method for an imported solid body that has rebuild errors or for an imported surface that did not knit into a solid body.

Example

[Import STEP File (C#)](Import_STEP_File_Example_CSharp.htm)  
[Import STEP File (VB.NET)](Import_STEP_File_Example_VBNET.htm)  
[Import STEP File (VBA)](Import_STEP_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ImportDiagnosisGapCloser Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ImportDiagnosisGapCloser.md)  
[IBody2::Diagnose Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Diagnose.md)  
[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md)
