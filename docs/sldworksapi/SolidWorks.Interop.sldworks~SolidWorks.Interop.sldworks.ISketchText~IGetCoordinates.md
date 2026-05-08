# IGetCoordinates Method (ISketchText)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetCoordinates`

Gets the position of this sketch text.
Gets the position of this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCoordinates() As System.Double
```

```

Dim instance As ISketchText
Dim value As System.Double
 
value = instance.IGetCoordinates()
```

```

System.double IGetCoordinates()
```

```

System.double IGetCoordinates(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 double values, the x,y,z coordinate of the sketch text

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To set the position of this sketch text, use [ISketchText::SetCoordinates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetCoordinates.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)  
[ISketchText::GetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetCoordinates.md)
