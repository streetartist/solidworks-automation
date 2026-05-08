# GetCoordinates Method (ISketchText)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetCoordinates`

Gets the position of this sketch text.
Gets the position of this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoordinates() As System.Object
```

```

Dim instance As ISketchText
Dim value As System.Object
 
value = instance.GetCoordinates()
```

```

System.object GetCoordinates()
```

```

System.Object^ GetCoordinates(); 
```

#### Return Value

Array of 3 double values, the x,y,z coordinate of the sketch text

Remarks

To set the position of this sketch text, use [ISketchText::SetCoordinates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetCoordinates.md).

Example

See the [ISketchText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)  
[ISketchText::IGetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetCoordinates.md)
