# SaveAsExcelFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SaveAsExcelFile`

Saves the design table to a Microsoft Excel file.
Saves the design table to a Microsoft Excel file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAsExcelFile( _
   ByVal Value As System.String _
) As System.Boolean
```

```

Dim instance As IDesignTable
Dim Value As System.String
Dim value As System.Boolean
 
value = instance.SaveAsExcelFile(Value)
```

```

System.bool SaveAsExcelFile( 
   System.string Value
)
```

```

System.bool SaveAsExcelFile( 
   System.String^ Value
) 
```

#### Parameters

*Value*
:   Path and filename for the Microsoft Excel file

#### Return Value

True if the design table is saved to a Microsoft Excel file, false if not

Example

[Save Design Table as Microsoft Excel File (VBA)](Save_Design_Table_as_Microsoft_Excel_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~FileName.md)  
[IDesignTable::SourceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~SourceType.md)
