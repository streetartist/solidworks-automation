# CreateSketchSlot Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchSlot`

Creates a sketch slot.
Creates a sketch slot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSketchSlot( _
   ByVal SlotCreationType As System.Integer, _
   ByVal SlotLengthType As System.Integer, _
   ByVal Width As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal X3 As System.Double, _
   ByVal Y3 As System.Double, _
   ByVal Z3 As System.Double, _
   ByVal CenterArcDirection As System.Integer, _
   ByVal AddDimension As System.Boolean _
) As SketchSlot
```

```

Dim instance As ISketchManager
Dim SlotCreationType As System.Integer
Dim SlotLengthType As System.Integer
Dim Width As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim X3 As System.Double
Dim Y3 As System.Double
Dim Z3 As System.Double
Dim CenterArcDirection As System.Integer
Dim AddDimension As System.Boolean
Dim value As SketchSlot
 
value = instance.CreateSketchSlot(SlotCreationType, SlotLengthType, Width, X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3, CenterArcDirection, AddDimension)
```

```

SketchSlot CreateSketchSlot( 
   System.int SlotCreationType,
   System.int SlotLengthType,
   System.double Width,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3,
   System.int CenterArcDirection,
   System.bool AddDimension
)
```

```

SketchSlot^ CreateSketchSlot( 
   System.int SlotCreationType,
   System.int SlotLengthType,
   System.double Width,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3,
   System.int CenterArcDirection,
   System.bool AddDimension
) 
```

#### Parameters

*SlotCreationType*
:   Type of sketch slot as defined in [swSketchSlotCreationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchSlotCreationType_e.html)

*SlotLengthType*
:   Type of length of sketch slot as defined in [swSketchSlotLengthType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchSlotLengthType_e.html)

*Width*
:   Width of sketch slot

*X1*
:   x coordinate of point 1

*Y1*
:   y coordinate of point 1

*Z1*
:   z coordinate of point 2

*X2*
:   x coordinate of point 2

*Y2*
:   y coordinate of point 2

*Z2*
:   z coordinate of point 2

*X3*
:   x coordinate of point 3

*Y3*
:   y coordinate of point 3

*Z3*
:   z coordinate of point 3

*CenterArcDirection*
:   - -1 = Clockwise (CW)
    - 1 = Counterclockwise (CCW)

*AddDimension*
:   True to automatically add dimensions, false to not

#### Return Value

[Sketch slot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.md)

Example

[Insert and Resize Sketch Slot (C#)](Insert_and_Resize_Sketch_Slot_Example_CSharp.htm)  
[Insert and Resize Sketch Slot (VB.NET)](Insert_and_Resize_Sketch_Slot_Example_VBNET.htm)  
[Insert and Resize Sketch Slot (VBA)](Insert_and_Resize_Sketch_Slot_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
