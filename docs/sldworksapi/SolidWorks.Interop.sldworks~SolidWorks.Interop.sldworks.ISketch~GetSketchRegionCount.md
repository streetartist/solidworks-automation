# GetSketchRegionCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegionCount`

Gets the number of sketch regions in this sketch.
Gets the number of sketch regions in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchRegionCount() As System.Integer
```

```

Dim instance As ISketch
Dim value As System.Integer
 
value = instance.GetSketchRegionCount()
```

```

System.int GetSketchRegionCount()
```

```

System.int GetSketchRegionCount(); 
```

#### Return Value

Number of sketch regions

Remarks

Call this method before calling [ISketch::IGetSketchRegions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchRegions.md) to get the size of the array for that method.

Example

[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)  
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)  
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketchRegion::GetSketchRegions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegions.md)
