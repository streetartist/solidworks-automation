# MakeSketchBlockFromSelected Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected`

Creates a block definition at the specified location from the selected entities.
Creates a block definition at the specified location from the selected entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeSketchBlockFromSelected( _
   ByVal InsertionPoint As MathPoint _
) As SketchBlockDefinition
```

```

Dim instance As ISketchManager
Dim InsertionPoint As MathPoint
Dim value As SketchBlockDefinition
 
value = instance.MakeSketchBlockFromSelected(InsertionPoint)
```

```

SketchBlockDefinition MakeSketchBlockFromSelected( 
   MathPoint InsertionPoint
)
```

```

SketchBlockDefinition^ MakeSketchBlockFromSelected( 
   MathPoint^ InsertionPoint
) 
```

#### Parameters

*InsertionPoint*
:   [Insertion point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md), which is a 2D point with z = 0.0, for the block definition

#### Return Value

[Block definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)

Remarks

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Example

[Create Block Definition and Insert Block Instance (VBA)](Create_Block_Definition_and_Insert_Block_Instance_Example_VB.htm)  
[Create Block Definition and Insert Block Instance (C#)](Create_Block_Definition_and_Insert_Block_Instance_Example_CSharp.htm)  
[Create Block Definition and Insert Block Instance (VB.NET)](Create_Block_Definition_and_Insert_Block_Instance_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::MakeSketchBlockFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md)  
[ISketchManager::MakeSketchBlockFromSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md)
