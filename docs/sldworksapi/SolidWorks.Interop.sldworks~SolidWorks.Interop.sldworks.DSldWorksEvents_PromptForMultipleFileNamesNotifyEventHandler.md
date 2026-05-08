# DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler`

Fired when any dependent documents are missing from the file being opened.
Fired when any dependent documents are missing from the file being opened.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler( _
   ByVal openOrSave As System.Integer, _
   ByRef suggestedFileNames As System.Object, _
   ByRef DocTypes As System.Object, _
   ByVal cause As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler( 
   System.int openOrSave,
   ref System.object suggestedFileNames,
   ref System.object DocTypes,
   System.int cause
)
```

```

public delegate System.int DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler( 
   System.int openOrSave,
   System.Object^% suggestedFileNames,
   System.Object^% DocTypes,
   System.int cause
)
```

#### Parameters

*openOrSave*
:   - 0 = save
    - 1 = open

*suggestedFileNames*
:   Array of names of the missing SOLIDWORKS documents

*DocTypes*
:   Types of the missing documents as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*cause*
:   Cause as defined in [swPrompForFilenameCause\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrompForFilenameCause_e.html)

Remarks

Use this event with the [ISldWorks::SetMultipleFilenamesPrompt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMultipleFilenamesPrompt.md) method.

If developing a C++ application, use [swAppPromptForMultipleFileNameNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_PromptForMultipleFileNamesNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
