# SetPromptFilename2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename2`

Sets the file to open in response to a SOLIDWORKS event.
Sets the file to open in response to a SOLIDWORKS event.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetPromptFilename2( _
   ByVal FileName As System.String, _
   ByVal ConfigName As System.String _
) 
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim ConfigName As System.String
 
instance.SetPromptFilename2(FileName, ConfigName)
```

```

void SetPromptFilename2( 
   System.string FileName,
   System.string ConfigName
)
```

```

void SetPromptFilename2( 
   System.String^ FileName,
   System.String^ ConfigName
) 
```

#### Parameters

*FileName*
:   Full pathname of file to open

*ConfigName*
:   Configuration name of file to open

Remarks

FileName is used only:

|  |  |
| --- | --- |
| **When the handler of this event...** | **Returns...** |
| [FileCloseNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileCloseNotifyEventHandler.md) | non-0 value |
| [PromptForFileNameNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.md) | non-0 value |
| [ReferencedFilePreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotifyEventHandler.md) | non-0 value |

Because the filename specified is used only when [PromptForFileNameNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.md) and [ReferencedFilePreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotifyEventHandler.md) return S\_FALSE, you cannot specify an initial filename for SOLIDWORKS to use in the standard dialog. Instead, you must provide your own file dialog and return the filename after the user selects it.

Example

Contact SOLIDWORKS API Support to obtain **Close and Reopen a Drawing Document (VBA, VB.NET, C#)**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md)  
[ISldWorks::OpenDoc7 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md)  
[ISldWorks::SetMultipleFilenamesPrompt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMultipleFilenamesPrompt.md)  
[ISldWorks::SetNewFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetNewFilename.md)
