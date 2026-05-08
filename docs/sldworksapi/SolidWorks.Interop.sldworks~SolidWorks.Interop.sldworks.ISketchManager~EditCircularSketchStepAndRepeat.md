# EditCircularSketchStepAndRepeat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditCircularSketchStepAndRepeat`

Edits a circular sketch pattern.
Edits a circular sketch pattern.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditCircularSketchStepAndRepeat( _
   ByVal ArcRadius As System.Double, _
   ByVal ArcAngle As System.Double, _
   ByVal PatternNum As System.Integer, _
   ByVal PatternSpacing As System.Double, _
   ByVal PatternRotate As System.Boolean, _
   ByVal DeleteInstances As System.String, _
   ByVal RadiusDim As System.Boolean, _
   ByVal AngleDim As System.Boolean, _
   ByVal CreateNumOfInstancesDim As System.Boolean, _
   ByVal Seeds As System.String _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim ArcRadius As System.Double
Dim ArcAngle As System.Double
Dim PatternNum As System.Integer
Dim PatternSpacing As System.Double
Dim PatternRotate As System.Boolean
Dim DeleteInstances As System.String
Dim RadiusDim As System.Boolean
Dim AngleDim As System.Boolean
Dim CreateNumOfInstancesDim As System.Boolean
Dim Seeds As System.String
Dim value As System.Boolean
 
value = instance.EditCircularSketchStepAndRepeat(ArcRadius, ArcAngle, PatternNum, PatternSpacing, PatternRotate, DeleteInstances, RadiusDim, AngleDim, CreateNumOfInstancesDim, Seeds)
```

```

System.bool EditCircularSketchStepAndRepeat( 
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.string DeleteInstances,
   System.bool RadiusDim,
   System.bool AngleDim,
   System.bool CreateNumOfInstancesDim,
   System.string Seeds
)
```

```

System.bool EditCircularSketchStepAndRepeat( 
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.String^ DeleteInstances,
   System.bool RadiusDim,
   System.bool AngleDim,
   System.bool CreateNumOfInstancesDim,
   System.String^ Seeds
) 
```

#### Parameters

*ArcRadius*
:   Radius of the circular sketch pattern

*ArcAngle*
:   Angle relative to the sketch entities being patterned

*PatternNum*
:   Total number of instances, including the seed geometry

*PatternSpacing*
:   Spacing between pattern instances

*PatternRotate*
:   True to rotate the pattern, false to not

*DeleteInstances*
:   Number of instances to delete, passed as a string formatted as: "(a) (b) (c) "

*RadiusDim*
:   True to display the radius dimension in the graphics area, false to not

*AngleDim*
:   True to display the angle dimension in the graphics area, false to not

*CreateNumOfInstancesDim*
:   True to display the number of instances dimension in the graphics area, false to not

*Seeds*
:   Array of the names of the entities, separated by the underscore character (\_), that comprise the seed pattern (e.g., "Line1\_Line2\_Line3\_Line4" for a rectangular-shaped seed pattern)

#### Return Value

True if the circular sketch pattern is successfully edited, false if not

Remarks

The radius, angle, and number of instances dimensions displayed in the graphics area can be modified by interactive users.

Example

[Create and Edit Circular Sketch Pattern (VB.NET)](Create_and_Edit_Circular_Sketch_Pattern_Example_VBNET.htm)  
[Create and Edit Circular Sketch Pattern (VBA)](Create_and_Edit_Circular_Sketch_Pattern_Example_VB.htm)  
[Create and Edit Circular Sketch Pattern (C#)](Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::CreateCircularSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircularSketchStepAndRepeat.md)  
[ISketchManager::CreateLinearSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLinearSketchStepAndRepeat.md)  
[ISketchManager::EditLinearSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditLinearSketchStepAndRepeat.md)
