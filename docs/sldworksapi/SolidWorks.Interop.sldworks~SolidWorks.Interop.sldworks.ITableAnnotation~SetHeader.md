# SetHeader Method (ITableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetHeader`

Sets the header for this table.
Sets the header for this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetHeader( _
   ByVal Style As System.Integer, _
   ByVal Count As System.Integer _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Style As System.Integer
Dim Count As System.Integer
Dim value As System.Boolean
 
value = instance.SetHeader(Style, Count)
```

```

System.bool SetHeader( 
   System.int Style,
   System.int Count
)
```

```

System.bool SetHeader( 
   System.int Style,
   System.int Count
) 
```

#### Parameters

*Style*
:   Header style as defined in [swTableHeaderPosition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableHeaderPosition_e.html)

*Count*
:   Number of lines in the header

#### Return Value

True if header is set successfully, false if not

Remarks

Tables created internally by the SOLIDWORKS software, such as Hole Charts, Revision Blocks, and BOM tables, are created with a specific number of headers lines.

This method cannot:

- Change the number of lines in the header for these tables; thus, the Count argument is ignored.
- Turn off the header in these types of tables; thus, this method has no effect, and FALSE is returned.

Essentially, the only thing this method can do with these types of tables is to change the header between the top and the bottom.

If you are changing the header style and number of header lines in a single use of this method, the number of lines is considered before changing the header style. For example, if you are changing a table that had 1 header line at the top, by calling SetHeader (swTableHeader\_Bottom, 3), the first 3 lines in the table are moved to the bottom of the table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetHeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetHeaderCount.md)  
[ITableAnnotation::GetHeaderStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetHeaderStyle.md)
