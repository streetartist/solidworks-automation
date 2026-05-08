# SaveToFile3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SaveToFile3`

Saves the selected weldment member, surface body, or solid body to another part document.
Saves the selected weldment member, surface body, or solid body to another part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveToFile3( _
   ByVal Name As System.String, _
   ByVal Options As System.Integer, _
   ByVal CutListProps As System.Integer, _
   ByVal OverrideTemplate As System.Boolean, _
   ByVal TemplatePath As System.String, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim Name As System.String
Dim Options As System.Integer
Dim CutListProps As System.Integer
Dim OverrideTemplate As System.Boolean
Dim TemplatePath As System.String
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean
 
value = instance.SaveToFile3(Name, Options, CutListProps, OverrideTemplate, TemplatePath, Errors, Warnings)
```

```

System.bool SaveToFile3( 
   System.string Name,
   System.int Options,
   System.int CutListProps,
   System.bool OverrideTemplate,
   System.string TemplatePath,
   out System.int Errors,
   out System.int Warnings
)
```

```

System.bool SaveToFile3( 
   System.String^ Name,
   System.int Options,
   System.int CutListProps,
   System.bool OverrideTemplate,
   System.String^ TemplatePath,
   [Out] System.int Errors,
   [Out] System.int Warnings
) 
```

#### Parameters

*Name*
:   Path and name of the part document to which to save the selected weldment member, solid body, or surface body

*Options*
:   How to save the document as defined in [swSaveAsOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsOptions_e.html)

*CutListProps*
:   Option for transferring the cut list of the selected weldment member, solid body, or surface body to the new part as defined in [swCutListTransferOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCutListTransferOptions_e.html)

*OverrideTemplate*
:   True to override the part template with the template specified by TemplatePath, false to not

*TemplatePath*
:   Path to part template; valid only if OverrideTemplate is true

*Errors*
:   Save errors as defined in [swFileSaveError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html)

*Warnings*
:   Warnings or extra information generated during the save operation as defined in [swFileSaveWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html)

#### Return Value

True if the save is successful, false if not

Remarks

The difference between this method and the now obsolete IPartDoc::SaveToFile2 is that this method allows you to specify in CutListProps how the cut list properties of the selected weldment member of a weldment part are transferred to the saved part.

Before calling this method, select a weldment member, surface body, or solid body in the FeatureManager design tree.

Example

[Save Solid Body to File (VBA)](Save_Solid_Body_to_File_Example_VB.htm)  
[Save Solid Body to File (VB.NET)](Save_Solid_Body_to_File_Example_VBNET.htm)  
[Save Solid Body to File (C#)](Save_Solid_Body_to_File_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
