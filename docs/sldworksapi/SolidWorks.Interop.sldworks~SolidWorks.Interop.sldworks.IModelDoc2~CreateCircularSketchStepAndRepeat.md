# CreateCircularSketchStepAndRepeat Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCircularSketchStepAndRepeat`

Obsolete. Superseded by ISketchManager::CreateCircularSketchStepAndRepeat.
Obsolete. Superseded by [ISketchManager::CreateCircularSketchStepAndRepeat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircularSketchStepAndRepeat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCircularSketchStepAndRepeat( _
   ByVal ArcRadius As System.Double, _
   ByVal ArcAngle As System.Double, _
   ByVal PatternNum As System.Integer, _
   ByVal PatternSpacing As System.Double, _
   ByVal PatternRotate As System.Boolean, _
   ByVal DeleteInstances As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim ArcRadius As System.Double
Dim ArcAngle As System.Double
Dim PatternNum As System.Integer
Dim PatternSpacing As System.Double
Dim PatternRotate As System.Boolean
Dim DeleteInstances As System.String
Dim value As System.Boolean
 
value = instance.CreateCircularSketchStepAndRepeat(ArcRadius, ArcAngle, PatternNum, PatternSpacing, PatternRotate, DeleteInstances)
```

```

System.bool CreateCircularSketchStepAndRepeat( 
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.string DeleteInstances
)
```

```

System.bool CreateCircularSketchStepAndRepeat( 
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.String^ DeleteInstances
) 
```

#### Parameters

*ArcRadius*
:   Radius to be used in the circular sketch pattern

*ArcAngle*
:   Angle relative to the sketch entities being patterned

*PatternNum*
:   Total number of instances, including the seed geometry

*PatternSpacing*
:   Spacing between pattern instances in radians

*PatternRotate*
:   True to rotate the pattern, false to not

*DeleteInstances*
:   Number of instances to delete passed as a string formatted as: "(a) (b) (c) "

#### Return Value

True if the sketch pattern was created successfully, false otherwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateLinearSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateLinearSketchStepAndRepeat.md)
