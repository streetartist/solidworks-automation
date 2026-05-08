# SetNewFilename Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetNewFilename`

Sets the name of the new SOLIDWORKS file.
Sets the name of the new SOLIDWORKS file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetNewFilename( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SetNewFilename(FileName)
```

```

System.bool SetNewFilename( 
   System.string FileName
)
```

```

System.bool SetNewFilename( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name for new SOLIDWORKS file

#### Return Value

True if the name of the new SOLIDWORKS file is set, false if not

Remarks

Use with SldWorks [FileNewPreNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewPreNotifyEventHandler.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
