# SetRowChanged Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SetRowChanged`

Sets the number of the row that was changed.
Sets the number of the row that was changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetRowChanged( _
   ByVal RowIndex As System.Integer _
) 
```

```

Dim instance As IDesignTable
Dim RowIndex As System.Integer
 
instance.SetRowChanged(RowIndex)
```

```

void SetRowChanged( 
   System.int RowIndex
)
```

```

void SetRowChanged( 
   System.int RowIndex
) 
```

#### Parameters

*RowIndex*
:   Number of row that changed

Remarks

Setting the number of the row that changed provides significant performance gains for products like CD Catalog Viewer, a component of 3D PartStream.NET.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::AddRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~AddRow.md)  
[IDesignTable::GetRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetRowCount.md)  
[IDesignTable::GetStartRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetStartRowNumber.md)  
[IDesignTable::GetTotalRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTotalRowCount.md)  
[IDesignTable::GetVisibleRowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleRowCount.md)  
[IDesignTable::GetVisibleTopRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetVisibleTopRowNumber.md)  
[IDesignTable::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~RowHidden.md)
