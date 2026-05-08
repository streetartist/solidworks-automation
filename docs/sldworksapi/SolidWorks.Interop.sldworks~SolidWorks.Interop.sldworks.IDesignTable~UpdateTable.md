# UpdateTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable`

Applies the changes made to the design table to the model.
Applies the changes made to the design table to the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateTable( _
   ByVal Type As System.Integer, _
   ByVal Close As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDesignTable
Dim Type As System.Integer
Dim Close As System.Boolean
Dim value As System.Boolean
 
value = instance.UpdateTable(Type, Close)
```

```

System.bool UpdateTable( 
   System.int Type,
   System.bool Close
)
```

```

System.bool UpdateTable( 
   System.int Type,
   System.bool Close
) 
```

#### Parameters

*Type*
:   Type of update as defined in [swDesignTableUpdateOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDesignTableUpdateOptions_e.html)

*Close*
:   True to close the design table, false to not

#### Return Value

True if the changes made to the design table update the model, false if not

Remarks

[IDesignTable::UpdateModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.md) is a simplified version of this method.

Example

[Add Row to Design Table (VBA)](Add_Row_to_Design_Table_Example_VB.htm)  
[Disable Cell Drop-down Lists in Design Table (C#)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_CSharp.htm)  
[Disable Cell Drop-down Lists in Design Table (VB.NET)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VBNET.htm)  
[Disable Cell Drop-down Lists in Design Table (VBA)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::EditFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.md)  
[IDesignTable::EditTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.md)  
[IDesignTable::IsActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~IsActive.md)  
[IDesignTable::UpdateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.md)  
[IDesignTable::UpdateModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.md)  
[IDesignTable::Warn Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Warn.md)
