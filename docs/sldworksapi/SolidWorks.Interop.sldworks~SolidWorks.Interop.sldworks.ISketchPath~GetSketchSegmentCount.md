# GetSketchSegmentCount Method (ISketchPath)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketchSegmentCount`

Gets the number of sketch segments in this sketch path.
Gets the number of sketch segments in this sketch path.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchSegmentCount() As System.Integer
```

```

Dim instance As ISketchPath
Dim value As System.Integer
 
value = instance.GetSketchSegmentCount()
```

```

System.int GetSketchSegmentCount()
```

```

System.int GetSketchSegmentCount(); 
```

#### Return Value

Number of sketch segments

Remarks

Call this method before calling [ISketch::IGetSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetSketchSegments.md) to get the size of the array for that method.

Example

See the [ISketchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.md)  
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.md)  
[SketdhPath:;GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketchSegments.md)
