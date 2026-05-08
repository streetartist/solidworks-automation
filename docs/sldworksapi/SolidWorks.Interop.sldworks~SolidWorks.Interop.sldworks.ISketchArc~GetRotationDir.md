# GetRotationDir Method (ISketchArc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetRotationDir`

Gets the rotation direction of this sketch arc.
Gets the rotation direction of this sketch arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRotationDir() As System.Integer
```

```

Dim instance As ISketchArc
Dim value As System.Integer
 
value = instance.GetRotationDir()
```

```

System.int GetRotationDir()
```

```

System.int GetRotationDir(); 
```

#### Return Value

Rotation direction with respect to the normal of the arc's sketch plane (counterclockwise = 1, clockwise = -1) (see **Remarks**)

Remarks

This method determines the direction that the sketch proceeds around this arc, beginning at the arc's start point and ending at the arc's end point. The direction is with respect to the normal of the arc's sketch plane and not with respect to the viewer.

| If the normal to the arc's sketch plane is... | And the normal to the arc is... | And this method returns... | It means that... |
| --- | --- | --- | --- |
| (0, 0, -1) | (0, 0, 1) | 1 (counterclockwise) | With respect to its sketch plane's normal (from behind the screen), the arc travels counterclockwise from its start point to its end point.  Note that from the perspective of the viewer (in front of the screen), the arc travels clockwise from its start point to its end point. |

Example

See the [ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md) examples.

Example

[Get All Elements in Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md)  
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.md)
