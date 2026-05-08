# GetBatchUploadedFilesInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBatchUploadedFilesInfo`

Gets the files uploaded to 3DEXPERIENCE during a batch process.
Gets the files uploaded to 3DEXPERIENCE during a batch process.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBatchUploadedFilesInfo( _
   ByRef ProcessedFileNames As System.Object, _
   ByRef NonProcessedFileNames As System.Object, _
   ByRef FailedFileNames As System.Object _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim ProcessedFileNames As System.Object
Dim NonProcessedFileNames As System.Object
Dim FailedFileNames As System.Object
Dim value As System.Boolean
 
value = instance.GetBatchUploadedFilesInfo(ProcessedFileNames, NonProcessedFileNames, FailedFileNames)
```

```

System.bool GetBatchUploadedFilesInfo( 
   out System.object ProcessedFileNames,
   out System.object NonProcessedFileNames,
   out System.object FailedFileNames
)
```

```

System.bool GetBatchUploadedFilesInfo( 
   [Out] System.Object^ ProcessedFileNames,
   [Out] System.Object^ NonProcessedFileNames,
   [Out] System.Object^ FailedFileNames
) 
```

#### Parameters

*ProcessedFileNames*
:   Array of processed file names

*NonProcessedFileNames*
:   Array of unprocessed file names

*FailedFileNames*
:   Array of file names that failed to upload

#### Return Value

True if retrieval successful, false if not

Remarks

This method is valid only for [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Before using this method, call [ISldWorks::RunBatchSaveProcess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunBatchSaveProcess.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
