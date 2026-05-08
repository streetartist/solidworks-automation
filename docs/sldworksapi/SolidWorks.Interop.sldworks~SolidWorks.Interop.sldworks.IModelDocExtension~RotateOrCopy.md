# RotateOrCopy Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RotateOrCopy`

Rotates and optionally copies the selected sketch entities or annotations.
Rotates and optionally copies the selected sketch entities or annotations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RotateOrCopy( _
   ByVal Copy As System.Boolean, _
   ByVal NumCopies As System.Integer, _
   ByVal KeepRelations As System.Boolean, _
   ByVal BaseX As System.Double, _
   ByVal BaseY As System.Double, _
   ByVal BaseZ As System.Double, _
   ByVal DestX As System.Double, _
   ByVal DestY As System.Double, _
   ByVal DestZ As System.Double, _
   ByVal Angle As System.Double _
) 
```

```

Dim instance As IModelDocExtension
Dim Copy As System.Boolean
Dim NumCopies As System.Integer
Dim KeepRelations As System.Boolean
Dim BaseX As System.Double
Dim BaseY As System.Double
Dim BaseZ As System.Double
Dim DestX As System.Double
Dim DestY As System.Double
Dim DestZ As System.Double
Dim Angle As System.Double
 
instance.RotateOrCopy(Copy, NumCopies, KeepRelations, BaseX, BaseY, BaseZ, DestX, DestY, DestZ, Angle)
```

```

void RotateOrCopy( 
   System.bool Copy,
   System.int NumCopies,
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double DestX,
   System.double DestY,
   System.double DestZ,
   System.double Angle
)
```

```

void RotateOrCopy( 
   System.bool Copy,
   System.int NumCopies,
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double DestX,
   System.double DestY,
   System.double DestZ,
   System.double Angle
) 
```

#### Parameters

*Copy*
:   True to copy sketch entities or annotations, false to not

*NumCopies*
:   Number of copies

*KeepRelations*
:   True to keep sketch relations, false to not

*BaseX*
:   X coordinate of the base point from which to rotate the sketch entities or annotations

*BaseY*
:   Y coordinate of the base point from which to rotate the sketch entities or annotations

*BaseZ*
:   Z coordinate of the base point from which to rotate the sketch entities or annotations

*DestX*
:   X vector component of the axis of rotation parallel to the base point

*DestY*
:   Y vector component of the axis of rotation parallel to the base point

*DestZ*
:   Z vector component of the axis of rotation parallel to the base point

*Angle*
:   Angle at which to rotate or move the sketch entities or annotations

Remarks

Typically a user will specify 0, 0, 1 for the x, y, z destination point coordinates and 0 for the baseZ argument. The baseX and baseY arguments should specify the center of rotation for the sketch entity.

Example

[Rotate, Scale, and Copy Sketch (C#)](Rotate_Scale_Copy_Sketch_Example_CSharp.htm)  
[Rotate, Scale, and Copy Sketch (VB.NET)](Rotate_Scale_Copy_Sketch_Example_VBNET.htm)  
[Rotate, Scale, and Copy Sketch (VBA)](Rotate_Scale_Copy_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::MoveOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveOrCopy.md)  
[IModelDocExtension::ScaleOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ScaleOrCopy.md)
