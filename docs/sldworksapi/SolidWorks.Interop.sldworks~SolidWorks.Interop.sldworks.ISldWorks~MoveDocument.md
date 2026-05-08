# MoveDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~MoveDocument`

Moves a document and optionally updates references to it.
Moves a document and optionally updates references to it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MoveDocument( _
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
 
value = instance.MoveDocument(SourceDoc, DestDoc, FromChildren, ToChildren, Option)
```

```

System.int MoveDocument( 
   System.string SourceDoc,
   System.string DestDoc,
   System.object FromChildren,
   System.object ToChildren,
   System.int Option
)
```

```

System.int MoveDocument( 
   System.String^ SourceDoc,
   System.String^ DestDoc,
   System.Object^ FromChildren,
   System.Object^ ToChildren,
   System.int Option
) 
```

#### Parameters

*SourceDoc*
:   Full path and filename of the document to move

*DestDoc*
:   Full path and filename of the new document to which to move the document specified for SourceDoc

*FromChildren*
:   Array of strings containing the full path and filenames of the child documents dependent on the document specified for SourceDoc

*ToChildren*
:   Array of strings containing the new full path and filenames for the child documents to which to move the documents specified for FromChildren

*Option*
:   Move options as defined by [swMoveCopyOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyOptions_e.html)

#### Return Value

Success or error code as defined by [swMoveCopyError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveCopyError_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IMoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IMoveDocument.md)  
[ISldWorks::ICopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.md)  
[ISldWorks::CopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.md)
