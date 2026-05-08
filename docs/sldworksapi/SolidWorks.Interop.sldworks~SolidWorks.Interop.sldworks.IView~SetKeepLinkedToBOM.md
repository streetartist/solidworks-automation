# SetKeepLinkedToBOM Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM`

Sets whether this drawing view is linked to the specified BOM or weldment cut-list table.
Sets whether this drawing view is linked to the specified BOM or weldment cut-list table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetKeepLinkedToBOM( _
   ByVal Linked As System.Boolean, _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IView
Dim Linked As System.Boolean
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.SetKeepLinkedToBOM(Linked, Name)
```

```

System.bool SetKeepLinkedToBOM( 
   System.bool Linked,
   System.string Name
)
```

```

System.bool SetKeepLinkedToBOM( 
   System.bool Linked,
   System.String^ Name
) 
```

#### Parameters

*Linked*
:   True to set a drawing view to the specified BOM or weldment cut-list table, false to not

*Name*
:   Name of the BOM or weldment cut-list table to which to link this drawing view

#### Return Value

True if the BOM or weldment cut-list table is linked to this drawing view, false if not

Remarks

This method returns false if the string specified for Name does not correspond to the name of a BOM or weldment cut-list table feature created for the model in this drawing view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.md)  
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.md)  
[IView::IInsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.md)  
[IView::InsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.md)  
[IView::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.md)  
[IView::InsertWeldmentTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertWeldmentTable.md)
