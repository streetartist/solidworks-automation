# CreateLinearSketchStepAndRepeat Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLinearSketchStepAndRepeat`

Creates a linear sketch pattern.
Creates a linear sketch pattern.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLinearSketchStepAndRepeat( _
   ByVal NumX As System.Integer, _
   ByVal NumY As System.Integer, _
   ByVal SpacingX As System.Double, _
   ByVal SpacingY As System.Double, _
   ByVal AngleX As System.Double, _
   ByVal AngleY As System.Double, _
   ByVal DeleteInstances As System.String, _
   ByVal XSpacingDim As System.Boolean, _
   ByVal YSpacingDim As System.Boolean, _
   ByVal AngleDim As System.Boolean, _
   ByVal CreateNumOfInstancesDimInXDir As System.Boolean, _
   ByVal CreateNumOfInstancesDimInYDir As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim NumX As System.Integer
Dim NumY As System.Integer
Dim SpacingX As System.Double
Dim SpacingY As System.Double
Dim AngleX As System.Double
Dim AngleY As System.Double
Dim DeleteInstances As System.String
Dim XSpacingDim As System.Boolean
Dim YSpacingDim As System.Boolean
Dim AngleDim As System.Boolean
Dim CreateNumOfInstancesDimInXDir As System.Boolean
Dim CreateNumOfInstancesDimInYDir As System.Boolean
Dim value As System.Boolean
 
value = instance.CreateLinearSketchStepAndRepeat(NumX, NumY, SpacingX, SpacingY, AngleX, AngleY, DeleteInstances, XSpacingDim, YSpacingDim, AngleDim, CreateNumOfInstancesDimInXDir, CreateNumOfInstancesDimInYDir)
```

```

System.bool CreateLinearSketchStepAndRepeat( 
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.string DeleteInstances,
   System.bool XSpacingDim,
   System.bool YSpacingDim,
   System.bool AngleDim,
   System.bool CreateNumOfInstancesDimInXDir,
   System.bool CreateNumOfInstancesDimInYDir
)
```

```

System.bool CreateLinearSketchStepAndRepeat( 
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.String^ DeleteInstances,
   System.bool XSpacingDim,
   System.bool YSpacingDim,
   System.bool AngleDim,
   System.bool CreateNumOfInstancesDimInXDir,
   System.bool CreateNumOfInstancesDimInYDir
) 
```

#### Parameters

*NumX*
:   Total number of instances along the x axis, including the seed

*NumY*
:   Total number of instances along the y axis, including the seed

*SpacingX*
:   Spacing between instances along the x axis

*SpacingY*
:   Spacing between instances along the y axis

*AngleX*
:   Angle for direction 1 relative to the x axis

*AngleY*
:   Angle for direction 2 relative to the y axis

*DeleteInstances*
:   Number of instances to delete, passed as a string in the format: "(a) (b) (c) "

*XSpacingDim*
:   True to display the spacing between instances dimension along the x axis in the graphics area, false to not

*YSpacingDim*
:   True to display the spacing between instances dimension along the y axis in the graphics area, false to not

*AngleDim*
:   True to display the angle dimension between axes in the graphics area, false to not

*CreateNumOfInstancesDimInXDir*
:   True to display the number of instances in the x direction dimension in the graphics area, false to not

*CreateNumOfInstancesDimInYDir*
:   True to display the number of instances in the y direction dimension in the graphics area, false to not

#### Return Value

True if the linear sketch pattern is created, false if not

Remarks

The spacing instances, angle, and number of instances dimensions displayed in the graphics area can be modified by interactive users.

Example

[Create and Edit Linear Sketch Pattern (VB.NET)](Create_and_Edit_Linear_Sketch_Pattern_Example_VBNET.htm)  
[Create and Edit Linear Sketch Patten (VBA)](Create_and_Edit_Linear_Sketch_Pattern_Example_VB.htm)  
[Create and Edit Linear Sketch Pattern (C#)](Create_and_Edit_Linear_Sketch_Pattern_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::EditLinearSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditLinearSketchStepAndRepeat.md)  
[ISketchManager::CreateCircularSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircularSketchStepAndRepeat.md)  
[ISketchManager::EditCircularSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditCircularSketchStepAndRepeat.md)
