# Hide Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Hide`

Hides this temporary body in the context of the specified part.
Hides this temporary body in the context of the specified part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Hide( _
   ByVal Part As System.Object _
) 
```

```

Dim instance As IBody2
Dim Part As System.Object
 
instance.Hide(Part)
```

```

void Hide( 
   System.object Part
)
```

```

void Hide( 
   System.Object^ Part
) 
```

#### Parameters

*Part*
:   [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Remarks

While SOLIDWORKS is displaying your IBody2 object using [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md), you cannot release it explicitly or implicitly. Before releasing or allowing your IBody2 object to be released, you must call this method to prevent it from being displayed.

COM applications should avoid explicitly releasing the IBody2 object by calling IBody2->Release() while it is being displayed by SOLIDWORKS. Dispatch applications should avoid allowing the IBody2 object to go out of scope while it is being displayed by SOLIDWORKS, and be destroyed when the ReleaseDispatch method is called automatically. Dispatch applications should also avoid explicitly releasing the IBody2 object by calling ReleaseDispatch while it is being displayed by SOLIDWORKS.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)  
[Create and Convert Non-manifold Bodies (C#)](Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm)  
[Create and Convert Non-manifold Bodies (VB.NET)](Create_and_Convert_Non-manifold_Bodies_Example_VBNET.htm)  
[Create and Convert Non-manifold Bodies (VBA)](Create_and_Convert_Non-manifold_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IHide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IHide.md)
