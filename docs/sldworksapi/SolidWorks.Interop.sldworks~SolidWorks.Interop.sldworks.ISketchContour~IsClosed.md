# IsClosed Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IsClosed`

Gets whether this sketch contour is open or closed.
Gets whether this sketch contour is open or closed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsClosed() As System.Boolean
```

```

Dim instance As ISketchContour
Dim value As System.Boolean
 
value = instance.IsClosed()
```

```

System.bool IsClosed()
```

```

System.bool IsClosed(); 
```

#### Return Value

True if the sketch contour is open, false if closed

Remarks

This method works even if the sketch is suppressed.

Example

[Get Sketch Contours (VBA)](Get_Sketch_Contours_Example_VB.htm)  
[Create Extrude Feature Using Sketch Contours (C#)](Create_Extrude_Feature_Using_Sketch_Contours_Example_CSharp.htm)  
[Create Extrude Feature Using Sketch Contours (VB.NET)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VBNET.htm)  
[Create Extrude Feature Using Sketch Contours (VBA)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)  
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.md)
