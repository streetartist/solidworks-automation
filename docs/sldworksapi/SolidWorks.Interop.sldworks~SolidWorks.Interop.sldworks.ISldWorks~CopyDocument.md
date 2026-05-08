# CopyDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument`

Copies a document and optionally updates references to it.
Copies a document and optionally updates references to it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CopyDocument( _
   ByVal SourceDoc As System.String, _
   ByVal DestDoc As System.String, _
   ByVal FromChildren As System.Object, _
   ByVal ToChildren As System.Object, _
   ByVal Option As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim SourceDoc As System.String
Dim DestDoc As System.String
Dim FromChildren As System.Object
Dim ToChildren As System.Object
Dim Option As System.Integer
Dim value As System.Integer
 
value = instance.CopyDocument(SourceDoc, DestDoc, FromChildren, ToChildren, Option)
```

```

System.int CopyDocument( 
   System.string SourceDoc,
   System.string DestDoc,
   System.object FromChildren,
   System.object ToChildren,
   System.int Option
)
```

```

System.int CopyDocument( 
   System.String^ SourceDoc,
   System.String^ DestDoc,
   System.Object^ FromChildren,
   System.Object^ ToChildren,
   System.int Option
) 
```

#### Parameters

*SourceDoc*
:   Full path and filename of the document to copy

*DestDoc*
:   Full path and filename of the document to which to copy SourceDoc

*FromChildren*
:   Array containing the full path and filenames of the child documents dependent on the document specified for SourceDoc

*ToChildren*
:   Array of strings containing the new full path and filenames of the child documents to which to copy the child documents specified for FromChildren

*Option*
:   Copy options as defined by [swMoveCopyOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyOptions_e.html)

#### Return Value

Success or error code as defined by [swMoveCopyError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyError_e.html)

Remarks

There can be no documents open when using this method.

Example

[Copy Document (VBA)](Copy_Document_Example_VB.htm)  
[Copy Document and Its Dependencies (VBA)](Copy_Document_and_Its_Dependencies_Example_VB.htm)  
[Copy Document and Its Dependencies (VB.NET)](Copy_Document_and_Its_Dependencies_Example_VBNET.htm)  
[Copy Document and Its Dependencies (C#)](Copy_Document_and_Its_Dependencies_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::MoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~MoveDocument.md)  
[ISldWorks::ICopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.md)  
[IModelDocExtension::SaveAs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md)
