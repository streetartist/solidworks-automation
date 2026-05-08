# ShowBatchSaveTo3DExperienceDlg Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBatchSaveTo3DExperienceDlg`

Opens a dialog to save files in the specified folder to 3DEXPERIENCE.
Opens a dialog to save files in the specified folder to 3DEXPERIENCE.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowBatchSaveTo3DExperienceDlg( _
   ByVal FolderPath As System.String, _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim FolderPath As System.String
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.ShowBatchSaveTo3DExperienceDlg(FolderPath, Options)
```

```

System.int ShowBatchSaveTo3DExperienceDlg( 
   System.string FolderPath,
   System.int Options
)
```

```

System.int ShowBatchSaveTo3DExperienceDlg( 
   System.String^ FolderPath,
   System.int Options
) 
```

#### Parameters

*FolderPath*
:   Path of files to save

*Options*
:   not used

#### Return Value

0 if successful, -1 if not

Remarks

This method is valid only for [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Call [ISldWorks::RunBatchSaveProcess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunBatchSaveProcess.md) after using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
