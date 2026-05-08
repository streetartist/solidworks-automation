# GetFirstLoop Method (ISketchRegion)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~GetFirstLoop`

Gets the first loop in this sketch region.
Gets the first loop in this sketch region.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstLoop() As Loop2
```

```

Dim instance As ISketchRegion
Dim value As Loop2
 
value = instance.GetFirstLoop()
```

```

Loop2 GetFirstLoop()
```

```

Loop2^ GetFirstLoop(); 
```

#### Return Value

First [loop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)

Example

[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)  
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)  
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md)  
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.md)
