# ApplyTransform Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform`

Applies a transform to this body.
Applies a transform to this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ApplyTransform( _
   ByVal Xform As MathTransform _
) As System.Boolean
```

```

Dim instance As IBody2
Dim Xform As MathTransform
Dim value As System.Boolean
 
value = instance.ApplyTransform(Xform)
```

```

System.bool ApplyTransform( 
   MathTransform Xform
)
```

```

System.bool ApplyTransform( 
   MathTransform^ Xform
) 
```

#### Parameters

*Xform*
:   [Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) to apply

#### Return Value

True if the transform is successfully applied, false if not

Remarks

By design, a temporary body is added to the part and displayed in the assembly. The origin of the temporary body is relative to the part instead of the assembly. As a work-around, insert an interim part in the assembly with the origin aligned with the assembly and add the temporary body to the interim part.

Example

[Check Interference (VBA)](Check_Interference_using_Modeler_CheckInterference_Example_VB.htm)  
[Combine Assembly Components into Part (VBA)](Combine_Assembly_Components_into_Part_Example_VB.htm)  
[Cut Body in Half using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
