# SaveToFile2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SaveToFile2`

Obsolete. Superseded by IPartDoc::SaveToFile3.
Obsolete. Superseded by [IPartDoc::SaveToFile3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SaveToFile3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveToFile2( _
   ByVal Name As System.String, _
   ByVal Options As System.Integer, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim Name As System.String
Dim Options As System.Integer
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean
 
value = instance.SaveToFile2(Name, Options, Errors, Warnings)
```

```

System.bool SaveToFile2( 
   System.string Name,
   System.int Options,
   out System.int Errors,
   out System.int Warnings
)
```

```

System.bool SaveToFile2( 
   System.String^ Name,
   System.int Options,
   [Out] System.int Errors,
   [Out] System.int Warnings
) 
```

#### Parameters

*Name*
:   Name of the part document (.sldprt)

*Options*
:   Relevant options indicating how to save the document as defined in [swSaveAsOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsOptions_e.html)

*Errors*
:   Errors that caused the save to fail as defined in [swFileSaveError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html)

*Warnings*
:   Warnings or extra information generated during the save operation as defined in [swFileSaveWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html)

#### Return Value

True if the save is successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
