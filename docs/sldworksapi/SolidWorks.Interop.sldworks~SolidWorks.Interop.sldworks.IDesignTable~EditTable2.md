# EditTable2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2`

Lets you edit the design table.
Lets you edit the design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditTable2( _
   ByVal NewWindow As System.Boolean _
) As System.Object
```

```

Dim instance As IDesignTable
Dim NewWindow As System.Boolean
Dim value As System.Object
 
value = instance.EditTable2(NewWindow)
```

```

System.object EditTable2( 
   System.bool NewWindow
)
```

```

System.Object^ EditTable2( 
   System.bool NewWindow
) 
```

#### Parameters

*NewWindow*
:   True to edit the design table in a separate window, false to not

#### Return Value

Microsoft Excel worksheet for this design table

Remarks

Do not use this method and [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md) in the same macro. Using IDesignTable::EditTable2 is preferable because it returns a pointer to the Microsoft Excel worksheet being operated on.

To avoid problems with zooming, set bNewWindow to True.

You can change the parameter values in the cells, add rows for additional configurations, or add columns to control additional parameters.

If the return value of this method is assigned to a variable, then it must be released before closing the design table with [IDesignTable::UpdateTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable.md)(type, True).

Example

[Disable Cell Drop-down Lists in Design Table (C#)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_CSharp.htm)  
[Disable Cell Drop-down Lists in Design Table (VB.NET)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VBNET.htm)  
[Disable Cell Drop-down Lists in Design Table (VBA)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::IsActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~IsActive.md)  
[IDesignTable::Updatable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Updatable.md)  
[IDesignTable::UpdateModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateModel.md)  
[IDesignTable::UpdateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.md)
