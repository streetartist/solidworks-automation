# BlockToSketchTransform Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~BlockToSketchTransform`

Gets the MathTransform required to transform coordinates from the sketch block space to the host sketch space.
Gets the MathTransform required to transform coordinates from the sketch block space to the host sketch space.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property BlockToSketchTransform As MathTransform
```

```

Dim instance As ISketchBlockInstance
Dim value As MathTransform
 
value = instance.BlockToSketchTransform
```

```

MathTransform BlockToSketchTransform {get;}
```

```

property MathTransform^ BlockToSketchTransform {
   MathTransform^ get();
}
```

#### Property Value

[Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockInstance::GetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetSketch.md)
