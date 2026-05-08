# SaveAsExcel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SaveAsExcel`

Saves this BOM table annotation as a Microsoft Excel document with the specified properties.
Saves this BOM table annotation as a Microsoft Excel document with the specified properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveAsExcel( _
   ByVal FileName As System.String, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal IncludeFileImages As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBomTableAnnotation
Dim FileName As System.String
Dim IncludeHidden As System.Boolean
Dim IncludeFileImages As System.Boolean
Dim value As System.Boolean
 
value = instance.SaveAsExcel(FileName, IncludeHidden, IncludeFileImages)
```

```

System.bool SaveAsExcel( 
   System.string FileName,
   System.bool IncludeHidden,
   System.bool IncludeFileImages
)
```

```

System.bool SaveAsExcel( 
   System.String^ FileName,
   System.bool IncludeHidden,
   System.bool IncludeFileImages
) 
```

#### Parameters

*FileName*
:   Full path and file name of the Microsoft Excel file to save to (**\*.xls**)

*IncludeHidden*
:   True to include text in hidden cells, false to not

*IncludeFileImages*
:   True to include file images, false to not

#### Return Value

True if the table is saved as a Microsoft Excel file, false if not

Example

[Save Table to Microsoft Excel (VBA)](Save_Table_to_Microsoft_Excel_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)
