# IMoveDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IMoveDocument`

Moves a document and optionally updates references to it.
Moves a document and optionally updates references to it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMoveDocument( _
   ByVal SourceDoc As System.String, _
   ByVal DestDoc As System.String, _
   ByVal ChildCount As System.Integer, _
   ByRef FromChildren As System.String, _
   ByRef ToChildren As System.String, _
   ByVal Option As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim SourceDoc As System.String
Dim DestDoc As System.String
Dim ChildCount As System.Integer
Dim FromChildren As System.String
Dim ToChildren As System.String
Dim Option As System.Integer
Dim value As System.Integer
 
value = instance.IMoveDocument(SourceDoc, DestDoc, ChildCount, FromChildren, ToChildren, Option)
```

```

System.int IMoveDocument( 
   System.string SourceDoc,
   System.string DestDoc,
   System.int ChildCount,
   ref System.string FromChildren,
   ref System.string ToChildren,
   System.int Option
)
```

```

System.int IMoveDocument( 
   System.String^ SourceDoc,
   System.String^ DestDoc,
   System.int ChildCount,
   System.String^% FromChildren,
   System.String^% ToChildren,
   System.int Option
) 
```

#### Parameters

*SourceDoc*
:   Full path and filename of the document to move

*DestDoc*
:   Full path and filename of the new document to which to move the document specified for SourceDoc

*ChildCount*
:   Number of child documents for SourceDoc

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
[ISldWorks::MoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~MoveDocument.md)  
[ISldWorks::ICopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.md)  
[ISldWorks::CopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.md)
