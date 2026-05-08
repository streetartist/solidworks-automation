# GetSketchBlockDefinitionCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitionCount`

Gets the number of block definitions in the model.
Gets the number of block definitions in the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchBlockDefinitionCount() As System.Integer
```

```

Dim instance As ISketchManager
Dim value As System.Integer
 
value = instance.GetSketchBlockDefinitionCount()
```

```

System.int GetSketchBlockDefinitionCount()
```

```

System.int GetSketchBlockDefinitionCount(); 
```

#### Return Value

Number of block definitions in the model

Remarks

Call this method before calling [ISketchManager::IGetSketchBlockDefinitions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~IGetSketchBlockDefinitions.md) to get the size of the array for that method.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::GetSketchBlockDefinitions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.md)
