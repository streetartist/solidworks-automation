# GetSketchBlockInstanceCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchBlockInstanceCount`

Gets the number of block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree).
Gets the number of block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchBlockInstanceCount() As System.Integer
```

```

Dim instance As ISketch
Dim value As System.Integer
 
value = instance.GetSketchBlockInstanceCount()
```

```

System.int GetSketchBlockInstanceCount()
```

```

System.int GetSketchBlockInstanceCount(); 
```

#### Return Value

Number of block instances in this sketch

Remarks

Call this method before calling [ISketch::IGetSketchBlockInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchBlockInstances.md) to get the size of the array for that method.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchBlockInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchBlockInstances.md)  
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)
