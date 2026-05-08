# GetFontInfo Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetFontInfo`

Gets with the note's font information.
Gets with the note's font information.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFontInfo() As System.Object
```

```

Dim instance As INote
Dim value As System.Object
 
value = instance.GetFontInfo()
```

```

System.object GetFontInfo()
```

```

System.Object^ GetFontInfo(); 
```

#### Return Value

Array of doubles containing the font information (see **Remarks**)

Remarks

Currently this method returns only a line type index. See [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) for line type index information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::IGetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetFontInfo.md)  
[INote::HasMultipleFonts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasMultipleFonts.md)  
[INote::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.md)
