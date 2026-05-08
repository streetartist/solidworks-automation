# Layer Property (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Layer`

Gets or sets the layer used by this annotation. Layers are supported only in SOLIDWORKS drawings.
Gets or sets the layer used by this annotation. Layers are supported only in SOLIDWORKS  
drawings.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Layer As System.String
```

```

Dim instance As IAnnotation
Dim value As System.String
 
instance.Layer = value
 
value = instance.Layer
```

```

System.string Layer {get; set;}
```

```

property System.String^ Layer {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the layer used for this annotation

Remarks

In Drawing documents, annotations can be created on a specific layer. This property allows you to get or set the layer used by this annotation. You can also set an annotation to not be on any layer by specifying "" for theLayer.

**NOTE:** The return value might be an empty string because an old document might not contain layers. This also occurs if annotations have been generated in a new document that does not have layers defined.

Example

[Insert Autoballoons (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
