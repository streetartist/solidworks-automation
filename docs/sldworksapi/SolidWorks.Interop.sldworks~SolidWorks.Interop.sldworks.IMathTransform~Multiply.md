# Multiply Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~Multiply`

Multiplies two matrices together.
Multiplies two matrices together.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Multiply( _
   ByVal TransformObjIn As System.Object _
) As System.Object
```

```

Dim instance As IMathTransform
Dim TransformObjIn As System.Object
Dim value As System.Object
 
value = instance.Multiply(TransformObjIn)
```

```

System.object Multiply( 
   System.object TransformObjIn
)
```

```

System.Object^ Multiply( 
   System.Object^ TransformObjIn
) 
```

#### Parameters

*TransformObjIn*
:   [Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) by which to multiply the calling math transform

#### Return Value

Newly created [math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) object or null or Nothing if the operation fails

Remarks

The resulting transform is the result of transforming the math transform with respect to the transformObjIn coordinate frame.

Example

[Set Components and Transforms for Interference Detection (C#)](Set_Components_and_Transforms_for_Interference_Detection_Example_CSharp.htm)  
[Set Components and Transforms for Interference Detection (VB.NET)](Set_Components_and_Transforms_for_Interference_Detection_Example_VBNET.htm)  
[Set Components and Transforms for Interference Detection (VBA)](Set_Components_and_Transforms_for_Interference_Detection_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)  
[IMathTransform::IMultiply Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IMultiply.md)
