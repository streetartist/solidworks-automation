# ScaleOrCopy Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ScaleOrCopy`

Scales and optionally copies the selected sketch items or annotations.
Scales and optionally copies the selected sketch items or annotations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ScaleOrCopy( _
   ByVal Copy As System.Boolean, _
   ByVal NumCopies As System.Integer, _
   ByVal BaseX As System.Double, _
   ByVal BaseY As System.Double, _
   ByVal BaseZ As System.Double, _
   ByVal Scale As System.Double _
) 
```

```

Dim instance As IModelDocExtension
Dim Copy As System.Boolean
Dim NumCopies As System.Integer
Dim BaseX As System.Double
Dim BaseY As System.Double
Dim BaseZ As System.Double
Dim Scale As System.Double
 
instance.ScaleOrCopy(Copy, NumCopies, BaseX, BaseY, BaseZ, Scale)
```

```

void ScaleOrCopy( 
   System.bool Copy,
   System.int NumCopies,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double Scale
)
```

```

void ScaleOrCopy( 
   System.bool Copy,
   System.int NumCopies,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double Scale
) 
```

#### Parameters

*Copy*
:   True to copy the sketch items or annotations, false to not

*NumCopies*
:   Number of copies

*BaseX*
:   X coordinate of the base point

*BaseY*
:   Y coordinate of the base point

*BaseZ*
:   Z coordinate of the base point

*Scale*
:   Factor by which to scale the sketch entities or annotations

Remarks

Before calling this method, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the entities to scale or copy.

Using this method may break existing sketch relations, including relations that are automatically created when offsetting or converting entities. Use the [ISketchRelationManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md) methods before and after using this method to determine whether all sketch relations remain intact.

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
[IModelDocExtension::RotateOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RotateOrCopy.md)
