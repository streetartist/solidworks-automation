# GetBomTable Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBomTable`

Gets the BOM table found in this drawing view.
Gets the BOM table found in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBomTable() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetBomTable()
```

```

System.object GetBomTable()
```

```

System.Object^ GetBomTable(); 
```

#### Return Value

[BOM table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)

Remarks

This method only returns a BOM table if there is a Microsoft Excel-based BOM for the drawing view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::InsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.md)  
[IView::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.md)  
[IView::IGetBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBomTable.md)  
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.md)  
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.md)  
[IView::IInsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.md)
