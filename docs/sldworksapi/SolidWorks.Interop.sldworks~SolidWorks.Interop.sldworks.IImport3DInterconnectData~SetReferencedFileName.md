# SetReferencedFileName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~SetReferencedFileName`

Sets the full path name of the proprietary, non-native CAD file.
Sets the full path name of the proprietary, non-native CAD file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetReferencedFileName( _
   ByVal FileName As System.String _
) 
```

```

Dim instance As IImport3DInterconnectData
Dim FileName As System.String
 
instance.SetReferencedFileName(FileName)
```

```

void SetReferencedFileName( 
   System.string FileName
)
```

```

void SetReferencedFileName( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Full path name of the linked non-native CAD file

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md)  
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.md)  
[IImport3DinterconnectData::GetReferencedFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~GetReferencedFileName.md)
