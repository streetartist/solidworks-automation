# GetFirstNote Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote`

Obsolete. Superseded by IView::GetFirstNote2.
Obsolete. Superseded by [IView::GetFirstNote2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstNote() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstNote()
```

```

System.object GetFirstNote()
```

```

System.Object^ GetFirstNote(); 
```

#### Return Value

First [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

The sheet must be visible. See [ISheet::SheetFormatVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetFirstNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstNote.md)  
[INote::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.md)  
[INote::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetNext.md)
