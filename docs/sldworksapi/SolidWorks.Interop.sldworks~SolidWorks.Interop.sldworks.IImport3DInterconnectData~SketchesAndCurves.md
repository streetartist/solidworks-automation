# SketchesAndCurves Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~SketchesAndCurves`

Gets or sets whether to import unconsumed sketches or curve data as 2D or 3D sketches.
Gets or sets whether to import unconsumed sketches or curve data as 2D or 3D sketches.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SketchesAndCurves As System.Boolean
```

```

Dim instance As IImport3DInterconnectData
Dim value As System.Boolean
 
instance.SketchesAndCurves = value
 
value = instance.SketchesAndCurves
```

```

System.bool SketchesAndCurves {get; set;}
```

```

property System.bool SketchesAndCurves {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import unconsumed sketches or curve data as 2D or 3D sketches, false to not

Example

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md)  
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.md)
