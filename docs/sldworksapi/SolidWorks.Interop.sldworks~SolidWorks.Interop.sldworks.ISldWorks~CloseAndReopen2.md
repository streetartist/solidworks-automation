# CloseAndReopen2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen2`

Closes and reopens the specified drawing document without unloading its references from memory.
Closes and reopens the specified drawing document without unloading its references from memory.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CloseAndReopen2( _
   ByVal Doc As System.Object, _
   ByVal Option As System.Integer, _
   ByRef NewDoc As System.Object _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Doc As System.Object
Dim Option As System.Integer
Dim NewDoc As System.Object
Dim value As System.Integer
 
value = instance.CloseAndReopen2(Doc, Option, NewDoc)
```

```

System.int CloseAndReopen2( 
   System.object Doc,
   System.int Option,
   out System.object NewDoc
)
```

```

System.int CloseAndReopen2( 
   System.Object^ Doc,
   System.int Option,
   [Out] System.Object^ NewDoc
) 
```

#### Parameters

*Doc*
:   [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md); drawing document to close and reopen

*Option*
:   Reopen options as defined in [swCloseReopenOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCloseReopenOption_e.html)

*NewDoc*
:   [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md); reopened drawing document

#### Return Value

Error code as defined in [swCloseReopenError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCloseReopenError_e.html)

Remarks

Before a third-party application can process a drawing document that is open in SOLIDWORKS, it must close the document. Usually when a drawing document is closed, its references are unloaded from memory, and reopening the drawing document takes a lot of time. This method closes a drawing document, keeps its references in memory, and quickly reopens it.

After the drawing document is closed and before it is reopened, SOLIDWORKS fires a [FileCloseNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileCloseNotifyEventHandler.md) event with reason [swFileCloseNotifyReason\_e.swFileCloseNotifyReason\_CloseForReload](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileCloseNotifyReason_e.html). In the handler of this event, a third-party application can call [ISldWorks::SetPromptFileName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename2.md) to open a different file, or it can process the specified document before it is reopened in SOLIDWORKS.

See [IModelDoc2::ReloadOrReplace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReloadOrReplace.md) to perform a similar function with part and assembly documents.

Example

Contact SOLIDWORKS API Support to obtain **Close and Reopen a Drawing Document (VBA, VB.NET, C#)**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CloseAllDocuments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.md)  
[ISldWorks::CloseDoc Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md)  
[ISldWorks::QuitDoc Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.md)
