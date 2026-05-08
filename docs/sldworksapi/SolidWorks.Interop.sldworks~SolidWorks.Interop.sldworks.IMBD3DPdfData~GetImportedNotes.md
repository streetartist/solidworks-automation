# GetImportedNotes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetImportedNotes`

Gets the imported note names from the theme of this MBD3DPdfData.
Gets the imported note names from the theme of this MBD3DPdfData.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetImportedNotes() As System.Object
```

```

Dim instance As IMBD3DPdfData
Dim value As System.Object
 
value = instance.GetImportedNotes()
```

```

System.object GetImportedNotes()
```

```

System.Object^ GetImportedNotes(); 
```

#### Return Value

Array of imported note names

Remarks

Before calling this method, you need to use [IMBD3DPdfData::ThemeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) to set the theme of this MBD3DPdfData.

Example

See the [IMBD3DPdfData::SetImportedNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetImportedNote.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)  
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.md)
