# Worksheet Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Worksheet`

Gets the Microsoft Excel worksheet for this design table.
Gets the Microsoft Excel worksheet for this design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Worksheet As System.Object
```

```

Dim instance As IDesignTable
Dim value As System.Object
 
value = instance.Worksheet
```

```

System.object Worksheet {get;}
```

```

property System.Object^ Worksheet {
   System.Object^ get();
}
```

#### Property Value

Microsoft Excel worksheet for this design table

Remarks

Before you can call this method, you must call [IDesignTable::Attach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Attach.md).

Example

[Get Microsoft Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.md)  
[IDesignTable::SaveAsExcelFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile.md)  
[IDesignTable::Detach Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Detach.md)  
[IDesignTable::SourceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.md)
