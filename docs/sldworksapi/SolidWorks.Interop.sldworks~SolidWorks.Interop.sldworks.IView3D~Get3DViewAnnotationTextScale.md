# Get3DViewAnnotationTextScale Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Get3DViewAnnotationTextScale`

Gets the annotation text scale for this 3D View.
Gets the annotation text scale for this 3D View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Get3DViewAnnotationTextScale( _
   ByRef Scale1 As System.Double, _
   ByRef Scale2 As System.Double _
) 
```

```

Dim instance As IView3D
Dim Scale1 As System.Double
Dim Scale2 As System.Double
 
instance.Get3DViewAnnotationTextScale(Scale1, Scale2)
```

```

void Get3DViewAnnotationTextScale( 
   out System.double Scale1,
   out System.double Scale2
)
```

```

void Get3DViewAnnotationTextScale( 
   [Out] System.double Scale1,
   [Out] System.double Scale2
) 
```

#### Parameters

*Scale1*
:   Numerator of the scale ratio (**n**:n)

*Scale2*
:   Denominator of the scale ratio (n:**n**)

Remarks

This method gets the **Text scale** on the Annotation Properties dialog that appears when you RMB on the Annotations folder in the FeatureManager design tree.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)
