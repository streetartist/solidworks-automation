# Owner Property (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Owner`

Gets the owner of this annotation.
Gets the owner of this annotation.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Owner As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
instance.Owner = value
 
value = instance.Owner
```

```

System.object Owner {get; set;}
```

```

property System.Object^ Owner {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Object for the view, sheet, or model document

Remarks

Use [IAnnotation::OwnerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~OwnerType.md) to determine if the annotation is located on a drawing view, drawing sheet, drawing template, assembly, or part.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
