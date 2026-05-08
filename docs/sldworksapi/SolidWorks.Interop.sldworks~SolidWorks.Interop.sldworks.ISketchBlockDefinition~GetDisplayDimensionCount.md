# GetDisplayDimensionCount Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensionCount`

Gets the number of display dimensions in this block definition.
Gets the number of display dimensions in this block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayDimensionCount() As System.Integer
```

```

Dim instance As ISketchBlockDefinition
Dim value As System.Integer
 
value = instance.GetDisplayDimensionCount()
```

```

System.int GetDisplayDimensionCount()
```

```

System.int GetDisplayDimensionCount(); 
```

#### Return Value

Number of display dimensions

Remarks

Call this method before calling [ISketchBlockDefinition::IGetDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetDisplayDimensions.md) to get the size of the array for that method.

Example

[Get Block Instance in Part or Assembly (VBA)](Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.md)
