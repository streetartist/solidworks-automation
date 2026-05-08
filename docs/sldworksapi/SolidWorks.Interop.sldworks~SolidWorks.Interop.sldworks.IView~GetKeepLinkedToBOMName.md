# GetKeepLinkedToBOMName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName`

Gets the name of the BOM or weldment cut-list table feature to which this drawing view is linked.
Gets the name of the BOM or weldment cut-list table feature to which this drawing view is linked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetKeepLinkedToBOMName() As System.String
```

```

Dim instance As IView
Dim value As System.String
 
value = instance.GetKeepLinkedToBOMName()
```

```

System.string GetKeepLinkedToBOMName()
```

```

System.String^ GetKeepLinkedToBOMName(); 
```

#### Return Value

Name of BOM or weldment cut-list table feature

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBomTable.md)  
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.md)  
[IView::IGetBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBomTable.md)  
[IView::IInsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.md)  
[IView::InsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.md)  
[IView::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.md)  
[IView::InsertWeldmentTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertWeldmentTable.md)  
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.md)
