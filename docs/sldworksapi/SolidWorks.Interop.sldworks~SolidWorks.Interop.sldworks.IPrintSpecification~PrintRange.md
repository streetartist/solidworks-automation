# PrintRange Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintRange`

Gets or sets the range of pages to print.
Gets or sets the range of pages to print.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrintRange As System.Object
```

```

Dim instance As IPrintSpecification
Dim value As System.Object
 
instance.PrintRange = value
 
value = instance.PrintRange
```

```

System.object PrintRange {get; set;}
```

```

property System.Object^ PrintRange {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of first and last page numbers of a range to print (see **Remarks**)

Remarks

The array can contain multiple pairs of integers, each pair indicating the start and end pages of a range of pages to print. For example, to print sheets 1, 2, 3, 6, and 7 of a drawing, this array contains 2 pairs of page numbers { 1, 3, 6, 7 } indicating to print pages 1-3 and 6-7. To print only page 6, this array is { 6, 6 }.

Instead of calling this method to set the print ranges, call [IPrintSpecification::AddPrintRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~AddPrintRange.md) for each range of pages you want to print.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)  
[IPrintSpecification::ResetPrintRange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ResetPrintRange.md)
