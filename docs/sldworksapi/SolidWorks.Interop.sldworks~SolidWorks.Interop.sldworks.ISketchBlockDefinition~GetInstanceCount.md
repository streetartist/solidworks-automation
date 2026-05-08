# GetInstanceCount Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstanceCount`

Gets the number of block instances of this block definition.
Gets the number of block instances of this block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInstanceCount() As System.Integer
```

```

Dim instance As ISketchBlockDefinition
Dim value As System.Integer
 
value = instance.GetInstanceCount()
```

```

System.int GetInstanceCount()
```

```

System.int GetInstanceCount(); 
```

#### Return Value

Number of block instances

Remarks

Call this method before calling [ISketchBlockDefinition::IGetInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetInstances.md) to get the size of the array for that method.

Example

[Get and Set Blocks in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)  
[Get Blocks in Drawing (VBA)](Get_Blocks_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::GetInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstances.md)
