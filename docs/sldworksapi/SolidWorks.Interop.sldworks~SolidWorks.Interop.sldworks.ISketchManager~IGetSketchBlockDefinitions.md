# IGetSketchBlockDefinitions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~IGetSketchBlockDefinitions`

Gets all of the block definitions.
Gets all of the block definitions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchBlockDefinitions( _
   ByVal BlockDefCount As System.Integer _
) As SketchBlockDefinition
```

```

Dim instance As ISketchManager
Dim BlockDefCount As System.Integer
Dim value As SketchBlockDefinition
 
value = instance.IGetSketchBlockDefinitions(BlockDefCount)
```

```

SketchBlockDefinition IGetSketchBlockDefinitions( 
   System.int BlockDefCount
)
```

```

SketchBlockDefinition^ IGetSketchBlockDefinitions( 
   System.int BlockDefCount
) 
```

#### Parameters

*BlockDefCount*
:   Number of block definitions

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [block definitions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISketchManager::GetSketchBlockDefinitionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitionCount.md) to get the value of BlockDefCount.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::GetSketchBlockDefinitions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.md)
