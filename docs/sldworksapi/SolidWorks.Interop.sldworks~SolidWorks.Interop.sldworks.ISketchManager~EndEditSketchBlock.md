# EndEditSketchBlock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EndEditSketchBlock`

Saves or discards your edits of the block and then ends the current editing session of this block.
Saves or discards your edits of the block and then ends the current editing session of this block.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EndEditSketchBlock( _
   ByVal AcceptChanges As System.Boolean _
) 
```

```

Dim instance As ISketchManager
Dim AcceptChanges As System.Boolean
 
instance.EndEditSketchBlock(AcceptChanges)
```

```

void EndEditSketchBlock( 
   System.bool AcceptChanges
)
```

```

void EndEditSketchBlock( 
   System.bool AcceptChanges
) 
```

#### Parameters

*AcceptChanges*
:   True to save your edits, false to discard them

Remarks

Use [ISketchManager::EditSketchBlock](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditSketchBlock.md) to put the block in edit mode.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)
