# ModelToSketchTransform Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform`

Gets the model-to-sketch transform for this sketch.
Gets the model-to-sketch transform for this sketch.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ModelToSketchTransform As MathTransform
```

```

Dim instance As ISketch
Dim value As MathTransform
 
instance.ModelToSketchTransform = value
 
value = instance.ModelToSketchTransform
```

```

MathTransform ModelToSketchTransform {get; set;}
```

```

property MathTransform^ ModelToSketchTransform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

#### Property Value

[Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[IModelDoc2::SketchSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSplineByEqnParams.md)  
[IModelDoc2::SketchSplineByEqnParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSplineByEqnParams2.md)
