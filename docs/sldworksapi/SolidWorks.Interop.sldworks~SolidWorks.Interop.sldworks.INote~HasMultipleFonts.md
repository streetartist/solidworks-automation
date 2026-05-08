# HasMultipleFonts Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasMultipleFonts`

Gets whether a note contains multiple fonts.
Gets whether a note contains multiple fonts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property HasMultipleFonts As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
value = instance.HasMultipleFonts
```

```

System.bool HasMultipleFonts {get;}
```

```

property System.bool HasMultipleFonts {
   System.bool get();
}
```

#### Property Value

True if the note contains multiple fonts, false if not

Example

[Get Whether Note Contains Rich Embedded Text (VBA)](Get_Whether_Note_Contains_Rich-embedded_Text_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetFontInfo.md)  
[INote::IGetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetFontInfo.md)  
[INote::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.md)
