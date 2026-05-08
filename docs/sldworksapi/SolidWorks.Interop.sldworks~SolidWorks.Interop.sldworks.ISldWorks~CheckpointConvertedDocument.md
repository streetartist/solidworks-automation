# CheckpointConvertedDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CheckpointConvertedDocument`

Saves the specified open document if its version is older than the version of the SOLIDWORKS product being used.
Saves the specified open document if its version is older than the version of the SOLIDWORKS product being used.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CheckpointConvertedDocument( _
   ByVal DocName As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim DocName As System.String
Dim value As System.Integer
 
value = instance.CheckpointConvertedDocument(DocName)
```

```

System.int CheckpointConvertedDocument( 
   System.string DocName
)
```

```

System.int CheckpointConvertedDocument( 
   System.String^ DocName
) 
```

#### Parameters

*DocName*
:   Full pathname of the file to save

#### Return Value

0 for no error or a bitwise OR of the errors encountered as defined in [swFileSaveError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html)

Remarks

This saves the document even if the document is read-only.

This method requires that the document is currently open in your SOLIDWORKS session. It specifically checks if the document has been upgraded to the current version of the SOLIDWORKS product in this session. If it has not, then this method has no effect.

Be careful when using this method because this method attempts to change the file permissions to read-write if the file is read-only, and if successful , it overwrites the file and restores the permission to read-only. Although it may appear the file is safe because it is read-only before and after the operation, it might have been overwritten by this method.

This method was designed to be used with the ISldWorks event [DocumentConversionNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentConversionNotifyEventHandler.md). It does not require that the notification be used, but it should work in response to that notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
