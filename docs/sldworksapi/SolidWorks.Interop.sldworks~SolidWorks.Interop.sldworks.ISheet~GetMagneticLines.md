# GetMagneticLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLines`

Gets the magnetic lines on this drawing sheet.
Gets the magnetic lines on this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMagneticLines() As System.Object
```

```

Dim instance As ISheet
Dim value As System.Object
 
value = instance.GetMagneticLines()
```

```

System.object GetMagneticLines()
```

```

System.Object^ GetMagneticLines(); 
```

#### Return Value

Array of [IMagneticLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.md)s

Remarks

Call [ISheet::GetMagneticLinesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLinesCount.md) to get the number of magnetic lines returned by this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::IGetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetMagneticLines.md)  
[ISheet::InsertMagneticLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertMagneticLine.md)
