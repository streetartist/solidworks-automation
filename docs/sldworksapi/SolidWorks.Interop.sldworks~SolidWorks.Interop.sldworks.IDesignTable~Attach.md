# Attach Method (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach`

Activates the design table within the part or assembly document.
Activates the design table within the part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Attach() As System.Boolean
```

```

Dim instance As IDesignTable
Dim value As System.Boolean
 
value = instance.Attach()
```

```

System.bool Attach()
```

```

System.bool Attach(); 
```

#### Return Value

True if the design table is successfully activated, false if not

Remarks

If you want SOLIDWORKS to run in the background, then do not use this method. Using this method will cause SOLIDWORKS to become visible.

Do not use this method and [IDesignTable::EditTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditTable2.md) in the same macro. Using IDesignTable::EditTable2 is preferable because it returns a pointer to the Microsoft Excel worksheet being operated on.

If you use IDesignTable::Attach, then you must call this method before calling any of the other IDesignTable methods. When your application is finished extracting data from the design table, use [IDesignTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md) to detach the IDesignTable object from the Microsoft Excel object.

Example

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)  
[Save Design Table as Microsoft Excel File (VBA)](Save_Design_Table_as_Microsoft_Excel_File_Example_VB.htm)  
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)  
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)  
[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)
