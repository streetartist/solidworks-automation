# MakeSketchBlockFromSketch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch`

Creates a block definition at the specified location using all of the sketch entities in the active sketch.
Creates a block definition at the specified location using all of the sketch entities in the active sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeSketchBlockFromSketch( _
   ByVal InsertionPoint As MathPoint, _
   ByVal Sketch As Sketch _
) As SketchBlockDefinition
```

```

Dim instance As ISketchManager
Dim InsertionPoint As MathPoint
Dim Sketch As Sketch
Dim value As SketchBlockDefinition
 
value = instance.MakeSketchBlockFromSketch(InsertionPoint, Sketch)
```

```

SketchBlockDefinition MakeSketchBlockFromSketch( 
   MathPoint InsertionPoint,
   Sketch Sketch
)
```

```

SketchBlockDefinition^ MakeSketchBlockFromSketch( 
   MathPoint^ InsertionPoint,
   Sketch^ Sketch
) 
```

#### Parameters

*InsertionPoint*
:   [Insertion point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md), which is a 2D point with z = 0.0, for the block definition

*Sketch*
:   [Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) to use

#### Return Value

[Block definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)

Remarks

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::MakeSketchBlockFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md)  
[ISketchManager::MakeSketchBlockFromSelected Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md)
