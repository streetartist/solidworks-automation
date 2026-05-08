# IGetNext Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetNext`

Gets the next note in drawing view.
Gets the next note in [drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNext() As Note
```

```

Dim instance As INote
Dim value As Note
 
value = instance.IGetNext()
```

```

Note IGetNext()
```

```

Note^ IGetNext(); 
```

#### Return Value

Next [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

The sheet must be visible. See [ISheet::SheetFormatVisible.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.md)
