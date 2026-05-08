# IGetSketchBlockInstances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchBlockInstances`

Gets the block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree).
Gets the block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchBlockInstances( _
   ByVal Count As System.Integer _
) As SketchBlockInstance
```

```

Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchBlockInstance
 
value = instance.IGetSketchBlockInstances(Count)
```

```

SketchBlockInstance IGetSketchBlockInstances( 
   System.int Count
)
```

```

SketchBlockInstance^ IGetSketchBlockInstances( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of block instances in this sketch

#### Return Value

- in-process, unmanaged C++: Pointer to an array containing the [block instances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) in this sketch

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISketch::GetSketchBlockInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchBlockInstanceCount.md) before calling this method to get the number of block instances in this sketch.

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
