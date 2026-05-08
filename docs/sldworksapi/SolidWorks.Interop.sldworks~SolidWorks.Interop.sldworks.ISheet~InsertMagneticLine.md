# InsertMagneticLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertMagneticLine`

Inserts a magnetic line at the specified start and end points on this drawing sheet.
Inserts a magnetic line at the specified start and end points on this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMagneticLine( _
   ByVal StartPoint As MathPoint, _
   ByVal EndPoint As MathPoint _
) As MagneticLine
```

```

Dim instance As ISheet
Dim StartPoint As MathPoint
Dim EndPoint As MathPoint
Dim value As MagneticLine
 
value = instance.InsertMagneticLine(StartPoint, EndPoint)
```

```

MagneticLine InsertMagneticLine( 
   MathPoint StartPoint,
   MathPoint EndPoint
)
```

```

MagneticLine^ InsertMagneticLine( 
   MathPoint^ StartPoint,
   MathPoint^ EndPoint
) 
```

#### Parameters

*StartPoint*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

*EndPoint*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

#### Return Value

[IMagneticLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.md)

Example

[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)  
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)  
[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLines.md)  
[ISheet::GetMagneticLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLinesCount.md)  
[ISheet::IGetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetMagneticLines.md)
