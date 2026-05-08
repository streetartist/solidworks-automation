# IGetMagneticLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetMagneticLines`

Gets the magnetic lines on this drawing sheet.
Gets the magnetic lines on this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMagneticLines( _
   ByVal Count As System.Integer _
) As MagneticLine
```

```

Dim instance As ISheet
Dim Count As System.Integer
Dim value As MagneticLine
 
value = instance.IGetMagneticLines(Count)
```

```

MagneticLine IGetMagneticLines( 
   System.int Count
)
```

```

MagneticLine^ IGetMagneticLines( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of magnetic lines returned by this method

#### Return Value

- In-process, unmanaged C++: Array of [IMagneticLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.md)s

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Example

Before calling this method, call [ISheet::GetMagneticLinesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLinesCount.md) to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLines.md)  
[ISheet::InsertMagneticLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertMagneticLine.md)
