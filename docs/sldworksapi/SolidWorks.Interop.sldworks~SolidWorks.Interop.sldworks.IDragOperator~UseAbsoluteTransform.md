# UseAbsoluteTransform Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~UseAbsoluteTransform`

Gets or sets whether the transforms to use with IDragOperator::Drag or IDragOperator::IDrag are absolute or relative.
Gets or sets whether the transforms to use with [IDragOperator::Drag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.md) or [IDragOperator::IDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IDrag.md) are absolute or relative.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseAbsoluteTransform As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.UseAbsoluteTransform = value
 
value = instance.UseAbsoluteTransform
```

```

System.bool UseAbsoluteTransform {get; set;}
```

```

property System.bool UseAbsoluteTransform {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use absolute transforms, false to use relative transforms

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::TransformType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~TransformType.md)
