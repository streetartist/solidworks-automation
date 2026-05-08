# SetCurrentWorkingDirectory Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory`

Sets the current working directory to be used by SOLIDWORKS.
Sets the current working directory to be used by SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCurrentWorkingDirectory( _
   ByVal CurrentWorkingDirectory As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim CurrentWorkingDirectory As System.String
Dim value As System.Boolean
 
value = instance.SetCurrentWorkingDirectory(CurrentWorkingDirectory)
```

```

System.bool SetCurrentWorkingDirectory( 
   System.string CurrentWorkingDirectory
)
```

```

System.bool SetCurrentWorkingDirectory( 
   System.String^ CurrentWorkingDirectory
) 
```

#### Parameters

*CurrentWorkingDirectory*
:   Directory to set as the current working directory

#### Return Value

True if specified direction is set as the current working directory, false if not

Remarks

The current working directory is used when opening documents containing references. If explicit search folders are not set (see [ISldWorks::SetSearchFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSearchFolders.md)), then SOLIDWORKS will initially try to locate file references (for example, assembly component parts) in the current working directory. Interactively, the current working directory is used by the File Open dialog and is set when you choose the Open dialog button.

The [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) method does not set the current working directory. Therefore, you may want to set the current working directory using ISldWorks::SetCurrentWorkingDirectory before opening a file that contains references. By doing so, you will get the same behavior as if the file was opened interactively using the File Open dialog.

For more information on the search criteria used by SOLIDWORKS when loading file references, see SOLIDWORKS Help.

Example

[Open Document (VBA)](Open_Document_Example_VB.htm)  
[Open Document (VB.NET)](Open_Document_Example_VBNET.htm)  
[Open Document (C#)](Open_Document_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.md)  
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.md)  
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.md)  
[ISldWorks::GetExecutablePath Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExecutablePath.md)
