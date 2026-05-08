# FileName Property (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName`

Gets or sets the Microsoft Excel file for this design table.
Gets or sets the Microsoft Excel file for this design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FileName As System.String
```

```

Dim instance As IDesignTable
Dim value As System.String
 
instance.FileName = value
 
value = instance.FileName
```

```

System.string FileName {get; set;}
```

```

property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Full path and filename for the Microsoft Excel file

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::SaveAsExcelFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile.md)  
[IDesignTable::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~LinkToFile.md)  
[IDesignTable::SourceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.md)
