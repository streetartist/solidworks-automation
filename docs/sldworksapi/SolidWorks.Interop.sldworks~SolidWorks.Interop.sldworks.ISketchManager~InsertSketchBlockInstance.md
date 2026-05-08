# InsertSketchBlockInstance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchBlockInstance`

Inserts a block instance at the specified location using the block definition.
Inserts a block instance at the specified location using the block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSketchBlockInstance( _
   ByVal BlockDef As SketchBlockDefinition, _
   ByVal Position As MathPoint, _
   ByVal Scale As System.Double, _
   ByVal Angle As System.Double _
) As SketchBlockInstance
```

```

Dim instance As ISketchManager
Dim BlockDef As SketchBlockDefinition
Dim Position As MathPoint
Dim Scale As System.Double
Dim Angle As System.Double
Dim value As SketchBlockInstance
 
value = instance.InsertSketchBlockInstance(BlockDef, Position, Scale, Angle)
```

```

SketchBlockInstance InsertSketchBlockInstance( 
   SketchBlockDefinition BlockDef,
   MathPoint Position,
   System.double Scale,
   System.double Angle
)
```

```

SketchBlockInstance^ InsertSketchBlockInstance( 
   SketchBlockDefinition^ BlockDef,
   MathPoint^ Position,
   System.double Scale,
   System.double Angle
) 
```

#### Parameters

*BlockDef*
:   [Block](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md) for this block instance

*Position*
:   [Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of this block instance

*Scale*
:   Scale for this block instance

*Angle*
:   Rotation angle for this block instance

#### Return Value

[Block instance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)

Remarks

This method creates a block definition if the block definition does not exist.

-  or -

If the definition exists, then this method uses that block definition to create the block instance. The name of the block instance is the same as the filename of the block file, without the filename extension.

If the entities of a block are associated with one or more layers and those layers do not already exist in the drawing, then the layers are inserted in the drawing and the associations between the entities of the block and the layers are maintained.

The block instance is inserted on the current drawing layer.

**TIP:** If inserting the same sketch block multiple times, do not create the block definition more than once. Instead, use the same block definition for each call to SketchManager::InsertSketchBlockInstance.

To save a block instance and its definition into a block file (**.sldblk**), use [ISketchBlockDefinition::Save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save.md).

This method does not work for drawings opened in view-only mode.

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
