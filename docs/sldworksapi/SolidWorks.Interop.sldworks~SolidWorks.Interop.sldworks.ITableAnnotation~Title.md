# Title Property (ITableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Title`

Gets or sets the title for this table.
Gets or sets the title for this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Title As System.String
```

```

Dim instance As ITableAnnotation
Dim value As System.String
 
instance.Title = value
 
value = instance.Title
```

```

System.string Title {get; set;}
```

```

property System.String^ Title {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Text for title of table

Remarks

You can set the title of the table even if the title is not currently visible. See [ITableAnnotation::TitleVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TitleVisible.md) for details.

Example

[Get Components for Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)  
[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)  
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)  
[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)
