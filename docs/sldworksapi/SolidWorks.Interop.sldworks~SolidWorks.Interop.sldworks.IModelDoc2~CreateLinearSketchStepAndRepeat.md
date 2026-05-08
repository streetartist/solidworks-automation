# CreateLinearSketchStepAndRepeat Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateLinearSketchStepAndRepeat`

Obsolete. Superseded by ISketchManager::CreateLinearSketchStepAndRepeat.
Obsolete. Superseded by [ISketchManager::CreateLinearSketchStepAndRepeat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLinearSketchStepAndRepeat.md).

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
   ByVal DeleteInstances As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim NumX As System.Integer
Dim NumY As System.Integer
Dim SpacingX As System.Double
Dim SpacingY As System.Double
Dim AngleX As System.Double
Dim AngleY As System.Double
Dim DeleteInstances As System.String
Dim value As System.Boolean
 
value = instance.CreateLinearSketchStepAndRepeat(NumX, NumY, SpacingX, SpacingY, AngleX, AngleY, DeleteInstances)
```

```

System.bool CreateLinearSketchStepAndRepeat( 
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.string DeleteInstances
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
   System.String^ DeleteInstances
) 
```

#### Parameters

*NumX*
:   Total number of instances along direction 1, including the seed

*NumY*
:   Total number of instances along direction 2, including the seed

*SpacingX*
:   Spacing between instances along direction 1

*SpacingY*
:   Spacing between instances along direction 2

*AngleX*
:   Relative to the X axis, the angle for direction 1

*AngleY*
:   Relative to the X axis, the angle for direction 2

*DeleteInstances*
:   Number of instances to delete passed as a string in the format: "(a) (b) (c) "

#### Return Value

True if the sketch pattern was created successfully, false otherwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateCircularSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCircularSketchStepAndRepeat.md)
