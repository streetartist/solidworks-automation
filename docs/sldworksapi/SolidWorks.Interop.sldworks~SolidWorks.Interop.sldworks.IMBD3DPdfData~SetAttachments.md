# SetAttachments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetAttachments`

Sets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF.
Sets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetAttachments( _
   ByVal Values As System.Object _
) 
```

```

Dim instance As IMBD3DPdfData
Dim Values As System.Object
 
instance.SetAttachments(Values)
```

```

void SetAttachments( 
   System.object Values
)
```

```

void SetAttachments( 
   System.Object^ Values
) 
```

#### Parameters

*Values*
:   Array of strings of the fully qualified paths of the files to include as attachments

Example

[Attach Files to MBD 3D PDF (C#)](Attach_Files_to_MBD_3D_PDF_Example_CSharp.htm)  
[Attach Files to MBD 3D PDF (VB.NET)](Attach_Files_to_MBD_3D_PDF_Example_VBNET.htm)  
[Attach Files to MBD 3D PDF (VBA)](Attach_Files_to_MBD_3D_PDF_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)  
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.md)  
[IMBD3DPdfData::GetAttachments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetAttachments.md)
