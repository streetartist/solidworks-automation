# DSldWorksEvents_PromptForFilenameNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler`

Fired when a dependent document is missing from the file being opened.
Fired when a dependent document is missing from the file being opened.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_PromptForFilenameNotifyEventHandler( _
   ByVal openOrSave As System.Integer, _
   ByVal suggestedFileName As System.String, _
   ByVal DocType As System.Integer, _
   ByVal cause As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_PromptForFilenameNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_PromptForFilenameNotifyEventHandler( 
   System.int openOrSave,
   System.string suggestedFileName,
   System.int DocType,
   System.int cause
)
```

```

public delegate System.int DSldWorksEvents_PromptForFilenameNotifyEventHandler( 
   System.int openOrSave,
   System.String^ suggestedFileName,
   System.int DocType,
   System.int cause
)
```

#### Parameters

*openOrSave*
:   - 0 = save
    - 1 = open

*suggestedFileName*
:   Name of the missing SOLIDWORKS document

*DocType*
:   Type of the missing document as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*cause*
:   Cause as defined in [swPrompForFilenameCause\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrompForFilenameCause_e.html)

Remarks

Use this event with the [ISldWorks::SetPromptFilename2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename2.md) method, not with the [ISldWorks::SetMissingReferencePathName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMissingReferencePathName.md) method.

An example of a good use for this event is when you are mirroring an assembly. If you want to create new files for the mirrored components, use this notification to specify the new filename. This is useful when you want to choose filenames for the newly created components during the mirroring process.

If developing a C++ application, use [swAppPromptForFileNameNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_PromptForFilenameNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
