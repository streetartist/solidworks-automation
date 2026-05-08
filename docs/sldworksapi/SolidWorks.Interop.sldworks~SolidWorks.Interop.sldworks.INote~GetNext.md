# GetNext Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext`

Gets the next note in drawing view.
Gets the next note in [drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNext() As System.Object
```

```

Dim instance As INote
Dim value As System.Object
 
value = instance.GetNext()
```

```

System.object GetNext()
```

```

System.Object^ GetNext(); 
```

#### Return Value

Next [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

The sheet must be visible. See [ISheet::SheetFormatVisible.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md)

Example

[Change Note Text (VBA)](Change_Note_Text_Example_VB.htm)  
[Get All Notes in Drawing Template (VBA)](Get_All_Notes_in_Drawing_Template_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetNext.md)  
[IView::GetFirstNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote.md)  
[IView::IGetFirstNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstNote.md)
