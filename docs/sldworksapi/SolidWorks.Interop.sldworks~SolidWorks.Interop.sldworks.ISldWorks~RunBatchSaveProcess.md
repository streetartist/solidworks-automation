# RunBatchSaveProcess Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunBatchSaveProcess`

Batch saves files to 3DEXPERIENCE.
Batch saves files to 3DEXPERIENCE.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RunBatchSaveProcess() As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
value = instance.RunBatchSaveProcess()
```

```

System.bool RunBatchSaveProcess()
```

```

System.bool RunBatchSaveProcess(); 
```

#### Return Value

True if batch save successful, false if not

Remarks

This method is valid only for [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Call this method:

- after loading the files to save using [ISldWorks::ShowBatchSaveTo3DExperienceDlg](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBatchSaveTo3DExperienceDlg.md).
- before calling [ISldWorks::GetBatchUploadedFilesInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBatchUploadedFilesInfo.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
