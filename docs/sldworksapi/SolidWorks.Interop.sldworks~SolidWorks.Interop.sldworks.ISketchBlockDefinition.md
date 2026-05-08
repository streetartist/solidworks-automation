# ISketchBlockDefinition Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition`

Allows access to information about a block definition.
Allows access to information about a block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISketchBlockDefinition 
```

```

Dim instance As ISketchBlockDefinition
```

```

public interface ISketchBlockDefinition 
```

```

public interface class ISketchBlockDefinition 
```

Remarks

Using this interface, you can:

- Get and set:

  - Name of the block
  - Whether the block links to a file, and get or set the name of that file
- Get:

  - All [instances of the block](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)
  - Sketch of this block definition
  - All notes and dimensions and the number of all notes and dimensions

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Example

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)  
[Get Block Instance in Part or Assembly (VBA)](Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm)  
[Get Blocks in Drawing (VBA)](Get_Blocks_in_Drawing_Example_VB.htm)  
[Create Block Definition and Insert Block Instance (C#)](Create_Block_Definition_and_Insert_Block_Instance_Example_CSharp.htm)  
[Create Block Definition and Insert Block Instance (VBA)](Create_Block_Definition_and_Insert_Block_Instance_Example_VB.htm)  
[Create Block Definition and Insert Block Instance (VB.NET)](Create_Block_Definition_and_Insert_Block_Instance_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)
