# GetCoincidenceTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetCoincidenceTransform`

Obsolete. Superseded by IBody2::GetCoincidenceTransform2.
Obsolete. Superseded by [IBody2::GetCoincidenceTransform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetCoincidenceTransform2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoincidenceTransform( _
   ByVal BodyDispIn As System.Object, _
   ByRef Xform As MathTransform _
) As System.Boolean
```

```

Dim instance As IBody2
Dim BodyDispIn As System.Object
Dim Xform As MathTransform
Dim value As System.Boolean
 
value = instance.GetCoincidenceTransform(BodyDispIn, Xform)
```

```

System.bool GetCoincidenceTransform( 
   System.object BodyDispIn,
   out MathTransform Xform
)
```

```

System.bool GetCoincidenceTransform( 
   System.Object^ BodyDispIn,
   [Out] MathTransform^ Xform
) 
```

#### Parameters

*BodyDispIn*
:   Input body

*Xform*
:   Pointer to the [transformation matrix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

#### Return Value

True if the bodies (the body on which the method is invoked and the input body) can coincide by applying appropriate transforms, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
