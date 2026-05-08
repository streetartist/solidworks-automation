# SetMultipleFilenamesPrompt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMultipleFilenamesPrompt`

Sets the new filenames to open in response to the ISldWorks PromptForMultipleFileNamesNotify event.
Sets the new filenames to open in response to the ISldWorks [PromptForMultipleFileNamesNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler.md) event.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetMultipleFilenamesPrompt( _
   ByVal FileName As System.Object _
) 
```

```

Dim instance As ISldWorks
Dim FileName As System.Object
 
instance.SetMultipleFilenamesPrompt(FileName)
```

```

void SetMultipleFilenamesPrompt( 
   System.object FileName
)
```

```

void SetMultipleFilenamesPrompt( 
   System.Object^ FileName
) 
```

#### Parameters

*FileName*
:   Array of filenames

Remarks

The filenames specified are only used if the SOLIDWORKS [PromptForMultipleFileNamesNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler.md) event returns S\_FALSE. This implies that you cannot specify initial filenames for SOLIDWORKS to use in the standard dialog. Instead, you must provide your own file dialog and return the filenames after the user selects them.

Guidelines for using this method when the cause argument of the SOLIDWORKS PromptForMultipleFileNamesNotify event is set to [swSaveVirtualComponentExternally](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrompForFilenameCause_e.html):

- Length of the Filename argument array must be equal to the length of the suggestedFileNames argument array passed into ISldWorks::SetMultipleFilenamesPrompt. If there is a mismatch, all virtual components will be saved internal to the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event .
- Supplying a full path and file name will save a virtual component external to the assembly using that path and file name.
- Supplying only a file name (i.e., no path) will save the virtual component internal to the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event .
- This method cannot be used to change the name of an internally saved virtual component.
- Supplying an empty string will save the virtual component external to the assembly and in the same folder as the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event.
- Supplying an invalid path and file name or insufficient access rights will save the virtual component internal to the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event.
- Insufficient access rights to the path and file name will save the virtual component internal to the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::SetNewFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetNewFilename.md)  
[ISldWorks::SetPromptFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename.md)
