# GetSpecificTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform`

Get the collapsed or exploded transform of a component when the assembly is exploded.
Get the collapsed or exploded transform of a component when the assembly is exploded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSpecificTransform( _
   ByVal IgnoreExplode As System.Boolean _
) As System.Object
```

```

Dim instance As IComponent2
Dim IgnoreExplode As System.Boolean
Dim value As System.Object
 
value = instance.GetSpecificTransform(IgnoreExplode)
```

```

System.object GetSpecificTransform( 
   System.bool IgnoreExplode
)
```

```

System.Object^ GetSpecificTransform( 
   System.bool IgnoreExplode
) 
```

#### Parameters

*IgnoreExplode*
:   True to get the component's collapsed transform when the assembly is exploded, false to get the component's exploded transform when the assembly is exploded

#### Return Value

[Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Example

[Get Collapsed Transform of Component in Exploded View (C#)](Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_CSharp.htm)  
[Get Collapsed Transform of Component in Exploded View (VB.NET)](Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_VBNET.htm)  
[Get Collapsed Transform of Component in Exploded View (VBA)](Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetTotalTransform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.md)  
[IComponent2::SetTransformAndSolve2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.md)  
[IComponent2::PresentationTransform Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.md)  
[IComponent2::Transform2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md)
