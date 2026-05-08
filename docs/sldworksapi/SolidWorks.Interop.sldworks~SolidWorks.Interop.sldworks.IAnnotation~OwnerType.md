# OwnerType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~OwnerType`

Gets the type of owner of this annotation.
Gets the type of owner of this annotation.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OwnerType As System.Integer
```

```

Dim instance As IAnnotation
Dim value As System.Integer
 
instance.OwnerType = value
 
value = instance.OwnerType
```

```

System.int OwnerType {get; set;}
```

```

property System.int OwnerType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of owner of this annotation as defined in [swAnnotationOwner\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnnotationOwner_e.html)

Remarks

Use this property to determine if an annotation is located on drawing view, drawing sheet, drawing template, assembly, or part. Use [IAnnotation::Owner](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Owner.md) to gain access to the owner of the annotation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
