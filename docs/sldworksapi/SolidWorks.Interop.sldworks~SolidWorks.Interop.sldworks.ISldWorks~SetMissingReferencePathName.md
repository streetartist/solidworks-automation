# SetMissingReferencePathName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMissingReferencePathName`

Sets the missing reference file name. Use with the SOLIDWORKS event ReferenceNotFoundNotify.
Sets the missing reference file name. Use with the SOLIDWORKS event [ReferenceNotFoundNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferenceNotFoundNotifyEventHandler.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetMissingReferencePathName( _
   ByVal FileName As System.String _
) 
```

```

Dim instance As ISldWorks
Dim FileName As System.String
 
instance.SetMissingReferencePathName(FileName)
```

```

void SetMissingReferencePathName( 
   System.string FileName
)
```

```

void SetMissingReferencePathName( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and filename of the missing reference

Remarks

Use with the SOLIDWORKS event [ReferenceNotFoundNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferenceNotFoundNotifyEventHandler.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
