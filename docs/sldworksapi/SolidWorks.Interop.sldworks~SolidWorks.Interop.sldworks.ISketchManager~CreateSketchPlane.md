# CreateSketchPlane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchPlane`

Creates a 3D sketch plane.
Creates a 3D sketch plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSketchPlane( _
   ByVal Relation1 As System.Integer, _
   ByVal Relation2 As System.Integer, _
   ByVal Relation3 As System.Integer _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim Relation1 As System.Integer
Dim Relation2 As System.Integer
Dim Relation3 As System.Integer
Dim value As System.Boolean
 
value = instance.CreateSketchPlane(Relation1, Relation2, Relation3)
```

```

System.bool CreateSketchPlane( 
   System.int Relation1,
   System.int Relation2,
   System.int Relation3
)
```

```

System.bool CreateSketchPlane( 
   System.int Relation1,
   System.int Relation2,
   System.int Relation3
) 
```

#### Parameters

*Relation1*
:   Relation as defined in [swConstraintType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html) for the first selection to position the 3D sketch plane

*Relation2*
:   Relation as defined in [swConstraintType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html) for the second selection to position the 3D sketch plane

*Relation3*
:   Relation as defined in [swConstraintType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html) for the third selection to position the 3D sketch plane

#### Return Value

True if the 3D sketch plane is created, false if not

Remarks

This method gets the selected items from the selection list in the order in which they were selected and applies the specified relation to them. If fewer than three items were selected, then only the first, or first and second, values are used.

Example

[Create 3D Sketch Plane (C#)](Create_3D_Sketch_Plane_Example_CSharp.htm)  
[Create 3D Sketch Plane (VB.NET)](Create_3D_Sketch_Plane_Example_VBNET.htm)  
[Create 3D Sketch Plane (VBA)](Create_3D_Sketch_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
