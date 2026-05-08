# GetCoincidenceTransform2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetCoincidenceTransform2`

Calculates the transformation matrix, which would make the input body coincident with this body if the transformation matrix is applied.
Calculates the transformation matrix, which would make the input body coincident with this body if the transformation matrix is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoincidenceTransform2( _
   ByVal BodyDispIn As System.Object, _
   ByRef Xform As MathTransform _
) As System.Boolean
```

```

Dim instance As IBody2
Dim BodyDispIn As System.Object
Dim Xform As MathTransform
Dim value As System.Boolean
 
value = instance.GetCoincidenceTransform2(BodyDispIn, Xform)
```

```

System.bool GetCoincidenceTransform2( 
   System.object BodyDispIn,
   out MathTransform Xform
)
```

```

System.bool GetCoincidenceTransform2( 
   System.Object^ BodyDispIn,
   [Out] MathTransform^ Xform
) 
```

#### Parameters

*BodyDispIn*
:   [Input body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*Xform*
:   Pointer to the [transformation matrix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

#### Return Value

True if this body and the input body can coincide by applying the transformation matrix, false if not

Example

[Calculate Transformations in Part (C#)](Calculate_Transformations_in_Part_Example_CSharp.htm)  
[Calculate Transformations in Part (VB.NET)](Calculate_Transformations_in_Part_Example_VBNET.htm)  
[Calculate Transformations in Part (VBA)](Calculate_Transformations_in_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
